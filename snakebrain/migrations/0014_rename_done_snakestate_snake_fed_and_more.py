# Generated by Django 4.1.1 on 2022-10-10 10:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakebrain', '0013_remove_snakestate_reward_snakestate_action'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snakestate',
            old_name='done',
            new_name='snake_fed',
        ),
        migrations.AddField(
            model_name='snakestate',
            name='snake_dead',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='snakestate',
            name='action',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='snakestate',
            name='apples',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='snakestate',
            name='scissors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='snakestate',
            name='score',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='snakestate',
            name='snakebody',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='snakestate',
            name='snakehead',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='snakestate',
            name='walls',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
