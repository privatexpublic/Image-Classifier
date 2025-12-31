import os
import shutil
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# 学習済みモデル（classify.pyと同じフォルダに置く）
model = load_model("anime_real_model.keras")

def classify_and_sort(folder_path):
    real_dir = os.path.join(folder_path, "real")
    anime_dir = os.path.join(folder_path, "anime")
    unsure_dir = os.path.join(folder_path, "unsure")

    os.makedirs(real_dir, exist_ok=True)
    os.makedirs(anime_dir, exist_ok=True)
    os.makedirs(unsure_dir, exist_ok=True)

    for file in os.listdir(folder_path):
        if file.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.bmp')):
            path = os.path.join(folder_path, file)

            img = Image.open(path).convert("RGB").resize((128,128))
            arr = np.array(img) / 255.0
            arr = np.expand_dims(arr, axis=0)

            pred = model.predict(arr)[0][0]

            #数字変更により自信のない画像をどうするか調節可能
            if pred >= 0.7:
                shutil.move(path, os.path.join(real_dir, file))
            elif pred <= 0.3:
                shutil.move(path, os.path.join(anime_dir, file))
            else:
                shutil.move(path, os.path.join(unsure_dir, file))


# 整理したい写真が入っているフォルダのパス
folder = r"C:\Users\・・・"

classify_and_sort(folder)
