# Generated by Django 5.1.4 on 2025-01-06 09:34

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(blank=True, max_length=100, null=True)),
                ('speciality_en', models.CharField(blank=True, max_length=100, null=True)),
                ('speciality_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('speciality_ky', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.TextField(blank=True, null=True)),
                ('shift_start', models.TimeField(blank=True, null=True)),
                ('shift_end', models.TimeField(blank=True, null=True)),
                ('qualifications', models.TextField(blank=True, null=True)),
                ('qualifications_en', models.TextField(blank=True, null=True)),
                ('qualifications_ru', models.TextField(blank=True, null=True)),
                ('qualifications_ky', models.TextField(blank=True, null=True)),
                ('experience_year', models.PositiveSmallIntegerField(default=1)),
                ('working_days', models.JSONField()),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Doctor', 'Doctor'), ('Patient', 'Patient')], max_length=32)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('address', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency_contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('blood_type', models.CharField(blank=True, max_length=3, null=True)),
                ('blood_type_en', models.CharField(blank=True, max_length=3, null=True)),
                ('blood_type_ru', models.CharField(blank=True, max_length=3, null=True)),
                ('blood_type_ky', models.CharField(blank=True, max_length=3, null=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('allergies_en', models.TextField(blank=True, null=True)),
                ('allergies_ru', models.TextField(blank=True, null=True)),
                ('allergies_ky', models.TextField(blank=True, null=True)),
                ('medical_history', models.TextField(blank=True, null=True)),
                ('medical_history_en', models.TextField(blank=True, null=True)),
                ('medical_history_ru', models.TextField(blank=True, null=True)),
                ('medical_history_ky', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(blank=True, max_length=100, null=True)),
                ('diagnosis_en', models.CharField(blank=True, max_length=100, null=True)),
                ('diagnosis_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('diagnosis_ky', models.CharField(blank=True, max_length=100, null=True)),
                ('treatment', models.CharField(blank=True, max_length=100, null=True)),
                ('treatment_en', models.CharField(blank=True, max_length=100, null=True)),
                ('treatment_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('treatment_ky', models.CharField(blank=True, max_length=100, null=True)),
                ('prescribed_medication', models.TextField(blank=True, null=True)),
                ('prescribed_medication_en', models.TextField(blank=True, null=True)),
                ('prescribed_medication_ru', models.TextField(blank=True, null=True)),
                ('prescribed_medication_ky', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('comment_en', models.TextField(blank=True, null=True)),
                ('comment_ru', models.TextField(blank=True, null=True)),
                ('comment_ky', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Billings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('issued_date', models.DateField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('planned', 'Planned'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=32)),
                ('notes', models.TextField(blank=True, null=True)),
                ('notes_en', models.TextField(blank=True, null=True)),
                ('notes_ru', models.TextField(blank=True, null=True)),
                ('notes_ky', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.CharField(blank=True, max_length=32, null=True)),
                ('medication_en', models.CharField(blank=True, max_length=32, null=True)),
                ('medication_ru', models.CharField(blank=True, max_length=32, null=True)),
                ('medication_ky', models.CharField(blank=True, max_length=32, null=True)),
                ('dosage', models.CharField(blank=True, max_length=32, null=True)),
                ('dosage_en', models.CharField(blank=True, max_length=32, null=True)),
                ('dosage_ru', models.CharField(blank=True, max_length=32, null=True)),
                ('dosage_ky', models.CharField(blank=True, max_length=32, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Wards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_type', models.CharField(choices=[('common', 'Common'), ('vip', 'VIP')], max_length=32)),
                ('capacity', models.PositiveSmallIntegerField(default=1)),
                ('current_occupancy', models.PositiveSmallIntegerField(default=1)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.patientprofile')),
            ],
        ),
    ]
