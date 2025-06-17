from django.db import models

# Patient Ticket Model
class PatientTicket(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    creator_id = models.IntegerField(blank=True)
    patient_id = models.IntegerField(blank=True)
    checkin_id = models.IntegerField(blank=True)
    ticket_code = models.CharField(max_length=200, blank=True) 
    expire_status = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'patient_ticket'


# Patient Ticket Inference Model
class PatientTicketInference(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    ticket_code = models.CharField(max_length=200, blank=True)
    # SPEAKER_AUDIO, TV_VISION, PHONE_SMS
    inference_type = models.CharField(max_length=200, blank=True) 
    to_location = models.CharField(max_length=200, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'patient_ticket_inference'