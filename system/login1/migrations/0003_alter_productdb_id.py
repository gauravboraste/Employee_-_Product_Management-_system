# Generated by Django 3.2.6 on 2021-09-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login1', '0002_auto_20210901_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]