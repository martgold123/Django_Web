# Generated by Django 2.2 on 2020-12-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tintuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieude', models.CharField(default='', max_length=255)),
                ('noidung', models.CharField(default='', max_length=255)),
                ('ngaydang', models.DateTimeField(null=True)),
                ('trangthai', models.BooleanField(default=True)),
            ],
        ),
    ]