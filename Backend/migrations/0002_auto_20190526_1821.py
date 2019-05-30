# Generated by Django 2.2 on 2019-05-26 18:21

import Backend.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noteapp',
            name='email',
        ),
        migrations.RemoveField(
            model_name='noteapp',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='noteapp',
            name='name',
        ),
        migrations.RemoveField(
            model_name='noteapp',
            name='photoUrl',
        ),
        migrations.RemoveField(
            model_name='noteapp',
            name='userID',
        ),
        migrations.AddField(
            model_name='authentication',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='authentication',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='noteapp',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='noteapp',
            name='notesApp',
            field=djongo.models.fields.ArrayModelField(default=[], model_container=Backend.models.Notes),
        ),
        migrations.AddField(
            model_name='noteapp',
            name='password',
            field=models.CharField(default='admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='authentication',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='authentication',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='noteapp',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]