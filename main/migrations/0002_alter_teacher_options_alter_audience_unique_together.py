# Generated by Django 4.1.5 on 2023-04-28 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
        migrations.AlterUniqueTogether(
            name='audience',
            unique_together={('name',)},
        ),
    ]
