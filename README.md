# dakoku
Dakoku is a simple script that uses Python + Selenium to automatically log in to "King of Time" and prompt you to clock in.

**King of Time って、キン・タイってダジャレだよね**

* King of Time への打刻をpython + seleniumを使って自動化するスクリプト
*
* 事前準備：
*
*   Seleniumライブラリをインストーする
*   % pip install selenium
*
* 使い方：
*
*   % python dakoku.py
*
*   Chromeブラウザが起動し、King of Timeへ自動ログインするので打刻しましょう
*   打刻後60秒後にブラウザは自動終了します。
