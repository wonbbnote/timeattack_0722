# Generated by Django 4.0.6 on 2022-07-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'apply_status',
            },
        ),
    ]
