# Generated by Django 4.1 on 2022-09-06 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Mercaderia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo_barra', models.IntegerField(max_length=20)),
                ('cantidad', models.IntegerField(max_length=300)),
                ('fecha_vencimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
