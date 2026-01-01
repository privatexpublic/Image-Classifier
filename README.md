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
作業フォルダで VS Code を起動し`classify.py`を作成するため以下を実行します。  
コードはアップロードされている`classify.py`を参照し、環境に合わせてパスを変更してください。
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
`classify.py`と同じディレクトリ内に `anime_real_model.keras`を置き、以下を実行します。
```sh
python classify.py
```
---

<br>

以上により、任意のフォルダ内の画像が `real` と `anime` フォルダに分けられます。  
確信度が低い画像は `unsure` フォルダに分類されます。



<br>
<br>

## 分類をカスタムしたい場合(anime_real_model.kerasの変更）

## ①データセット構成
Google Driveを以下の構成にし、`real`と`anime`内に分類したいパターンごとに画像を入れます。（最低10枚は必要）  
`unlabeled` は アクティブラーニング用の未分類画像を配置するためのフォルダです。  
今回の手順ではこの工程を省略し、用意した画像をすべて `real` と `anime` に入れても問題ありません。  

```sh
MyDrive/
 └─ dataset/
     ├─ labeled/
     │   ├─ real/
     │   └─ anime/
     └─ unlabeled/
```



## ②KERASファイルを作成
学習用の Google Colab ノートを以下で公開しています。  
リンク先のノートを上から順に実行してください。  
任意の場所で新しいGoogle Colabノートを作成し、それぞれコードを実行していきます。  

https://colab.research.google.com/drive/10bYzTj9edPQxQW4YtpHHBMvfRfDyCC0y?usp=drive_link
<br>
<br>
最後にanime_real_model.kerasをダウンロードし、classify.pyと同じローカルディレクトリに入れて完了です。
