# Generated by Django 4.1.4 on 2023-01-16 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_note_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='note'),
        ),
    ]
