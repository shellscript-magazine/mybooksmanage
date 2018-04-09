#!/usr/bin/env python3
# coding: utf-8

import requests
import mysql.connector

rakuten_book_api = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
app_id = "アプリケーションID"

def bookinfodb(isbn):
	response = requests.get(rakuten_book_api + "?applicationId=" + app_id + "&isbn=" + isbn)
	if response.json()["count"] == 0:
		print("{}に該当する書籍がありません\n".format(isbn))
	else:
		bookdata = isbn + "\t" + response.json()["Items"][0]["Item"]["title"] +"\t" + response.json()["Items"][0]["Item"]["author"] + "\n"
		title = response.json()["Items"][0]["Item"]["title"]
		author = response.json()["Items"][0]["Item"]["author"] 
		print(bookdata)		
		connect = mysql.connector.connect(user='root', password='MySQL管理者パスワード', host='localhost', database='mybook', charset='utf8mb4')
		cursor = connect.cursor()
		cursor.execute('insert into bookinfo values(%s, %s, %s)',(isbn, title, author))
		connect.commit()
		connect.close()

if __name__ == '__main__':
	try:
		while(True):
			isbn = input('ISBNコードを入力してください\n')
			bookinfodb(isbn)
	except KeyboardInterrupt:
		pass
