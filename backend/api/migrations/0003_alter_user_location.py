# Generated by Django 5.0.3 on 2024-03-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_latitude_remove_user_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
