# Generated by Django 2.2.5 on 2020-06-21 20:19

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('logbook_app', '0009_auto_20200617_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorneymodel',
            name='counsel_telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]