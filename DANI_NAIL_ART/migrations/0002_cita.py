# Generated by Django 4.2.4 on 2023-10-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DANI_NAIL_ART', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
    ]