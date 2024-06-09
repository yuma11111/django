from django.db import models

# Create your models here.

class BookRecord(models.Model):
    #id（主キー）
    id = models.AutoField(primary_key=True)
    #書籍名
    name = models.CharField(max_length=100)
    #書籍のシリーズID
    series_id = models.IntegerField(null=True)
    #詳細
    detail = models.TextField(null=True)
    #所有しているか
    have = models.BooleanField(default=False)
    #発売日
    release_date = models.DateTimeField(null=True)
    #削除フラグ
    delete_flg = models.BooleanField(default=False)
    #インサート日
    insert_date = models.DateTimeField()
    #アップデート日
    update_date = models.DateTimeField()

class series(models.Model):
    #id（主キー）
    id = models.AutoField(primary_key=True)
    #書籍のシリーズID
    series_id = models.IntegerField()
    #シリーズ名
    series_name = models.CharField(max_length=100)
    #詳細
    detail = models.TextField(null=True)
    #削除フラグ
    delete_flg = models.BooleanField(default=False)
    #インサート日
    insert_date = models.DateTimeField()
    #アップデート日
    update_date = models.DateTimeField()
