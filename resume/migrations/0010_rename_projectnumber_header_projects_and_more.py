# Generated by Django 4.2 on 2023-04-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_header_experience_header_happyclients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header',
            old_name='projectNumber',
            new_name='projects',
        ),
        migrations.AlterField(
            model_name='header',
            name='experience',
            field=models.CharField(max_length=4),
        ),
    ]
