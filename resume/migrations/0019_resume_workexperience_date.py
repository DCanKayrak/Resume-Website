# Generated by Django 4.2 on 2023-04-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_certificate_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='workexperience',
            name='date',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
