# Generated by Django 5.0.1 on 2024-01-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.IntegerField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'Create',
            },
        ),
    ]
