import os
import shutil
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model("anime_real_model.keras")#classifyと同じディレクトリに入れる

def classify_and_sort(folder_path):
    real_dir = os.path.join(folder_path, "real")
    anime_dir = os.path.join(folder_path, "anime")

    os.makedirs(real_dir, exist_ok=True)
    os.makedirs(anime_dir, exist_ok=True)

    for file in os.listdir(folder_path):
        if file.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.bmp')):
            path = os.path.join(folder_path, file)

            img = Image.open(path).convert("RGB").resize((128,128))
            arr = np.array(img) / 255.0
            arr = np.expand_dims(arr, axis=0)

            pred = model.predict(arr)[0][0]

            if pred > 0.5:
                shutil.move(path, os.path.join(real_dir, file))
            else:
                shutil.move(path, os.path.join(anime_dir, file))


#整理したい写真たちが入っているフォルダ
folder = r"C:\Users\・・・"
classify_and_sort(folder)