# Generated by Django 4.2.14 on 2024-07-31 11:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scrap',
            unique_together={('user', 'post')},
        ),
    ]
