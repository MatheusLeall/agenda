# Generated by Django 3.1.7 on 2021-03-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
