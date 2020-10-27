# Generated by Django 3.1.1 on 2020-10-27 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_auto_20201027_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unreg_students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_app.institute')),
            ],
        ),
    ]
