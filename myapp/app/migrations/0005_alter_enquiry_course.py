# Generated by Django 5.0.7 on 2024-08-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_enquiry_scheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='course',
            field=models.CharField(choices=[(6000, 'Microsoft'), (8000, 'Tally'), (10000, 'Programming')], max_length=20),
        ),
    ]
