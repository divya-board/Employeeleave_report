# Generated by Django 4.2.4 on 2023-08-22 03:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Empper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_date', models.DateTimeField()),
                ('permissionTime_from', models.DateTimeField()),
                ('permissionTime_To', models.DateTimeField()),
                ('reason', models.CharField(max_length=200, null=True)),
                ('Status', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=200, null=True)),
                ('leave_date_from', models.DateTimeField()),
                ('leave_date_to', models.DateTimeField()),
                ('leave_reason', models.CharField(max_length=200, null=True)),
                ('leave_type', models.CharField(max_length=200, null=True)),
                ('leave_session', models.CharField(max_length=200, null=True)),
                ('Status', models.CharField(max_length=200, null=True)),
                ('emp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='new.emp')),
            ],
        ),
    ]
