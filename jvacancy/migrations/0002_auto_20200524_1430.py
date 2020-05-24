# Generated by Django 3.0.5 on 2020-05-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jvacancy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='MEDIA_SPECIALITY_IMAGE_DIR'),
        ),
    ]
