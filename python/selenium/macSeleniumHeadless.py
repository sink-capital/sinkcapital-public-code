# -*- coding: utf-8 -*-

# 宣言部分
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# chromedriverの設定
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
# driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
driver = webdriver.Chrome('/opt/chrome/chromedriver', options=options)

# 特定のサイト（Yahoo!検索）にアクセスする
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
    print(a.find_element_by_tag_name('h3').text)
    print(a.get_attribute('href'))
    print("--------")

# 終了処理
driver.close()
