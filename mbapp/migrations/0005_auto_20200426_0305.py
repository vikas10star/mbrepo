# Generated by Django 3.0.5 on 2020-04-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbapp', '0004_tblemp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('manager', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_emp',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TblEmp',
        ),
    ]
