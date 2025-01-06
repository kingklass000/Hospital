from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import PositiveSmallIntegerField
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    ROLE = [
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient')
    ]
    role = models.CharField(max_length=32, choices=ROLE)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.username} - {self.address}'


class PatientProfile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='patient_profile')
    emergency_contact = PhoneNumberField(region='KG', null=True, blank=True)
    blood_type = models.CharField(max_length=3, null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.blood_type} - {self.allergies} - {self.medical_history}'


class Doctor(models.Model):
    speciality = models.CharField(max_length=100, null=True, blank=True)
    department = models.TextField(null=True, blank=True)
    shift_start = models.TimeField(null=True, blank=True)
    shift_end = models.TimeField(null=True, blank=True)
    qualifications = models.TextField(null=True, blank=True)
    experience_year = models.PositiveSmallIntegerField(default=1)
    working_days = models.JSONField()
    price = PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.speciality} - {self.department} - {self.qualifications}'


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True, blank=True)
    STATUS = [
        ('planned', 'Planned'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=32, choices=STATUS)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.patient} - {self.doctor} - {self.notes}'


class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=100, null=True, blank=True)
    treatment = models.CharField(max_length=100, null=True, blank=True)
    prescribed_medication = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.patient} - {self.doctor} - {self.diagnosis} - {self.treatment} - {self.prescribed_medication}'


class Prescriptions(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medication = models.CharField(max_length=32, null=True, blank=True)
    dosage = models.CharField(max_length=32, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.patient} - {self.doctor} - {self.medication} - {self.dosage}'


class Billings(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    total_amount = models.PositiveSmallIntegerField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    issued_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.patient


class Wards(models.Model):
    name = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    WARP_TYPE = [
        ('common', 'Common'),
        ('vip', 'VIP')
    ]
    ward_type = models.CharField(max_length=32, choices=WARP_TYPE)
    capacity = models.PositiveSmallIntegerField(default=1)
    current_occupancy = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.patient} - {self.doctor} - {self.comment}'