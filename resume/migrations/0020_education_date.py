# Generated by Django 4.2 on 2023-04-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0019_resume_workexperience_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='date',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
