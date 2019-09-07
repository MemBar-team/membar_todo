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
 

```
//  mysqlclient インストール
pip install mysqlclient

// 初期化マイグレーション
$python manage.py makemigrations manager
$python manage.py migrate

// アプリ起動
$python manage.py runserver

```