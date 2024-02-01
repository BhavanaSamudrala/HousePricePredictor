# Generated by Django 4.0.3 on 2022-04-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=2)),
                ('area', models.IntegerField()),
                ('flat_type', models.IntegerField()),
                ('prediction', models.FloatField()),
                ('search_frequency', models.IntegerField(default=1)),
            ],
        ),
    ]