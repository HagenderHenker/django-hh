# Generated by Django 3.2.7 on 2021-10-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhapp', '0010_auto_20211023_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berechnungsgrundlagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haushaltsjahr', models.IntegerField(unique=True)),
                ('nivellierungssatz_GrStA', models.IntegerField()),
                ('nivellierungssatz_GrStB', models.IntegerField()),
                ('nivellierungssatz_GewSt', models.IntegerField()),
                ('landesdurchschnittliche_stk', models.DecimalField(decimal_places=2, max_digits=8)),
                ('achwellenwertSZA', models.DecimalField(decimal_places=2, max_digits=8)),
                ('schwellensatzSZA', models.DecimalField(decimal_places=2, max_digits=5)),
                ('schluesselsatzb1', models.DecimalField(decimal_places=2, max_digits=8)),
                ('einheitlgrundbetragb2', models.DecimalField(decimal_places=2, max_digits=8)),
                ('einheitlgrundbetragb2inv', models.DecimalField(decimal_places=2, max_digits=8)),
                ('landesdurchschnGebietsfl', models.DecimalField(decimal_places=4, max_digits=6)),
                ('landesdurchschnittliche_stkFinAUmlage', models.DecimalField(decimal_places=2, max_digits=14)),
                ('umlageZVS', models.DecimalField(decimal_places=2, max_digits=4)),
                ('gewStumlageverf', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='steuerkraft',
            unique_together={('gemeinde', 'haushaltsjahr')},
        ),
    ]