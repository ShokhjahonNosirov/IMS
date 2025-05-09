# Generated by Django 5.2 on 2025-05-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maruza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('image', models.ImageField(upload_to='maruza/')),
                ('file', models.FileField(upload_to='maruza/files/')),
            ],
        ),
    ]
