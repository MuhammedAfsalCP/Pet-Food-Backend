from django.urls import path

from .views import (OrderUpdate, OrderView, Specificorder, TotalPayment,
                    allorder,NotificationListAPIView,UnreadNotificationCountAPIView,MarkAllNotificationsAsReadAPIView)

urlpatterns = [
    path("orderview/", OrderView.as_view()),
    path("orderupdate/<int:pk>/", OrderUpdate.as_view()),
    path("allorder/", allorder.as_view()),
    path("sepecificorder/<int:pk>/", Specificorder.as_view()),
    path("totalpayment/", TotalPayment.as_view()),
    path("notifications/", NotificationListAPIView.as_view()),
     path('notifications/', NotificationListAPIView.as_view(), name='notification-list'),
    path('notifications/unread-count/', UnreadNotificationCountAPIView.as_view(), name='notification-unread-count'),
    path('notifications/mark-all-read/', MarkAllNotificationsAsReadAPIView.as_view(), name='notification-mark-read')

]
