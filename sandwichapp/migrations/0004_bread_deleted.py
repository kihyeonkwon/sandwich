# Generated by Django 3.2.7 on 2022-01-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwichapp', '0003_sandwich_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bread',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]