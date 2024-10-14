# Generated by Django 5.1.1 on 2024-10-14 22:24

import users.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email address')),
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='User ID')),
                ('is_bot', models.BooleanField(default=False, verbose_name='Is bot')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Username')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='password')),
                ('groups', models.ManyToManyField(blank=True, related_name='telegram_user_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='telegram_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', users.managers.TelegramUserManager()),
            ],
        ),
    ]
