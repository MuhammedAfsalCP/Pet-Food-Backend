from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from products.models import Products
from users.serializer import User

from .models import Order, OrderItem,Notification
from .serializer import (AllOrderSerializer, OrderItemSerializer,
                         OrderSerializer,NotificationSerializer)


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def create_notification(user, message):
    notification = Notification.objects.create(user=user, message=message)
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user.id}",  # group name should match in consumer
        {
            "type": "send_notification",
            "message": message,
            "timestamp": str(notification.created_at)
        }
    )

class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


class OrderView(ListAPIView):

    pagination_class = ProductPagination
    serializer_class = OrderSerializer

    def get_queryset(self):

        user = self.request.user
        return Order.objects.filter(user=user)

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class OrderUpdate(APIView):

    def put(self, request, pk):
        action = request.data.get("method")
        if not action:
            return Response({"error": "Missing method action"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = OrderItem.objects.get(Q(id=pk) & ~Q(status="Cancelled"))
        except OrderItem.DoesNotExist:
            return Response("Invalid Product", status=status.HTTP_400_BAD_REQUEST)

        order = product.order

        if action == "Cancelled":
            item_total = product.item_subtotal
            order.total_price -= item_total
            product.status = "Cancelled"

        elif action in ["Shipped", "Delivered"]:
            product.status = action
            create_notification(order.user, f"Your order item '{product.product.Name}' is now {action}.")

        else:
            return Response({"error": "Invalid action method"}, status=status.HTTP_400_BAD_REQUEST)

        order.updated_at = timezone.now()
        order.save()
        product.save()

        return Response("Updated", status=status.HTTP_202_ACCEPTED)

class allorder(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        order = Order.objects.all()
        serializer = AllOrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class Specificorder(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            orderitem = Order.objects.get(id=pk)
        except:
            return Response("invalidProduct", status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(orderitem, context={"request": request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class TotalPayment(APIView):
    def get(self, request):

        total_orders = Order.objects.filter(items__status="Delivered")

        users = User.objects.filter(Q(is_staff=False) & Q(is_deleted=False))
        total_revenue = sum(order.total_price for order in total_orders)
        orders = Order.objects.all()
        products = Products.objects.filter(is_deleted=False)

        print(total_revenue)

        return Response(
            {
                "totalrevanue": total_revenue,
                "userlength": len(users),
                "orderlen": len(orders),
                "productlen": len(products),
            },
            status=status.HTTP_200_OK,
        )
class NotificationListAPIView(APIView):
    

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

# 2. Unread count
class UnreadNotificationCountAPIView(APIView):
  

    def get(self, request):
        count = Notification.objects.filter(user=request.user, is_read=False).count()
        return Response({"unread_count": count})

# 3. Mark one notification as read
class MarkAllNotificationsAsReadAPIView(APIView):

    def post(self, request):
        notifications = Notification.objects.filter(user=request.user, is_read=False)
        notifications.update(is_read=True)
        return Response({"message": "All notifications marked as read."})