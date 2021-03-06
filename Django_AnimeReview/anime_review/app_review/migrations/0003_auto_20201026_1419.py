# Generated by Django 3.0.3 on 2020-10-26 07:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_review', '0002_allboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('favor', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('dropdown', models.TextField(blank=True, null=True)),
                ('mute', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='allboard',
            name='commentation',
        ),
        migrations.AddField(
            model_name='allboard',
            name='category',
            field=models.CharField(choices=[('Love-Comedy', 'Love-Comedy'), ('Action', 'Action'), ('Adventure', 'Adventure'), ('Fantasy', 'Fantasy'), ('Drama', 'Drama'), ('Romance', 'Romance')], default='Love-Comedy', max_length=100),
        ),
        migrations.AlterField(
            model_name='allboard',
            name='favor',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='allboard',
            name='header',
            field=models.CharField(max_length=200),
        ),
    ]
