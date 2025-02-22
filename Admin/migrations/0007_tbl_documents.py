# Generated by Django 5.0.4 on 2024-06-17 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_delete_tbl_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents_name', models.CharField(max_length=100)),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_certificate')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_service')),
            ],
        ),
    ]
