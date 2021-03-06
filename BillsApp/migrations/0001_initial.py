# Generated by Django 2.0.5 on 2018-07-05 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnesBills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=30)),
                ('money', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
                ('mood', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='onesbills',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BillsApp.UserInfo'),
        ),
    ]
