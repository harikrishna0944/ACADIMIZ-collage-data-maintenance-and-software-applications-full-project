# Generated by Django 4.0.5 on 2022-07-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_addadtimisionenquire_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='addadtimisionenquire_table',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]