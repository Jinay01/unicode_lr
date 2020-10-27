# Generated by Django 3.1.1 on 2020-10-27 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(blank=True, max_length=40, null=True)),
                ('name', models.CharField(max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_institute', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_faculty', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Faculty', 'Faculty'), ('Institute', 'Institute')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chat_app.account')),
                ('address', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
            bases=('chat_app.account',),
        ),
    ]