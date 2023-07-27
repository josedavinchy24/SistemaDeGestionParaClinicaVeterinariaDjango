# Generated by Django 4.2.1 on 2023-05-28 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("veterinaria", "0004_rename_idmascota_mascota_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="factura",
            name="cedulaDueno",
            field=models.ForeignKey(
                db_column="cedulaDueno",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facturas_dueno",
                to="veterinaria.persona",
            ),
        ),
        migrations.AlterField(
            model_name="factura",
            name="idMascota",
            field=models.ForeignKey(
                db_column="idMascota",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facturas_mascota",
                to="veterinaria.mascota",
            ),
        ),
        migrations.AlterField(
            model_name="factura",
            name="idorden",
            field=models.ForeignKey(
                blank=True,
                db_column="idOrden",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facturas_orden",
                to="veterinaria.orden",
            ),
        ),
    ]