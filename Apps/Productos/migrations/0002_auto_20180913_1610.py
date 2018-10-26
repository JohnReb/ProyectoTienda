# Generated by Django 2.1.1 on 2018-09-13 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto_categoria',
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='producto_categoria',
            name='Producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Categoria'),
        ),
        migrations.DeleteModel(
            name='Producto_Categoria',
        ),
    ]
