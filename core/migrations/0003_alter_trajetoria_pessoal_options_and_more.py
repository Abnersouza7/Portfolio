# Generated by Django 5.0.1 on 2024-01-29 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_trajetoria_pessoal_trajetoria_profissional_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trajetoria_pessoal',
            options={'verbose_name': 'trajetoria pessoal', 'verbose_name_plural': 'trajetoria pessoal'},
        ),
        migrations.AddField(
            model_name='trajetoria_pessoal',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='trajetoria pessoal'),
        ),
        migrations.AddField(
            model_name='trajetoria_profissional',
            name='description',
            field=models.TextField(default=1, verbose_name='trajetoria profissional'),
            preserve_default=False,
        ),
    ]
