# インスタnt サプライズ！

## 概要
サプライズのお店探しを簡単にするWeb上プラットフォーム
Hottpepperのお店情報＋Instagram投稿画像でお店の雰囲気がもっとわかりやすく！
予算やエリアで絞り込み可能！ AIでInstagram投稿画像を分類して気になるバースデープレートなどを優先表示します！

## APIの動作
必要なものをインストール
pip install -r requirements.txt

## Version
Django 2.1.5

## Usage

Windows Command Prompt

```
cd Instant_Surprise
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata hotpepper_instatag.json
pythonmanage.py runserver
```

## MEMO
db.sqlite3という隠しファイルがデータベースの実体のよう
　
データ消すにはappの中のmigrationsとdb.sqlite3を一度消してから
python manage.py makemigrations appを実行して作り直してください．
　
起動後の管理ツールからデータを入れたり消したりしようとするとエラーを吐いちゃって
調べたらなんかDjangoとデータベースのSQliteのバージョンの問題とか出たけど改善しなかった
（管理ツールからデータ入れない，仕様ってことにしよう）
（最後に管理ツールやデータ追加のリンクは見えないように消すといいかな）
　
今データの画面開くのにユーザーログインいる状態だけどいらないように消していいかなと思う
