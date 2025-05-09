# Generated by Django 5.2 on 2025-04-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_course_enrolled_users_delete_usercourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('image', models.ImageField(upload_to='books/')),
                ('file', models.FileField(upload_to='books/files/')),
            ],
        ),
    ]
