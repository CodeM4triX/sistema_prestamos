# Generated by Django 5.1.5 on 2025-02-05 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField()),
                ('prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.prestamo')),
            ],
        ),
    ]
