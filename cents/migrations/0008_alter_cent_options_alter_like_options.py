# Generated by Django 4.1.5 on 2023-01-11 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cents', '0007_alter_cent_user_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cent',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['-created']},
        ),
    ]