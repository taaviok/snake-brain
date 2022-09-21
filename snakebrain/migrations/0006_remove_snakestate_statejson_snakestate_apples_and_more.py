# Generated by Django 4.1.1 on 2022-09-21 07:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakebrain', '0005_rename_statejson_snakestate_statejson_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snakestate',
            name='statejson',
        ),
        migrations.AddField(
            model_name='snakestate',
            name='apples',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='snakestate',
            name='scissors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='snakestate',
            name='snakebody',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='snakestate',
            name='snakehead',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
