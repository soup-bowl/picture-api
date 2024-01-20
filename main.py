from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from typing import Union
import os
import random

app = FastAPI()

@app.get("/")
async def get_random_image():
    images_directory = "/images"
    try:
        images = [file for file in os.listdir(images_directory) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        if not images:
            raise HTTPException(status_code=404, detail="No images found in the directory")
        
        random_image = random.choice(images)
        image_path = os.path.join(images_directory, random_image)

        response = FileResponse(image_path)
        response.headers["Cache-Control"] = "no-store"
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
