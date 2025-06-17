import json
import random
from datetime import date
from drf_yasg import openapi
from django.http import JsonResponse

from django.db.models import Q

import datetime
from ticketing import toolsa
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from ticketing.models import PatientTicket
from ticketing.models import PatientTicketInference

from ticketing.serializers import PatientTicketSerializer
from ticketing.serializers import PatientTicketInferenceSerializer

@api_view(['POST'])
def delete_ticket(request, ticket_id):
    """
    Delete Ticket by using Ticket Id
    """
    try:
        delete_ticket = PatientTicket.objects.get(id=ticket_id)
        delete_ticket.delete()

        return JsonResponse({
            'status': True,
            'deleted_ticket': str(ticket_id)
        })
    except PatientTicket.DoesNotExist:
        return JsonResponse({
            'status': False,
            'message': 'Patient Ticket Does Not Exist'
        })

@api_view(['POST'])
def update_ticket(request, ticket_id):
    """
    Update Ticket by Using Ticket Id
    """
    patient_id = request.POST.get('patient_id')
    checkin_id = request.POST.get('checkin_id')
    expire_status = request.POST.get('expire_status')

 	# Get Params in json
    if patient_id == None:
        data = toolsa.parse_data(request)
        patient_id = data['patient_id']
        checkin_id = data['checkin_id']
        expire_status = data['expire_status']

    try:
        # Update Ticket to Database
        update_ticket = PatientTicket.objects.get(id=ticket_id)
        update_ticket.patient_id = patient_id
        update_ticket.checkin_id = checkin_id
        update_ticket.expire_status = expire_status
        update_ticket.save()

        # Serialize Data
        update_ticket_sr = PatientTicketSerializer(update_ticket).data

        return JsonResponse({
            'status': True,
            'data': update_ticket_sr
        })
    except PatientTicket.DoesNotExist:
        return JsonResponse({
            'status': False,
            'message': 'Patient Ticket Does Not Exist',
            'data': []
        })        

@api_view(['GET'])
def read_all_tickets(request):
    """
    Read All Tickets in the System - Paginated
    """
    ticketsDataQ = PatientTicket.objects.all().order_by("-created_at")
    ticketsData = PatientTicketSerializer(ticketsDataQ, many=True).data
	
    return JsonResponse({
		'tickets_data': ticketsData,
		'status': True
		})

@api_view(['GET'])
def read_ticket_by_checkin_id(request, checkin_id):
    """
    Read Ticket by Checkin ID
    """
    try:
        ticket_data_q = PatientTicket.objects.get(checkin_id=int(checkin_id))
        ticket_data = PatientTicketSerializer(ticket_data_q).data

        return JsonResponse({
			'ticket_data': ticket_data,
			'status': True
			})
    except PatientTicket.DoesNotExist:
        return JsonResponse({
			'ticket_data': [],
			'message': 'Does Not Exist Exception',
			'status': True
			})


@api_view(['GET'])
def read_ticket(request, ticket_id):
    """
    Read Ticket by Ticket Id
    """
    try:
        ticket_data_q = PatientTicket.objects.get(id=ticket_id)
        ticket_data = PatientTicketSerializer(ticket_data_q).data

        return JsonResponse({
			'ticket_data': ticket_data,
			'status': True
			})
    except PatientTicket.DoesNotExist:
        return JsonResponse({
			'ticket_data': [],
			'message': 'Does Not Exist Exception',
			'status': True
			})


@api_view(['POST'])
def create_ticket(request):
    """
    Generate Ticket From Reception Point Usually
    for user to Use in his/her movements
    """
    patient_id = request.POST.get('patient_id')
    checkin_id = request.POST.get('checkin_id')

 	# Get Params in json
    if patient_id == None:
        data = toolsa.parse_data(request)
        patient_id = data['patient_id']
        checkin_id = data['checkin_id']

    # Check if Ticket for this (patient and checkin) exists
    ticket_check = PatientTicket.objects.filter(patient_id=patient_id).filter(checkin_id=checkin_id)

    ticket_id = ""
    ticket_code = ""

    if len(ticket_check) == 0:
        # Generate a random letter from A to Z.
        letter = random.choice('ABC')
        # letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        while True:
            # Generate a random number from 001 to 999.
            number = random.randint(1, 999)

            # Format the ticket ID as N-XXX.
            ticket_code = f'{letter}{number:03d}'

            # Check if Ticket is Used
            ticket_use_statusQ = PatientTicket.objects.filter(ticket_code=ticket_code).filter(expire_status=1)
            ticket_use_status = PatientTicketSerializer(ticket_use_statusQ, many=True).data

            # Check if the ticket ID is unique.
            if len(ticket_use_status) == 0:
                break

        ticket_id = toolsa.next_id(PatientTicket)

        # Add Ticket to Database
        new_ticket = PatientTicket()
        new_ticket.id = ticket_id
        new_ticket.patient_id = patient_id
        new_ticket.checkin_id = checkin_id
        new_ticket.ticket_code = ticket_code
        new_ticket.expire_status = 0
        new_ticket.save()

        # Return Response
        return JsonResponse({
            'id': str(ticket_id),
            'status': True,
            'ticket_code': str(ticket_code),
            'patient_id': str(patient_id),
            'checkin_id': str(checkin_id) 
        })

    else:
        # Get Existing Ticket Code
        ticket_data = PatientTicketSerializer(ticket_check[0]).data

        ticket_id = ticket_data['id']
        ticket_code = ticket_data['ticket_code']

        return JsonResponse({
            'id': str(ticket_id),
            'status': True,
            'ticket_code': str(ticket_code),
            'patient_id': str(patient_id),
            'checkin_id': str(checkin_id) 
        })
    
