# Generated by Django 4.1.3 on 2022-11-02 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=255)),
                ('manejador', models.CharField(db_column='manejador', max_length=50)),
                ('valor', models.CharField(db_column='valor', max_length=255)),
            ],
            options={
                'verbose_name': 'configuracion',
                'verbose_name_plural': 'configuraciones',
                'db_table': 'configuracion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DepartamentoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=150)),
                ('active', models.BooleanField(db_column='active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'departamento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstadoUsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('active', models.BooleanField(db_column='active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'estado usuario',
                'verbose_name_plural': 'estado usuarios',
                'db_table': 'estado_usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GeneroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('active', models.BooleanField(db_column='active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'genero',
                'verbose_name_plural': 'generos',
                'db_table': 'genero',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('modulo', models.CharField(db_column='modulo', max_length=300)),
                ('request', models.CharField(blank=True, db_column='request', max_length=800, null=True)),
                ('excepcion', models.CharField(db_column='excepcion', max_length=600)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, db_column='fecha_ingreso')),
            ],
            options={
                'verbose_name': 'log',
                'verbose_name_plural': 'logs',
                'db_table': 'log',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoDocumentoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('active', models.BooleanField(db_column='active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tipo de documentos',
                'verbose_name_plural': 'Tipo documentos',
                'db_table': 'tipo_documento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoUsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('active', models.BooleanField(db_column='active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tipo usuario',
                'verbose_name_plural': 'Tipo usuarios',
                'db_table': 'tipo_usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CiudadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=150)),
                ('active', models.BooleanField(db_column='active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('departamento', models.ForeignKey(db_column='departamento', on_delete=django.db.models.deletion.DO_NOTHING, to='config.departamentomodel')),
            ],
            options={
                'verbose_name': 'ciudad',
                'verbose_name_plural': 'ciudades',
                'db_table': 'ciudad',
                'managed': True,
            },
        ),
    ]
