# Generated by Django 3.1.3 on 2020-11-20 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(max_length=50, verbose_name='имя блока')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блоки',
            },
        ),
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_name', models.CharField(max_length=50, verbose_name='имя элемента')),
                ('element_text', models.TextField(verbose_name='текст елемента')),
                ('blocks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.blocks')),
            ],
            options={
                'verbose_name': 'Элемент',
                'verbose_name_plural': 'Элементы',
            },
        ),
    ]