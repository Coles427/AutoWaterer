# Generated by Django 2.2.1 on 2019-06-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190601_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterdat',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='waterdat',
            name='plant_num',
            field=models.IntegerField(),
        ),
    ]
