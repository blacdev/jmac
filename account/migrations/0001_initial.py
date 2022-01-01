# Generated by Django 3.2.4 on 2022-01-01 19:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='accountInfo',
            fields=[
                ('accounts_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='account.accounts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='User', serialize=False, to='account.accounts')),
                ('bank_name', models.CharField(blank=True, max_length=30)),
                ('account_number', models.CharField(blank=True, max_length=30)),
                ('account_name', models.CharField(blank=True, max_length=30)),
                ('account_type', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.accounts',),
        ),
    ]
