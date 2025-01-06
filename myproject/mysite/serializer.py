from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(format('%d-%m-%Y'))
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'role', 'phone_number',
                  'profile_picture', 'address', 'date_of_birth']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['speciality']


class DoctorDetailSerializer(serializers.ModelSerializer):
    shift_start = serializers.TimeField(format('%H:%M'))
    shift_end = serializers.TimeField(format('%H:%M'))
    class Meta:
        model = Doctor
        fields = ['speciality', 'department', 'shift_start', 'shift_end',
                  'qualifications', 'experience_year', 'working_days', 'price']


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['user', 'emergency_contact', 'blood_type', 'allergies', 'medical_history']


class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient']


class AppointmentDetailSerializer(serializers.ModelSerializer):
    date_time = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date_time', 'status', 'notes']


class MedicalRecordListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = MedicalRecord
        fields = ['patient']


class MedicalRecordDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at']


class PrescriptionsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Prescriptions
        fields = ['patient', 'doctor', 'medication', 'dosage', 'created_at']


class BillingsSerializer(serializers.ModelSerializer):
    issued_date = serializers.DateField(format('%d-%m-%Y'))
    class Meta:
        model = Billings
        fields = ['patient', 'total_amount', 'paid', 'issued_date']


class WardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wards
        fields = ['name', 'ward_type', 'capacity', 'current_occupancy']


class FeedbackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['doctor']


class FeedbackDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['doctor', 'patient', 'rating', 'comment']
