# Generated by Django 4.1.7 on 2023-02-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0004_profession_alter_human_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='human',
            options={'ordering': ['age'], 'verbose_name': 'Люди', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterField(
            model_name='profession',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Профессия'),
        ),
    ]
