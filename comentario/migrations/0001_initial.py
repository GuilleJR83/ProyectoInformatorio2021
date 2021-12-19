# Generated by Django 4.0 on 2021-12-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuenta', '0001_initial'),
        ('publicacion', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField(max_length=250)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuenta.usuario')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacion.publicacion')),
            ],
        ),
    ]
