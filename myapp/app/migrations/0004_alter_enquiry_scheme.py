# Generated by Django 5.0.7 on 2024-08-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_enquiry_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='scheme',
            field=models.CharField(choices=[(10, 'General'), (40, 'Referal'), (80, 'walking')], max_length=10),
        ),
    ]
