from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('speciality', 'qualifications')


@register(Appointment)
class AppointmentTranslationOptions(TranslationOptions):
    fields = ('notes',)


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment',)


@register(MedicalRecord)
class MedicalRecordTranslationOptions(TranslationOptions):
    fields = ('diagnosis', 'treatment', 'prescribed_medication')


@register(PatientProfile)
class MedicalRecordTranslationOptions(TranslationOptions):
    fields = ('blood_type', 'allergies', 'medical_history')


@register(Billings)
class BillingsTranslationOptions(TranslationOptions):
    pass


@register(Wards)
class WardsTranslationOptions(TranslationOptions):
    pass


@register(Prescriptions)
class PrescriptionsTranslationOptions(TranslationOptions):
    fields = ('medication', 'dosage')
