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
* 使い方：
*
*   % python kintai-dakoku.py
*
*   Chromeブラウザが起動し、King of Timeへ自動ログインするので打刻しましょう
*   打刻後60秒後にブラウザは自動終了します。
"""
# library
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# setting
login_url='https://s3.ta.kingoftime.jp/independent/recorder2/personal/#'
id="trme**********"
password="*************"

# Chrome Webドライバー の インスタンスを生成
driver = webdriver.Chrome()

# WebドライバーでKing of Timeログインページを起動
driver.get(login_url)

driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys(id)
driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(password)
# CLASS属性が”sessions_button--wide”であるHTML要素を取得してクリック
driver.find_element(By.CLASS_NAME,"btn-control-message").click()

# マイページへ移動
driver.get(login_url)

print("打刻待ち...")
time.sleep(60)
print("終了")

# Webドライバー の セッションを終了
driver.quit()