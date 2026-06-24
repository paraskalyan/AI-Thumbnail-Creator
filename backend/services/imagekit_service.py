from imagekitio import ImageKit
from openai import base_url
from config import IMAGEKIT_PRIVATE_KEY, IMAGEKIT_PUBLIC_KEY, IMAGEKIT_URL_ENDPOINT

imagekit = ImageKit(private_key=IMAGEKIT_PRIVATE_KEY)

# Function to upload_file
def upload_file(file_bytes: bytes, file_name: str, folder: str = "/", content_type: str='image/png') -> dict:
    response = imagekit.files.upload(
        file=file_bytes,
        file_name=file_name,
        folder=folder,
        content_type=content_type,
        is_private_file=False,
        use_unique_file_name=True,
    )
    return response.url

def get_variants(base_url: str) -> dict:
    return{
        "youtube": f"{base_url}?tr=w-1280,h-720,fo-auto",
        "shorts": f"{base_url}?tr=w-1080,h-1920,fo-auto",
        "square": f"{base_url}?tr=w-1080,h-1080,fo-auto",
    }