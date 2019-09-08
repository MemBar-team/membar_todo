#TODOリストアプリ
 ## アプリ起動
 
 // 環境変数例
```buildoutcfg
export MEMBAR_DB_NAME="d_mason"
export MEMBAR_USER="dmason"
export MEMBAR_PASSWORD="dmason"
export MEMBAR_HOST="127.0.0.1"
export MEMBAR_PORT="3306"
``` 
 
```commandline 
// 仮想環境起動
$ source membar_todo_env/bin/activate

// 仮想環境のpipまとめインストール
$ pip install --upgrade pip
$ pip install -r requirements.txt

//  mysqlclient インストール
$ pip install mysqlclient

// 初期化マイグレーション
$ python manage.py makemigrations <対象APP>
$ python manage.py migrate

// アプリ起動
$ python manage.py runserver

```