# Generated by Django 4.0.4 on 2022-06-01 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prestar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_dev', models.DateField()),
                ('fecha_prest', models.DateField()),
                ('ejemplaresid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestar.ejemplares')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ejemplaresid', models.ManyToManyField(related_name='ejemplaresid', through='prestar.Prestar', to='prestar.ejemplares')),
            ],
        ),
        migrations.AddField(
            model_name='prestar',
            name='usuarioid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestar.usuario'),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('num_pag', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=50)),
                ('autorid', models.ManyToManyField(related_name='autorid', to='prestar.autor')),
            ],
        ),
        migrations.AddField(
            model_name='ejemplares',
            name='libro',
            field=models.ManyToManyField(related_name='libro', to='prestar.libro'),
        ),
        migrations.AddField(
            model_name='ejemplares',
            name='usuarioid',
            field=models.ManyToManyField(related_name='usuarioid', through='prestar.Prestar', to='prestar.usuario'),
        ),
    ]
