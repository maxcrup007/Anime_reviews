# Generated by Django 3.0.3 on 2020-10-26 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.ImageField(upload_to='site_media')),
            ],
        ),
        migrations.CreateModel(
            name='spoiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_us', models.BooleanField(default=False)),
                ('spoiled', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
