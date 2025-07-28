import cloudinary
import cloudinary.uploader
from decouple import config

# Configure Cloudinary
cloudinary.config(
    cloud_name="dhvjaalwh",
    api_key="866668241343445",
    api_secret="V9c-gBmB0E-1X4Qjuyt5b8VxecU"
)

def upload_image_to_cloudinary(image_file, image_name):
    try:
        result = cloudinary.uploader.upload(
            image_file,
            public_id=f"products/{image_name}",
            resource_type="image"
        )
        return result.get("secure_url")
    except Exception as e:
        print("Cloudinary upload error:", e)
        return None
