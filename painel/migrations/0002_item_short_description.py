# Generated by Django 4.0.2 on 2022-02-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='short_description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
