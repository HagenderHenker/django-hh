# Generated by Django 3.2.7 on 2021-11-05 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hhapp', '0011_auto_20211026_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='investitionsentwicklung',
            name='afa',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investitionsentwicklung',
            name='istinv',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investitionsentwicklung',
            name='planinv',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=11),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Abgaben',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gliederung', models.IntegerField()),
                ('text', models.CharField(max_length=200)),
                ('abgabesatz', models.DecimalField(decimal_places=2, max_digits=11)),
                ('einheit', models.CharField(max_length=50)),
                ('haushalt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhapp.haushalt')),
            ],
        ),
    ]
