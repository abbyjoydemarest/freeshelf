# Generated by Django 2.1.7 on 2019-03-13 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190312_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='category',
            name='book_category',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='access_online',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_category',
        ),
        migrations.AddField(
            model_name='book',
            name='book_category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
