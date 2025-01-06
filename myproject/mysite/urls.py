from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'patient_profile', PatientProfileViewSet, basename='patient-profile_list')
router.register(r'prescriptions', PrescriptionsViewSet, basename='prescriptions_list')
router.register(r'billings', BillingsViewSet, basename='billings_list')
router.register(r'wards', WardsViewSet, basename='wards_list')

urlpatterns = [
    path('', include(router.urls)),
    path('doctor/', DoctorListApiView.as_view(), name='doctor_list'),
    path('doctor/<int:pk>/', DoctorDetailApiView.as_view(), name='doctor_detail'),
    path('appointment/', AppointmentListApiView.as_view(), name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentDetailApiView.as_view(), name='appointment_detail'),
    path('feedback/', FeedbackListApiView.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', FeedbackDetailApiView.as_view(), name='feedback_detail'),
    path('medical_record/', MedicalRecordListApiView.as_view(), name='medical-record_list'),
    path('medical_record/<int:pk>/', MedicalRecordDetailApiView.as_view(), name='medical-record_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]