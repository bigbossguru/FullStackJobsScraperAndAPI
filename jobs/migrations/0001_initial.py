# Generated by Django 3.2.13 on 2022-05-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, unique=True)),
                ('company', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('salary', models.CharField(blank=True, max_length=200, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
