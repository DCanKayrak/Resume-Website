# Generated by Django 4.2 on 2023-04-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
