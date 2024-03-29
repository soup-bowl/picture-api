from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from io import BytesIO
from PIL import Image
from typing import Union
import os
import random

app = FastAPI()

def resize_image(input_path: str, size: tuple) -> BytesIO:
    with Image.open(input_path) as img:
        target_ratio = size[0] / size[1]
        img_ratio = img.width / img.height

        if img_ratio > target_ratio:
            # X Crop
            new_width = int(target_ratio * img.height)
            left = (img.width - new_width) / 2
            img_cropped = img.crop((left, 0, left + new_width, img.height))
        elif img_ratio < target_ratio:
            # Y crop
            new_height = int(img.width / target_ratio)
            top = (img.height - new_height) / 2
            img_cropped = img.crop((0, top, img.width, top + new_height))
        else:
            img_cropped = img

        img_resized = img_cropped.resize(size, Image.LANCZOS)

        img_stream = BytesIO()
        img_resized.save(img_stream, format='JPEG')
        img_stream.seek(0)
        return img_stream

def save_string(text: str) -> None:
    with open('/tmp/choosenimage.txt', 'w') as file:
        file.write(text)

def check_string(text: str) -> bool:
    try:
        with open('/tmp/choosenimage.txt', 'r') as file:
            saved_string = file.read()
        return saved_string == text
    except FileNotFoundError:
        return False

def select_image(images, images_directory):
    while True:
        random_image = random.choice(images)
        image_path = os.path.join(images_directory, random_image)

        if not check_string(image_path):
            save_string(image_path)
            return image_path

@app.get("/")
async def get_random_image():
    images_directory = "/images"
    try:
        images = [file for file in os.listdir(images_directory) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        if not images:
            raise HTTPException(status_code=404, detail="No images found in the directory")
        
        image_path = select_image(images, images_directory)
        resized_image = resize_image(image_path, (800, 480))

        response = Response(content=resized_image.read(), media_type="image/jpeg")
        response.headers["Cache-Control"] = "no-store"
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
