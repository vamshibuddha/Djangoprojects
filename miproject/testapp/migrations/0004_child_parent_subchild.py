# Generated by Django 3.1.2 on 2020-10-23 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20201023_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fd1', models.CharField(max_length=128)),
                ('fd2', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.parent')),
                ('fd3', models.CharField(max_length=128)),
                ('fd4', models.CharField(max_length=128)),
            ],
            bases=('testapp.parent',),
        ),
        migrations.CreateModel(
            name='SubChild',
            fields=[
                ('child_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.child')),
                ('fd5', models.CharField(max_length=128)),
            ],
            bases=('testapp.child',),
        ),
    ]
