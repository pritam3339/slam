# Generated by Django 2.1.7 on 2019-02-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_q1'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='q1',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
