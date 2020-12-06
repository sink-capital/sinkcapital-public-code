# selenium
seleniumの勉強に利用したコード格納リポジトリ

## インストール
```shell script
$ brew install chromedriver
$ pip install selenium
```

## 実行
### ローカル実行

```shell script
$ python macSelenium.py 
```

画面が立ち上がり「selenium」の検索をして終わる

### docker実行（chrome-headless）

```shell script
$ docker build -t tmp-train .
$ docker run -v `pwd`:/usr/src/app tmp-train
  Google
  Python - Google 検索
  ('プログラミング言語 Python - python.jp', 'https://www.python.jp/')
  ('Welcome to Python.org', 'https://www.python.org/')
  ('Pythonってどんな言語なの？ (1/2)：Python入門 - ＠IT', 'https://www.atmarkit.co.jp/ait/articles/1904/02/news024.html')
  ('Python | プログラミングの入門なら基礎から学べるProgate ...', 'https://prog-8.com/languages/python')
  ('Python - ウィキペディア', 'https://ja.wikipedia.org/wiki/Python')
  ('Python入門 ～Pythonのインストール方法やPythonを使った ...', 'https://www.javadrive.jp/python/')
  ('Pythonとは？大人気プログラミング言語のメリットや活用事例 ...', 'https://www.internetacademy.jp/it/programming/programming-basic/what-is-python.html')
  ('Python - Qiita', 'https://qiita.com/tags/python')
  ('とほほのPython入門 - とほほのWWW入門', 'http://www.tohoho-web.com/python/')
```

## 参考リンク
- [たった3行のpythonで始めるSelenium入門](https://qiita.com/mastar_3104/items/0a1ce2bfa1d29287bc35)
- [Docker上で、Python + Selenium + Headless Chromeを使用してWEBスクレイピング](https://oliversi.com/2019/01/07/python-docker-selenium-chrome/)
- [スクレイピング初心者が３時間でスクレイピングをやってみた](https://qiita.com/yuji_sakurai/items/c3720c899593b7ab3ba8)
