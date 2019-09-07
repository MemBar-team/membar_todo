#TODOリストアプリ
 ## アプリ起動
    ```
    //  mysqlclient インストール
    pip install mysqlclient
    
    // 初期化マイグレーション
    $python manage.py makemigrations membar_todo
    $python manage.py migrate
    
    // アプリ起動
    $python manage.py runserver
  
    ```