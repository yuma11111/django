# Generated by Django 5.0.4 on 2024-06-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('series_id', models.IntegerField(null=True)),
                ('detail', models.TextField(null=True)),
                ('have', models.BooleanField(default=False)),
                ('release_date', models.DateTimeField(null=True)),
                ('delete_flg', models.BooleanField(default=False)),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('series_id', models.IntegerField()),
                ('series_name', models.CharField(max_length=100)),
                ('detail', models.TextField(null=True)),
                ('delete_flg', models.BooleanField(default=False)),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
            ],
        ),
    ]