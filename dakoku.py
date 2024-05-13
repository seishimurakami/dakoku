# -*- coding: utf-8 -*-
"""
*
* King of Time への打刻をpython + seleniumを使って自動化するスクリプト
*
* 事前準備：
*
*   Seleniumライブラリをインストーする
*   % pip install selenium
*
*   Seleniumライブラリ 4.20でテストしています。
*   % pip show selenium 
*     Name: selenium
*     Version: 4.20.0
*
* 使い方：
*
*   % python dakoku.py
*
*   Chromeブラウザが起動し、King of Timeへ自動ログインするので打刻しましょう。
*   出勤・退勤ボタンが押されるか・ブラウザが閉じられるまで待機します。
"""
# library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# setting
login_url='https://s3.ta.kingoftime.jp/independent/recorder2/personal/#'
id="trme**********"
password="*************"

# Chrome Webdriverのインスタンスを生成
driver = webdriver.Chrome()

# King of Timeログインページを起動
driver.get(login_url)

try:
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys(id)
    driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(password)
    driver.find_element(By.CLASS_NAME,"btn-control-message").click()
except:
    print("ログインエラー")
    driver.quit()
    exit()

# ログインページへ移動
driver.get(login_url)

# 出勤・退勤ボタンが押されるか・ブラウザが閉じられるまで待機
while True:
    text_element = driver.find_element(By.CLASS_NAME,"notification-message").text
    print(text_element)
    if text_element == "退勤が完了しました。":
        break
    elif text_element == "出勤が完了しました。":
        break
    try: 
        # ブラウザが閉じられた場合、例外が発生するので、例外処理でループを抜ける
        driver.find_element(By.CLASS_NAME,"wrapper-all")
        time.sleep(1)
    except: 
        break

# Webdriverのセッションを終了
driver.quit()
