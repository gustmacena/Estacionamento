# Generated by Django 5.1.6 on 2025-02-26 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_veiculo', models.CharField(max_length=50)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dia_semana', models.CharField(max_length=20)),
            ],
        ),
    ]
