# Generated by Django 3.2.4 on 2022-01-02 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='updated_at',
        ),
    ]