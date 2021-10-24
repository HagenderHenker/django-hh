# Generated by Django 3.2.7 on 2021-10-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hhapp', '0008_gemeindestatistik_schluesselzuweisunga_schluesselzuweisungb1_schluesselzuweisungb2_steuerkraft_steue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datafiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile', models.FileField(upload_to='')),
                ('datafileuploaddate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='haushalt',
            name='datendatei',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hhapp.datafiles'),
        ),
    ]
