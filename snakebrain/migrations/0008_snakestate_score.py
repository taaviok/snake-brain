# Generated by Django 4.1.1 on 2022-09-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakebrain', '0007_alter_snakestate_apples_alter_snakestate_gameid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='snakestate',
            name='score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
