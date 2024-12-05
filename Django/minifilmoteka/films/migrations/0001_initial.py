# Generated by Django 5.1.4 on 2024-12-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('poster_url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
