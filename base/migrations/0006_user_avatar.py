# Generated by Django 5.1.2 on 2024-11-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_event_date_event_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.png', upload_to=''),
        ),
    ]
