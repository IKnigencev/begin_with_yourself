# Generated by Django 4.0 on 2022-09-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideamodel',
            name='flag',
        ),
        migrations.AddField(
            model_name='ideamodel',
            name='coordinate_y',
            field=models.FloatField(default=None, help_text='По этим коориднатам будет отражаться метка вашей идеи.', verbose_name='Координаты места'),
        ),
    ]
