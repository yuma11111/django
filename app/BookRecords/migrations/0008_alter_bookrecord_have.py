# Generated by Django 5.0.4 on 2024-06-29 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookRecords', '0007_alter_bookrecord_have'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecord',
            name='have',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]