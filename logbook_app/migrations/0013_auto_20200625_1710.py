# Generated by Django 2.2.5 on 2020-06-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook_app', '0012_auto_20200621_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorneymodel',
            name='disposal',
            field=models.CharField(choices=[('CN', 'Conviction'), ('AC', 'Acquittal'), ('SO', 'Struck Out– Want Of Diligent Prosecution'), ('DS', 'Dismissal– No Case Submission')], max_length=2),
        ),
        migrations.AlterField(
            model_name='attorneymodel',
            name='reason_for_adjournment',
            field=models.CharField(choices=[('CDN', 'Court Did Not Sit'), ('ABP', 'Absent Prosecution'), ('AC', 'Absent Defence Counsel'), ('AD', 'Absent Defendant'), ('PNR', 'Prosecution Not Ready'), ('PR', 'Request Prosecution'), ('RC', 'Request Counsel'), ('HD', 'Heard'), ('NHD', 'Not Heard')], max_length=4),
        ),
    ]