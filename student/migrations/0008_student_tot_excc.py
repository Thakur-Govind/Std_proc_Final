# Generated by Django 2.2.5 on 2019-09-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_remove_student_hunter'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='tot_excc',
            field=models.IntegerField(default=0),
        ),
    ]
