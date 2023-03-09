# Generated by Django 4.1.7 on 2023-02-25 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='News.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Категория'),
        ),
    ]
