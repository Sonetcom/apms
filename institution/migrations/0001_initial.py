# Generated by Django 2.1.1 on 2018-11-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inst_num', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['inst_num'],
            },
        ),
    ]
