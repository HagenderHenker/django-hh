# Generated by Django 3.2.6 on 2021-09-28 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hhapp', '0007_alter_haushalt_docxtemplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steuerkraftgrunddaten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haushaltsjahr', models.IntegerField()),
                ('ist1_grundsteuera', models.IntegerField()),
                ('ist2_grundsteuera', models.IntegerField()),
                ('ist3_grundsteuera', models.IntegerField()),
                ('ber_grundsteuera', models.IntegerField()),
                ('hs_grundsteuera', models.IntegerField()),
                ('gz2_grundsteuera', models.IntegerField()),
                ('ist4_grundsteueravj', models.IntegerField()),
                ('ber_grundsteueravj', models.IntegerField()),
                ('hs_grundsteueravj', models.IntegerField()),
                ('gz1_grundsteueravj', models.IntegerField()),
                ('nivs_grundsteuera', models.IntegerField()),
                ('ist1_grundsteuerb', models.IntegerField()),
                ('ist2_grundsteuerb', models.IntegerField()),
                ('ist3_grundsteuerb', models.IntegerField()),
                ('ber_grundsteuerb', models.IntegerField()),
                ('hs_grundsteuerb', models.IntegerField()),
                ('gz2_grundsteuerb', models.IntegerField()),
                ('ist4vj_grundsteuerb', models.IntegerField()),
                ('ber_grundsteuerbvj', models.IntegerField()),
                ('hs_grundsteuerbvj', models.IntegerField()),
                ('gz1_grundsteuerbvj', models.IntegerField()),
                ('nivs_grundsteuerb', models.IntegerField()),
                ('ist1_gewerbesteuer', models.IntegerField()),
                ('ist2_gewserbeteuer', models.IntegerField()),
                ('ist3_gewerbesteuer', models.IntegerField()),
                ('hs_gewerbesteuer', models.IntegerField()),
                ('ist4vj_gewerbesteuer', models.IntegerField()),
                ('hs_gewerbesteuervj', models.IntegerField()),
                ('ist1_eksteuer', models.IntegerField()),
                ('ist2_eksteuer', models.IntegerField()),
                ('ist3_eksteuer', models.IntegerField()),
                ('ist4vj_eksteuer', models.IntegerField()),
                ('ist1_usteuer', models.IntegerField()),
                ('ist2_usteuer', models.IntegerField()),
                ('ist3_usteuer', models.IntegerField()),
                ('ist4vj_usteuer', models.IntegerField()),
                ('ist1_ausgl', models.IntegerField()),
                ('ist2_ausgl', models.IntegerField()),
                ('ist3_ausgl', models.IntegerField()),
                ('ist4vj_ausgl', models.IntegerField()),
                ('gemeinde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhapp.gemeinde')),
            ],
        ),
        migrations.CreateModel(
            name='Steuerkraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haushaltsjahr', models.IntegerField()),
                ('stk_grundsteuera', models.IntegerField()),
                ('stk_grundsteuerb', models.IntegerField()),
                ('stk_gewerbesteuer', models.IntegerField()),
                ('stk_eksteuer', models.IntegerField()),
                ('stk_usteuer', models.IntegerField()),
                ('stk_ausgl', models.IntegerField()),
                ('gemeinde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhapp.gemeinde')),
            ],
        ),
        migrations.CreateModel(
            name='SchluesselzuweisungB2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haushaltsjahr', models.IntegerField()),
                ('gemeinde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhapp.gemeinde')),
            ],
        ),
        migrations.CreateModel(
            name='SchluesselzuweisungB1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haushaltsjahr', models.IntegerField()),
                ('szb1_satz', models.DecimalField(decimal_places=2, max_digits=11)),
                ('szb1_betrag', models.IntegerField()),
                ('gemeinde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhapp.gemeinde')),
            ],
        ),
        migrations.CreateModel(
            name='SchluesselzuweisungA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haushaltsjahr', models.IntegerField()),
                ('steuerkraftmesszahl', models.IntegerField()),
                ('einwohner', models.IntegerField()),
                ('stkproew', models.DecimalField(decimal_places=2, max_digits=11)),
                ('landesdurchschnstkproew', models.DecimalField(decimal_places=2, max_digits=11)),
                ('schwellenwert', models.DecimalField(decimal_places=2, max_digits=11)),
                ('diff_stkproewschwellenwert', models.DecimalField(decimal_places=2, max_digits=11)),
                ('schluesselzuw', models.IntegerField()),
                ('gemeinde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhapp.gemeinde')),
            ],
        ),
        migrations.CreateModel(
            name='Gemeindestatistik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haushaltsjahr', models.IntegerField()),
                ('ew30_06', models.IntegerField()),
                ('gemeinde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhapp.gemeinde')),
            ],
        ),
    ]
