# -*- coding: utf-8 -*-

# 宣言部分
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sqlite3

dbname = 'database.db'
conn = sqlite3.connect(dbname)
c = conn.cursor()
table_name = 'test'

# chromedriverの設定
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
# driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
driver = webdriver.Chrome('/opt/chrome/chromedriver', options=options)


def create_table(tname):
    drop_table = '''drop table if EXISTS {}'''.format(tname)
    c.execute(drop_table)
    # executeメソッドでSQL文を実行する
    create_table = '''create table if NOT EXISTS {} (title varchar(64), url varchar(64))'''.format(tname)
    c.execute(create_table)


def insert_data(tname, data):
    # 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
    # executemanyメソッドを実行する
    insert_sql = 'insert into {0} (title, url) values (?,?)'.format(tname)
    c.executemany(insert_sql, data)
    conn.commit()


if __name__ == '__main__':
    create_table(table_name)
    # 特定のサイト（Google検索）にアクセスする
    driver.get("https://google.co.jp")

    print(driver.title)
    # 確認01
    assert 'Google' in driver.title

    # 検索窓を操作する
    input_elem = driver.find_element_by_name("q")
    input_elem.clear()
    input_elem.send_keys('Python')
    input_elem.send_keys(Keys.RETURN)
    # driver.implicitly_wait(20)

    print(driver.title)
    # 確認02
    assert 'Python' in driver.title

    # 必要な情報を取得、出力
    for a in driver.find_elements_by_css_selector('#rso .g .rc .yuRUbf > a'):
        insert_data(table_name, [(a.find_element_by_tag_name('h3').text, a.get_attribute('href'))])

    # 終了処理
    driver.close()

    select_sql = 'select * from {0}'.format(table_name)
    for row in c.execute(select_sql):
        print(row)
