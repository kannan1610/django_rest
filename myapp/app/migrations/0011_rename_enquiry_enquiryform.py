# Generated by Django 5.0.7 on 2024-08-08 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_enquiry_qualification_alter_enquiry_stream'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enquiry',
            new_name='EnquiryForm',
        ),
    ]
