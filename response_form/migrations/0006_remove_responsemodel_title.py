# Generated by Django 2.1.7 on 2019-03-07 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('response_form', '0005_responsemodel_submit_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsemodel',
            name='title',
        ),
    ]