# Generated by Django 4.1.7 on 2023-02-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('birthday', models.DateTimeField()),
                ('is_live', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Люди',
                'verbose_name_plural': 'Люди',
                'ordering': ['age'],
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
