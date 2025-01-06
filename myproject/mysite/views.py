from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .filter import DoctorFilter
from .serializer import *
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import *
from .permission import IsAdmin, IsDoctor, IsPatient, IsOwnerOrAdmin


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(TokenObtainPairView):
    serializer_class =LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status = status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs ):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class DoctorListApiView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer


class DoctorDetailApiView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_class = DoctorFilter
    search_fields = ['speciality']
    ordering_fields = ['working_days']
    pagination_class = DoctorPagination
    permission_classes = [IsDoctor]

    def get_queryset(self):
        queryset = Doctor.objects.all()
        return queryset


class PatientProfileViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer


class AppointmentListApiView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer


class AppointmentDetailApiView(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentDetailSerializer
    permission_classes = [IsPatient]


    def get_queryset(self):
        queryset = Appointment.objects.all()
        doctor = self.request.query_params.get('doctor', None)
        if doctor:
            queryset = queryset.filter(doctor__id=doctor)
        return queryset


class MedicalRecordListApiView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordListSerializer


class MedicalRecordDetailApiView(generics.RetrieveAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordDetailSerializer
    permission_classes = [IsDoctor]


class PrescriptionsViewSet(viewsets.ModelViewSet):
    queryset = Prescriptions.objects.all()
    serializer_class = PrescriptionsSerializer


class BillingsViewSet(viewsets.ModelViewSet):
    queryset = Billings.objects.all()
    serializer_class = BillingsSerializer


class WardsViewSet(viewsets.ModelViewSet):
    queryset = Wards.objects.all()
    serializer_class = WardsSerializer


class FeedbackListApiView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer


class FeedbackDetailApiView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer
    permission_classes = [IsOwnerOrAdmin]
