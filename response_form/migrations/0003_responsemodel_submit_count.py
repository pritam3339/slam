# Generated by Django 2.1.7 on 2019-02-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response_form', '0002_responsemodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsemodel',
            name='submit_count',
            field=models.IntegerField(default=0),
        ),
    ]
