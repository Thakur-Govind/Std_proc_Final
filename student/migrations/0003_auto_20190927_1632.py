# Generated by Django 2.2.5 on 2019-09-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190927_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
