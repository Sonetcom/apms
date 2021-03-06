# Generated by Django 2.1.5 on 2019-02-10 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.IntegerField()),
                ('street_name', models.CharField(default='default', max_length=200)),
                ('post_code', models.CharField(default='default', max_length=70)),
                ('province', models.CharField(default='default', max_length=100)),
                ('city', models.CharField(default='default', max_length=100)),
                ('country', models.CharField(default='default', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='I_Adminstrator',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Person')),
                ('i_admin_id', models.CharField(default='default', max_length=20)),
                ('inst_id', models.CharField(default='default', max_length=20)),
            ],
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='S_Adminstrator',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Person')),
                ('s_admin_id', models.CharField(default='default', max_length=20)),
                ('inst_id', models.CharField(default='default', max_length=20)),
            ],
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Person')),
                ('stud_id', models.CharField(default='default', max_length=20)),
                ('intrests', models.CharField(default='default', max_length=500)),
                ('n_first_name', models.CharField(default='default', max_length=70)),
                ('n_surname_name', models.CharField(default='default', max_length=70)),
                ('n_email', models.CharField(default='default', max_length=70)),
            ],
            bases=('users.person',),
        ),
        migrations.AddField(
            model_name='person',
            name='cell_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default='default', max_length=40),
        ),
        migrations.AddField(
            model_name='person',
            name='home_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='profile',
            field=models.CharField(default='default', max_length=400),
        ),
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='person',
            name='work_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='academic_level',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='default', max_length=70),
        ),
        migrations.AlterField(
            model_name='person',
            name='maiden_name',
            field=models.CharField(default='default', max_length=70),
        ),
        migrations.AlterField(
            model_name='person',
            name='second_name',
            field=models.CharField(default='default', max_length=70),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname_name',
            field=models.CharField(default='default', max_length=70),
        ),
    ]
