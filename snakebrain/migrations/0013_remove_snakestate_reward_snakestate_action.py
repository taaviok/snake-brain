# Generated by Django 4.1.1 on 2022-10-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakebrain', '0012_alter_snakestate_reward'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snakestate',
            name='reward',
        ),
        migrations.AddField(
            model_name='snakestate',
            name='action',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]