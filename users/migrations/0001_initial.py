# Generated by Django 2.1.1 on 2018-11-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True, verbose_name='date created')),
                ('first_name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('surname_name', models.CharField(max_length=200)),
                ('maiden_name', models.CharField(max_length=200)),
                ('academic_level', models.CharField(max_length=100)),
            ],
        ),
    ]