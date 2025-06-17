import os, sys, json
from datetime import date
from drf_yasg import openapi
from django.http import JsonResponse

from django.db.models import Q
from django.conf import settings

import moviepy.editor as mpe

import datetime
from ticketing import toolsa
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from ticketing.models import PatientTicket
from ticketing.models import PatientTicketInference

from ticketing.serializers import PatientTicketSerializer
from ticketing.serializers import PatientTicketInferenceSerializer

from backend.settings import main_ticketing_site_url

@api_view(['POST'])
def call_ticket_smarttv(request):
    """
    Call Ticket by Smart TV
    """
    return JsonResponse({
        'status': True
    })

@api_view(['POST'])
def call_ticket_speaker(request):
    """
    Call Ticket by Speaker
    """
    to_location = request.POST.get('to_location')
    patient_id = request.POST.get('patient_id')
    checkin_id = request.POST.get('checkin_id')

 	# Get Params in json
    if patient_id == None:
        data = toolsa.parse_data(request)
        to_location = data['to_location']
        patient_id = data['patient_id']
        checkin_id = data['checkin_id']
    
    # Get Ticket Data
    ticket_id = ticket_code = ""
    ticket_dataQ = PatientTicket.objects.filter(patient_id=patient_id).filter(checkin_id=checkin_id)
    ticket_data = PatientTicketSerializer(ticket_dataQ, many=True).data

    if len(ticket_data) != 0:
        ticket_id = ticket_data[0]['id']
        ticket_code = ticket_data[0]['ticket_code']

    ticket_inference_checkQ = []
    # Check if Ticket Already Audio Inferenced
    had_check_exception = False 
    try:
        had_check_exception = True
        ticket_inference_checkQ = PatientTicketInference.objects.filter(ticket_code=ticket_code).filter(to_location=to_location)
    except PatientTicketInference.DoesNotExist:
        pass

    # Make Generated Ticket Folder
    ticket_folder = os.path.join(settings.MEDIA_ROOT, "generated/" + str(ticket_id))
    
    print(len(ticket_inference_checkQ))

    if (len(ticket_inference_checkQ) == 0) and (had_check_exception != False):
        # Create Inference Ticket Id
        ticket_inference_id = toolsa.next_id(PatientTicketInference)

        # Create New Inference for Speaker
        new_ticket_inference = PatientTicketInference()
        new_ticket_inference.id = ticket_inference_id
        new_ticket_inference.ticket_code = ticket_code
        new_ticket_inference.inference_type = "SPEAKER_AUDIO"
        new_ticket_inference.to_location = to_location
        new_ticket_inference.save()

        # Chunks Resource Folder
        media_root_dir = os.path.join(settings.MEDIA_ROOT, "rehema")

        # Get Each Character for Ticket Code
        ticket_code_r = list(ticket_code)

        to_generate_chunk_list = []

        # Add Tiketi Nambari Chunk
        tiketi_nambari_chunk = os.path.join(media_root_dir, "tiketi_nambari.mp3")
        to_generate_chunk_list.append(mpe.AudioFileClip(tiketi_nambari_chunk))

        for t_code in ticket_code_r:
            t_code_chunk = os.path.join(media_root_dir, str(t_code) + ".mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(t_code_chunk))

        # Add Elekea Chunk
        elekea_chunk = os.path.join(media_root_dir, "elekea.mp3")
        to_generate_chunk_list.append(mpe.AudioFileClip(elekea_chunk))

        # CASHIER, VITAL SIGNS, DOCTOR, LABORATORY, RADIOLOGY, PHARMACY

        if to_location == "VITAL_SIGNS":
            # Add Ofisi Nambari Chunk
            ofisi_nambari_chunk = os.path.join(media_root_dir, "ofisi_nambari.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(ofisi_nambari_chunk)) 

            # Namba 1 Chunk
            namba_moja_chunk = os.path.join(media_root_dir, "1.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(namba_moja_chunk))

        elif to_location == "LABORATORY":
            # Add Maabara Chunk
            maabara_chunk = os.path.join(media_root_dir, "maabara.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(maabara_chunk)) 

        elif to_location == "RADIOLOGY":
            # Add Radiology Chunk
            maabara_chunk = os.path.join(media_root_dir, "radioloji.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(maabara_chunk)) 

        elif to_location == "CASHIER":
            # Add Dirisha Nambari Chunk
            dirisha_nambari_chunk = os.path.join(media_root_dir, "dirisha_nambari.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(dirisha_nambari_chunk)) 

            # Namba Moja Chunk
            namba_moja_chunk = os.path.join(media_root_dir, "1.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(namba_moja_chunk))

        elif to_location == "PHARMACY":
            # Add Dirisha Nambari Chunk
            dirisha_nambari_chunk = os.path.join(media_root_dir, "dirisha_nambari.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(dirisha_nambari_chunk)) 

            # Namba 2 Chunk
            namba_mbili_chunk = os.path.join(media_root_dir, "2.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(namba_mbili_chunk))

        elif to_location == "DOCTOR":
            # Add Daktari Chumba Namba Chunk
            daktari_chumba_namba_chunk = os.path.join(media_root_dir, "daktari_chumba_namba.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(daktari_chumba_namba_chunk)) 

            # Namba 5 Chunk
            namba_tano_chunk = os.path.join(media_root_dir, "5.mp3")
            to_generate_chunk_list.append(mpe.AudioFileClip(namba_tano_chunk))
        
        # Create Folder if Does Not Exist
        if not os.path.isdir(ticket_folder):
            os.system("mkdir " + ticket_folder)

        # Area to Store Audio File
        aud_ticket_loc = os.path.join(ticket_folder, str(ticket_inference_id) + ".mp3")

        # Join Audio Clips
        audio_file = mpe.concatenate_audioclips(to_generate_chunk_list)
        audio_file.write_audiofile(aud_ticket_loc)

        return JsonResponse({
            'id': str(ticket_inference_id),
            'status': True,
            'ticket_code': str(ticket_code),
            'patient_id': str(patient_id),
            'audio_file': main_ticketing_site_url + "/media/generated/"+str(ticket_id)+"/"+str(ticket_inference_id)+".mp3",
            'generate_status': "NEW_GEN",
        })
    
    else:
        ticket_inference_data = PatientTicketInferenceSerializer(ticket_inference_checkQ, many=True).data
        ticket_inference_id = ticket_inference_data[0]['id']

        # already_generated_audio = 
        return JsonResponse({
            'id': str(ticket_inference_id),
            'status': True,
            'ticket_code': str(ticket_code),
            'audio_file':  main_ticketing_site_url + "/media/generated/"+str(ticket_id)+"/"+str(ticket_inference_id)+".mp3",
            'generate_status': "EXIST_GEN",
        })