# Generated by Django 5.1.5 on 2025-02-06 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_rename_slag_categories_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('id',), 'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
    ]
