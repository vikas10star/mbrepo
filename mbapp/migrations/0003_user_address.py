# Generated by Django 3.0.5 on 2020-04-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbapp', '0002_user_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]