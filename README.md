# ISBNから書籍リストを作成するアプリ

バーコードリーダーやキーボードから入力したISBN番号で「タイトル」「著者」のリストを作成できる
アプリケーションです。プログラミング言語「Python」のバージョン3で記述しています。書籍情報は
楽天ブックスから取り込んでいます。 リストは、タブ区切りテキストとして「mybook.txt」ファイル
に保存されます。

Python 3が動作する環境を用意してください。読み書き可能な任意のディレクトリーに「booksmanage.py」
とmybook.txtを保存します。 「 https://webservice.rakuten.co.jp/api/booksbooksearch/ 」に
アクセスして「アプリID発行」をクリックし、ログインしてからアプリを作成します。表示された「アプリ
ID」に、booksmanage.pyの「アプリケーションID」（7行目）を書き換えます。  

次のように実行すると、アプリが起動します。  

$ python3 booksmanage.py  

あるいはbooksmanage.pyに実行権限を与え、直接実行します。  

$ chmod +x booksmanage.py     
$ ./booksmanage  

「ISBNコードを入力してください」が表示されたら、ISBN番号をバーコードから読み込ませたり、キーボ
ードから入力したりします。楽天ブックスを検索して書籍のタイトルと著者名が表示されます。同時に
mybook.txtにISBN、タイトル、著者名が保存されます。  
［Ctrl］キーを押しながら［C］キーを押すと、アプリが終了します。

## MySQLにデータを保存する
データベース管理システム「MySQL」に書籍データを保存するアプリ（booksmanagedb.py）を作成しました。
「booksmanagedb.py」と「bookinfo.sql」を任意のディレクトリーに保存してください。  

Ubuntu（16.04 LTS）の場合、次のようにして実行環境を作成します。MySQLと、MySQLにpython 3プログラムからアクセスするための「mysql.connector」モジュールを導入します。
MySQLの管理者パスワードの設定画面が開いたら、任意のパスワードを入力します。  

$ sudo apt update  
$ sudo apt install -y mysql-server python3-mysql.connector     

MySQLで使用する言語を4バイトのUTF-8に設定します。クライアントとサーバーの設定を書き換えたら、サーバーを再起動します。  

$ sudo sh -c "echo 'default-character-set=utf8mb4'>> /etc/mysql/conf.d/mysql.cnf"    
$ sudo sh -c "echo 'character-set-server=utf8mb4' >> /etc/mysql/mysql.conf.d/mysqld.cnf"      
$ sudo systemctl restart mysql      

書籍データ保存用の「mybook」データベース、「bookinfo」テーブルを作成します。  

$ mysqladmin -u root create mybook -p     
MySQL管理者パスワードを入力     

$ mysql -u root -p mybook < bookinfo.sql    
MySQL管理者パスワードを入力    

「 https://webservice.rakuten.co.jp/api/booksbooksearch/ 」に
アクセスして「アプリID発行」をクリックし、ログインしてからアプリを作成します。表示された「アプリ
ID」に、booksmanagedb.pyの「アプリケーションID」（8行目）を書き換えます。booksmanagedb.pyの「MySQL管理者
パスワード」（20行目）を、MySQLのインストール時に設定したパスワードに書き換えます。
次のように実行すると、アプリが起動します。  

$ python3 booksmanagedb.py    

あるいはbooksmanagedb.pyに実行権限を与え、直接実行します。  

$ chmod +x booksmanagedb.py     
$ ./booksmanagedb    

「ISBNコードを入力してください」が表示されたら、ISBN番号をバーコードから読み込ませたり、キーボ
ードから入力したりします。楽天ブックスを検索して書籍のタイトルと著者名が表示されます。同時に
bookinfoテーブルにISBN、タイトル、著者名が保存されます。［Ctrl］キーを押しながら［C］キーを押すと、アプリが終了します。    

## 古い書籍にも対応する
古い書籍は、楽天ブックスに登録されていません。そのため、「ISBNから書籍リストを作成するアプリ」（booksmanage.py）では、登録されていない書籍は無視されます。「booksmanage2.py」では、「mylist.txt」にタブ区切り形式で「ISBN」「タイトル」「著者名」を記述しておけば、そのファイルも検索してISBNに一致するものがそれらの情報を書籍リストに登録します。    
mylist.txtにサンプルとなる例を記述しているので、それに合わせて登録されていない書籍情報を追記してください。次のように実行すると、アプリが起動します。  

$ python3 booksmanage2.py    

あるいはbooksmanagedb.pyに実行権限を与え、直接実行します。  

$ chmod +x booksmanage2.py           
$ ./booksmanagedb    

「ISBNコードを入力してください」が表示されたら、ISBN番号をバーコードから読み込ませたり、キーボ
ードから入力したりします。楽天ブックスおよびmylist.txtを検索して書籍のタイトルと著者名が表示されます。同時に
同時にmybook.txtにISBN、タイトル、著者名が保存されます。［Ctrl］キーを押しながら［C］キーを押すと、アプリが終了します。   

written by Jiro Aso
