# Generated by Django 5.1 on 2024-08-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_alter_trainee_address_alter_trainee_birth_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='image',
            field=models.ImageField(blank=True, upload_to='trainee/images'),
        ),
    ]