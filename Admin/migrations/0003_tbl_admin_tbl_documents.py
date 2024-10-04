# Generated by Django 5.0.4 on 2024-06-17 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_email', models.CharField(max_length=50)),
                ('admin_contact', models.CharField(max_length=50)),
                ('admin_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents_name', models.CharField(max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_service')),
            ],
        ),
    ]