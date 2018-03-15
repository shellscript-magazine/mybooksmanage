#! /usr/bin/env python3
# coding: utf-8

import requests
import sys

rakuten_book_api = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
app_id = "アプリケーションID"

def bookinfo(isbn):
	response = requests.get(rakuten_book_api + "?applicationId=" + app_id + "&isbn=" + isbn)
	if response.json()["count"] == 0:
		print("{}に該当する書籍がありません\n".format(isbn))
	else:
		bookdata = isbn + "\t" + response.json()["Items"][0]["Item"]["title"] +"\t" + response.json()["Items"][0]["Item"]["author"] + "\n"
		print(bookdata)
		with open('mybook.txt','a') as f:
			f.write(bookdata)


if __name__ == '__main__':
	try:
		while(True):
			isbn = input('ISBNコードを入力してください\n')
			bookinfo(isbn)
	except KeyboardInterrupt:
		pass
