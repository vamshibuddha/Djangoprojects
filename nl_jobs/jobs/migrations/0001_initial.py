# Generated by Django 3.1.2 on 2020-10-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nl_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_no', models.IntegerField()),
                ('job_des', models.CharField(max_length=20)),
                ('job_loc', models.CharField(max_length=20)),
                ('job_skill', models.CharField(max_length=50)),
                ('job_sal', models.FloatField()),
                ('job_stdt', models.DateField()),
            ],
        ),
    ]
