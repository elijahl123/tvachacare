# Generated by Django 3.0.8 on 2020-08-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('profile_picture_path', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('group', models.CharField(choices=[('Admin', 'Admin'), ('Approver', 'Approver'), ('Data Entry', 'Data Entry')], default='Admin', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=120, null=True)),
                ('lastName', models.CharField(max_length=120, null=True)),
                ('patientRecordNumber', models.SlugField(max_length=11, null=True)),
                ('preferredName', models.CharField(blank=True, max_length=120, null=True)),
                ('dateOfBirth', models.DateField(null=True)),
                ('ageAtSurgery', models.IntegerField(null=True)),
                ('patientSex', models.CharField(choices=[('female', 'female'), ('male', 'male')], default='male', max_length=6)),
                ('siteCountry', models.CharField(max_length=120, null=True)),
                ('siteRegion', models.CharField(max_length=120, null=True)),
                ('hospitalName', models.TextField(null=True)),
                ('preoperativeDiagnostic1', models.TextField(null=True)),
                ('preoperativeDiagnostic2', models.TextField(blank=True, null=True)),
                ('preoperativeDiagnostic3', models.TextField(blank=True, null=True)),
                ('preoperativeDiagnostic4', models.TextField(blank=True, null=True)),
                ('burnInjury', models.BooleanField(default=False)),
                ('TBSA', models.FloatField(blank=True, null=True)),
                ('degreeOfBurn', models.IntegerField(blank=True, null=True)),
                ('causeOfBurn', models.TextField(blank=True, null=True)),
                ('approximateYearOfInjury', models.IntegerField(blank=True, null=True)),
                ('occupation', models.CharField(max_length=120, null=True)),
                ('patientAddress', models.TextField(null=True)),
                ('patientPhoneNumber', models.CharField(blank=True, max_length=12, null=True)),
                ('parentFirstName', models.CharField(blank=True, max_length=120, null=True)),
                ('parentMiddleName', models.CharField(blank=True, max_length=120, null=True)),
                ('parentLastName', models.CharField(blank=True, max_length=120, null=True)),
                ('relationshipToParent', models.CharField(blank=True, max_length=120, null=True)),
                ('uploadDate', models.DateField(auto_now=True)),
                ('referral', models.CharField(blank=True, max_length=120, null=True)),
                ('patientWeight', models.IntegerField(null=True)),
                ('patientHeight', models.IntegerField(null=True)),
                ('currentMedication', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
