from django.db import models

# Create your models here.
class membar_todo(models.Model):
    #・タスク名 name varchar
    #・タスク詳細 contents varchar
    #・実行フラグ done_flag varchar(1)
    #・論理削除フラグ delete_at varchar
    #・作成日時 create_at datetime
    name      = models.CharField(max_length=50)
    contents  = models.CharField(max_length=200)
    done_flag = models.CharField(max_length=1)
    delete_at = models.DateField()
    create_at = models.DateField()