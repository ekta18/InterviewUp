# Generated by Django 4.0.2 on 2022-05-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewup_app', '0002_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartupNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'newsstartup',
            },
        ),
        migrations.CreateModel(
            name='TechNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'newstech',
            },
        ),
    ]