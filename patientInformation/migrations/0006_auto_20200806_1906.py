# Generated by Django 3.0.8 on 2020-08-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientInformation', '0005_auto_20200806_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinformation',
            name='uploadDate',
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='ageAtSurgery',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='burnInjury',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='firstName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='hospitalName',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='lastName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='occupation',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='patientAddress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='patientHeight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='patientRecordNumber',
            field=models.SlugField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='patientSex',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], default='male', max_length=6),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='patientWeight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='preoperativeDiagnostic1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='siteCountry',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='siteRegion',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
