# Generated by Django 5.0.3 on 2024-05-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_pdfhistory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfhistory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pdfhistory',
            name='pdf',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]