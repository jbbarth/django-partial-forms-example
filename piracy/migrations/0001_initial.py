# Generated by Django 2.0.5 on 2018-05-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pirate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_captain', models.BooleanField()),
            ],
            options={
                'db_table': 'pirates',
            },
        ),
    ]
