import json
from urllib.parse import parse_qs
from django.db.models import Max

from dateutil.parser import parse
from datetime import datetime, timezone
from rest_framework.authtoken.models import Token

post_endpoint_message = 'This is a POST API End Point'

def get_date():
	# Get current date and time
	now = datetime.now()

	# Format date and time as YYYY-MM-DD
	date = now.strftime("%Y-%m-%d")

	return date


def get_date_time():
	# Get current date and time
	now = datetime.now()

	# Format date and time as YYYY-MM-DD HH:MM:SS
	dateTime = now.strftime("%Y-%m-%d %H:%M:%S")

	return dateTime


# Get Auth User Id
def getAuthId(authToken):
	try:
		token_q = Token.objects.get(key=authToken)
		return token_q.user_id
	except Token.DoesNotExist:
		return "0"

# Generate Next Id for the Model
def next_id(Model):
	no = Model.objects.all().aggregate(Max('id'))

	max_id = no['id__max']

	if max_id == None:
		return 1
	else:
		return int(max_id) + 1


# Parse Data for Other Methods from Front End Pals
def parse_data(request):
	body_data = {}

	try:
		body_data = json.loads(request.body.decode('utf-8'))
	except Exception:
    	# RawPostDataException
		body_data = json.loads(json.dumps(request.data))
	
	if len(body_data) < 1:
		body_data_a = parse_qs(request.get_full_path().split('?')[1])
		body_data_dict = json.dumps(dict(body_data_a)) 
		body_data = json.loads(body_data_dict)
		
	return body_data