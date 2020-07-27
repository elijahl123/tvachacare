# Generated by Django 3.0.8 on 2020-07-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientInformation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinformation',
            name='TBSA',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='ageAtSurgery',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='approximateYearOfInjury',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='burnInjury',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='causeOfBurn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='currentMedication',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='dateOfBirth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='degreeOfBurn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='hospitalName',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='occupation',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='parentFirstName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='parentLastName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='parentMiddleName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='patientAddress',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='patientHeight',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='patientPhoneNumber',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='patientRecordNumber',
            field=models.SlugField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='patientSex',
            field=models.CharField(choices=[('male', 'female')], default='male', max_length=6),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='patientWeight',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='preferredName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='preoperativeDiagnostic1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='preoperativeDiagnostic2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='preoperativeDiagnostic3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='preoperativeDiagnostic4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='referral',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='relationshipToParent',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='siteCountry',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='siteRegion',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='uploadDate',
            field=models.DateField(auto_now=True),
        ),
    ]
