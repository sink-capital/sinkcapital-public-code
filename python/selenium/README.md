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
  プログラミング言語 Python - python.jp
  https://www.python.jp/
  --------
...
```

## 参考リンク
- [たった3行のpythonで始めるSelenium入門](https://qiita.com/mastar_3104/items/0a1ce2bfa1d29287bc35)
