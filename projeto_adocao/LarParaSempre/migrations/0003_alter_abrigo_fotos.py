# Generated by Django 4.1.5 on 2023-01-03 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LarParaSempre', '0002_alter_abrigo_fotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abrigo',
            name='fotos',
            field=models.ImageField(upload_to=''),
        ),
    ]
