# Generated by Django 3.1.5 on 2021-01-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='age',
            field=models.IntegerField(),
        ),
    ]
