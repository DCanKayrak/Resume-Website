# Generated by Django 4.2 on 2023-04-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='company',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
