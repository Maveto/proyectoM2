# Generated by Django 2.2.8 on 2020-03-21 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido_Paterno', models.CharField(max_length=30)),
                ('Apellido_Materno', models.CharField(max_length=30)),
                ('Mail', models.EmailField(max_length=254)),
                ('CI', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=30)),
                ('Tema', models.CharField(max_length=50)),
                ('Contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Docente')),
                ('Lectura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Lectura')),
            ],
        ),
    ]
