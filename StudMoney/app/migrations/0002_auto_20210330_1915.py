# Generated by Django 3.1.7 on 2021-03-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('User', 'U'), ('Admin', 'A')], default='User', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='location',
            field=models.CharField(choices=[('Cluj', 'Cj'), ('Bucuresti', 'B')], default='Cluj', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(choices=[('Cluj', 'Cj'), ('Bucuresti', 'B')], default='Cluj', max_length=100),
        ),
    ]