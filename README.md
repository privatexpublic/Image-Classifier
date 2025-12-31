# 実写画像・二次元画像 自動分類ツール（Windows / 無料環境）

## 概要
このプロジェクトは、  **AI（機械学習）を用いてフォルダ内の画像を自動判別し、  「実写画像」と「二次元画像（アニメ・イラスト・スクリーンショット）」に分類するツール**です。

- 学習：Google Colab（無料・GPU使用）
- 実行：Windows ローカル環境（Anaconda + Python）
- モデル保存形式：`.keras`（Keras 推奨形式）

---

## 使用技術
- Python 3.10（実行言語）
- TensorFlow / Keras（モデル読み込み・推論）
- NumPy（画像を配列に変換）
- Pillow（画像読み込み・リサイズ）
- Anaconda（仮想環境管理）
- Google Colab（学習用）

---

## 全体構成と役割分担
| 作業 | 環境 |
|----|----|
| データセット準備 | Google Drive |
| モデル学習 | Google Colab |
| モデル保存 | Google Drive |
| 画像分類 | Windows（ローカル） |

---

## 手順
## ① Anaconda のインストール（Windows）
Anaconda は **Python の実行環境を安全に分離して管理できるツール**です。

以下の公式サイトからダウンロード  
https://www.anaconda.com/products/distribution

手順は以下を参照  
https://envader.plus/article/530

### ~ Anaconda Prompt を使う理由 ~
本プロジェクトでは **仮想環境** を以下の理由で使用します。

- Python のバージョン衝突を防ぐ
- ライブラリ管理を明確にする


## ② 仮想環境を作成・有効化
Anaconda Prompt を起動して以下を実行します。

```sh
conda activate myenv
```
(myenv) C:\Users\...
となれば、今はmyenvという箱（仮想環境）の中で作業していることを意味します。


## ③ 必要ライブラリのインストール（Windows）
仮想環境myenvが有効な状態で以下を実行します。
```sh
pip install numpy tensorflow pillow opencv-python scikit-learn matplotlib
```


## ④ 分類スクリプトの作成
作業フォルダで VS Code を起動しclassify.pyを作成するため以下を実行します。
コードはアップロードされているclassify.pyを参照してください。
```sh
code classify.py　（メモ帳を使う場合はnotepad classify.pyでもよい）
```

## ⑤ モデルのダウンロード
GitHubのファイルサイズ制限のため、学習済みモデルは外部ストレージに配置しています。  
以下のリンクから `anime_real_model.keras` をダウンロードしてください。

https://drive.google.com/drive/folders/1MweaBHzv5CL1xOCG2tLy64340vWuZ02s?usp=drive_link

※ Google Drive では、サイズの大きいバイナリファイルに対して  
「ウイルススキャン可能な上限サイズを超えています」という警告が表示される場合があります。  
これは Google Drive の仕様によるものであり、ファイル自体の危険性を示すものではありません。


## ⑥ スクリプトの実行
classify.pyと同じディレクトリ内にとanime_real_model.kerasを置き、以下を実行します。
```sh
python classify.py
```
---

<br>

以上により、任意のフォルダ内の画像がrealとanimeファイルに分かれます。



<br>
<br>

# 分類をカスタムしたい場合(anime_real_model.kerasの変更）

## ①データセット構成
Google Driveを以下の構成にし、realとanime内に分類したいパターンに分けて写真を入れます。（最低10枚は必要）
```sh
MyDrive/
 └─ dataset/
     ├─ real/
     └─ anime/
```



## ②KERASファイルを作成
任意の場所で新しいGoogle Colabノートを作成し、それぞれコードを実行していきます。  
  
以下はGoogle Drive をマウントするためのコードです。
```python
from google.colab import drive
drive.mount('/content/drive')
```

以下はデータセット構成のdatasetにアクセスするためのコードです。
```python
data_dir = "/content/drive/MyDrive/dataset"
```

以下はモデル作成コードです。
```python
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_gen = datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val_gen = datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(128,128,3)),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(train_gen, validation_data=val_gen, epochs=10)
```
以下は学習したモデルを指定したパスにファイルとして保存するためのコードです。
```python
model.save("/content/drive/MyDrive/anime_real_model.keras")
```
<br>
<br>
最後にanime_real_model.kerasをダウンロードし、classify.pyと同じディレクトリに入れて完了です。
