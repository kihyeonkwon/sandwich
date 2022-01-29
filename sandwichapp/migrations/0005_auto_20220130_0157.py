# Generated by Django 3.2.7 on 2022-01-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwichapp', '0004_bread_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='sauce',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='topping',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
