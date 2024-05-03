# Generated by Django 5.0.4 on 2024-05-03 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_history', '0001_initial'),
        ('patients', '0002_patient_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medical_history.medicalhistory'),
        ),
    ]