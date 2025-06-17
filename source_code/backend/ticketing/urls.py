from ticketing import views

from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ticketing.controllers import ticket_controller
from ticketing.controllers import ticket_actions_controller

urlpatterns = [
  
    # Call Ticket by Speaker
    path('call/ticket/speaker', ticket_actions_controller.call_ticket_speaker, name='call-ticket-speaker'),

    # Call Ticket by Smart TV
    path('call/ticket/smart/tv', ticket_actions_controller.call_ticket_smarttv, name='call-ticket-smarttv'),

    # Create New Ticket
    path('ticket/create', ticket_controller.create_ticket, name='create-ticket'),

    # Read Ticket by Checkin ID
    path('ticket/read/by/checkin_id/<str:checkin_id>', ticket_controller.read_ticket_by_checkin_id, name='read-ticket-by-checkinid'),

    # Read Ticket with Id
    path('ticket/read/<str:ticket_id>', ticket_controller.read_ticket, name='read-ticket'),

    # Read All Tickets
    path('ticket/read_all/tickets', ticket_controller.read_all_tickets, name='read-all-ticket'),

    # Update Ticket with Id
    path('ticket/update/<str:ticket_id>', ticket_controller.update_ticket, name='update-ticket'),

    # Delete Ticket
    path('ticket/delete/<str:ticket_id>', ticket_controller.delete_ticket, name='delete-ticket'),

] 