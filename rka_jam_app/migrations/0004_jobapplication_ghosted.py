# Generated by Django 5.0.4 on 2024-04-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rka_jam_app', '0003_alter_jobapplication_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='ghosted',
            field=models.BooleanField(default=False, help_text='If I was ghosted in this process'),
        ),
    ]
