# Generated by Django 4.2.1 on 2023-05-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tonometr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sys', models.IntegerField(default=0)),
                ('dys', models.IntegerField(default=0)),
                ('puls', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]