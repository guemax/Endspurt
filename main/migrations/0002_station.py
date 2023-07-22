# Generated by Django 4.2.3 on 2023-07-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=200, verbose_name='Sportart')),
            ],
            options={
                'verbose_name': 'Station',
                'verbose_name_plural': 'Stationen',
            },
        ),
    ]
