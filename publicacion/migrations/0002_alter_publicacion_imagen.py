# Generated by Django 4.0 on 2021-12-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]