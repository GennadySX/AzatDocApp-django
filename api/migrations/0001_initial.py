# Generated by Django 3.0.4 on 2020-03-05 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('desc', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desc', models.TextField(max_length=350)),
                ('category_id', models.ManyToManyField(to='api.Categories')),
            ],
            options={
                'verbose_name': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(verbose_name='Описания темы (текст)')),
                ('theme_id', models.ManyToManyField(to='api.Themes')),
            ],
            options={
                'verbose_name': 'Описание темы',
            },
        ),
    ]
