# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(verbose_name='Nombre', max_length=100, default='')),
                ('descripcion', models.TextField(verbose_name='Descripción', blank=True, null=True, default='')),
                ('codigo', models.CharField(verbose_name='Código', max_length=10, blank=True, null=True)),
                ('facultad', models.CharField(verbose_name='Facultad', max_length=30, blank=True, null=True, default='0', choices=[('0', 'Facultad de Sistemas'), ('1', 'Facultad de Industrial'), ('2', 'Facultad de Civil'), ('3', 'Facultad de Eléctrica'), ('4', 'Facultad de Ciencias y Tecnología')])),
                ('fecha_de_creacion', models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)),
                ('fecha_de_actualizacion', models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Asignaturas',
                'db_table': 'asignaturas',
                'ordering': ['facultad', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombreEST', models.CharField(verbose_name='Nombre', max_length=100, default='')),
                ('apellidoEST', models.CharField(verbose_name='Apellido', max_length=100, blank=True, null=True, default='')),
                ('edadEST', models.PositiveIntegerField(verbose_name='Edad', blank=True, null=True)),
                ('generoEST', models.CharField(verbose_name='Género', max_length=30, blank=True, null=True, default='otros', choices=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('otros', 'Otros')])),
                ('salarioEST', models.DecimalField(verbose_name='Salario', blank=True, null=True, max_digits=9, decimal_places=2)),
                ('fecha_de_creacionEST', models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)),
                ('fecha_de_actualizacionEST', models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Estudiantes',
                'db_table': 'estudiantes',
                'ordering': ['nombreEST', 'apellidoEST'],
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nota', models.DecimalField(max_digits=4, decimal_places=2)),
                ('fecha_de_creacionNot', models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)),
                ('fecha_de_actualizacionNot', models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)),
                ('asignatura', models.ForeignKey(verbose_name='Asignatura', blank=True, null=True, to='semestral.Asignatura')),
                ('estudiante', models.ForeignKey(verbose_name='Estudiante', blank=True, null=True, to='semestral.Estudiante')),
            ],
            options={
                'verbose_name_plural': 'Notas',
                'db_table': 'notas',
                'ordering': ['nota', 'asignatura', 'estudiante'],
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombreProf', models.CharField(verbose_name='Nombre', max_length=50, default=None)),
                ('apellidoProf', models.CharField(verbose_name='Apellido', max_length=50, default=None)),
                ('cedulaProf', models.CharField(verbose_name='Cedula', max_length=50, default=None)),
                ('fecha_de_creacionProf', models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)),
                ('fecha_de_actualizacionProf', models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Profesor',
                'db_table': 'profesor',
                'ordering': ['nombreProf', 'apellidoProf'],
            },
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ForeignKey(verbose_name='Profesor', blank=True, null=True, default=None, to='semestral.Profesor'),
        ),
    ]
