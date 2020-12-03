# -*- coding: utf-8 -*-

from selenium import webdriver #Selenium Webdriverをインポートして

driver = webdriver.Chrome("/usr/local/bin/chromedriver") #Chromeを動かすドライバを読み込み

driver.get("https://google.co.jp") #googleを開く！

text = driver.find_element_by_name("q") # ID属性から検索用テキストボックスの要素を取得し
text.send_keys("selenium") # 文字列"selenium"をテキストボックスに入力

btn = driver.find_element_by_name("btnK") # 検索用ボタンにはID属性がないのでname属性から取得し
driver.implicitly_wait(1)
btn.click() # 対象をクリック！
