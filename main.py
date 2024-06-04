#!/usr/bin/python3
from sys import argv, exit
from requests import post
from re import findall, MULTILINE
import json
import logging
import time
import random

# Logging configuration
log_format = '%(asctime)s - %(funcName)s - [%(levelname)s] - %(message)s'
logging.basicConfig(format='{}'.format(log_format), datefmt='%m/%d/%Y %H:%M:%S')
log_level = logging.INFO
## Main logger
logger = logging.getLogger(name='aranda_connector')
logger.setLevel(log_level)

if len(argv) < 3:
    logger.error('Missing parameters. Should at least provide <SUBJECT> & <MESSAGE>')
    exit(1)

# Aranda connection values
#aranda_uri = 'https://qaitsm.sonda.com/asmsapi'
aranda_uri = 'ARANDA URL'
aranda_user = 'USER'
aranda_pass = 'PASSWORD'

# Request values
author_id = ""
category_id = ""
#company_id = ""
company_id = ""
contract_id = ""
#customer_id = ""
customer_id = ""
#group_id = ""
group_id = ""
impact_id = ""
instance = ""
model_id = ""
project_id = ""
reason_id = ""
service_id = ""
state_id = ""

# Event values
zabbix_subject = argv[1]
logger.debug('Event subject: {}'.format(zabbix_subject))
zabbix_message = argv[2]
logger.debug('Event Message: {}'.format(zabbix_message))

# API REST BODYs
auth_request = {
    'consoleType': 1,
    'password': aranda_pass,
    'providerId': 0,
    'userName': aranda_user
}
aranda_contents = {
    'authorId': author_id,
    'categoryId': category_id,
    'companyId': company_id,
    'consoleType': 'specialist',
    'contractId': contract_id,
    'currentTime': 0,
    'customerId': customer_id,
    'description': zabbix_message,
    'estimatedCost': 0,
    'estimatedTime': 0,
    'foregroundColorRgb': '',
    'groupId': group_id,
    'hasMoreInformation': False,
    'hasPendingSurvey': False,
    'impactId': impact_id,
    'instance': instance,
    'isFeeAvailable': True,
    'itemType': 1,
    'itemVersion': 0,
    'listAdditionalField': [],
    'modelId': model_id,
    'priorityReason': '',
    'projectId': project_id,
    'realCost': 0,
    'reasonId': reason_id,
    'registryTypeId': 30,
    'serviceId': service_id,
    'stateId': state_id,
    'subject': zabbix_subject,
    'surveyToken': '',
    'tempItemId': -1,
    'transformed': False
}

# Execution flow begins here...
auth_token = post('{}/api/v9/authentication/'.format(aranda_uri), json=auth_request).json()['token']
logger.debug('Token obtained: {}'.format(auth_token))
# Header used during ticket generation...
create_ticket_header = {
    'Content-Type': 'application/json',
    'X-Authorization': 'Bearer ' + auth_token
}
logger.debug('Bearer token: {}'.format(create_ticket_header['X-Authorization']))
created_ticket_id = post('{}/api/v9/item/'.format(aranda_uri), data=json.dumps(aranda_contents), headers=create_ticket_header).json()['idByProject']
logger.info('Ticket created. ID: {}'.format(created_ticket_id))

def update_ticket_status(ticket_id, new_state_id):
    update_contents = {
        'stateId': new_state_id
    }
    response = post('{}/api/v9/item/{}/state'.format(aranda_uri, ticket_id), data=json.dumps(update_contents), headers=create_ticket_header)
    if response.status_code == 200:
        logger.info('Ticket ID {} status updated to In Progress'.format(ticket_id))
    else:
        logger.error('Failed to update ticket ID {} status. Response: {}'.format(ticket_id, response.text))

# Wait for a random interval between 4 and 8 minutes
wait_time = random.randint(4, 8) * 60
logger.info('Waiting for {} seconds before updating ticket status.'.format(wait_time))
time.sleep(wait_time)

# Update the ticket status to 'In Progress'
new_state_id = 6341  # Assuming 6337 is the state ID for 'In Progress'
update_ticket_status(created_ticket_id, new_state_id)

# Logout
post('{}/api/v9/authentication/logout'.format(aranda_uri), headers={'X-Authorization': 'Bearer ' + auth_token})
