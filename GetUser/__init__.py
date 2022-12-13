import PureCloudPlatformClientV2
import os
import json
import azure.functions
from dotenv import dotenv_values

config = dotenv_values(".env")

def main(req: azure.functions.HttpRequest) -> azure.functions.HttpResponse: 
    # Parse the URL for the conversationId
    # conversation_id = req.params.get('conversationId')
    conversation_id = 'be9d3155-c3b6-4a6c-8ff1-5c48b4585135'
    
    # This sets the region for where you will be making the calls I.E. US-EAST-1
    region = PureCloudPlatformClientV2.PureCloudRegionHosts.us_west_2
    PureCloudPlatformClientV2.configuration.host = region.get_api_host()

    # Sets the client credentials
    apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(config['client'],
                                                                                              config['secret'])
    
    # Make the API call to get the conversation data
    calls_api = PureCloudPlatformClientV2.ConversationsApi(apiclient)
    calls_resp = calls_api.get_conversations_call(conversation_id=conversation_id)

    if calls_resp.participants[3].wrapup_required == True:
        # Parse the user from the ConversationCalls Object
        user = calls_resp.participants[3].user.id

        # Make the API call for getting a user
        users_api = PureCloudPlatformClientV2.UsersApi(apiclient)
        user_resp = users_api.get_user(user)

        # Create dictionary with the users name
        name = {'agent': user_resp.name}

        # Return the JSON
        return azure.functions.HttpResponse(
            json.dumps(name),
            mimetype="application/json",
        )
    elif calls_resp.participants[4].wrapup_required == True:
        # Parse the user from the ConversationCalls Object
        user = calls_resp.participants[4].user.id

        # Make the API call for getting a user
        users_api = PureCloudPlatformClientV2.UsersApi(apiclient)
        user_resp = users_api.get_user(user)

        # Create dictionary with the users name
        name = {'agent': user_resp.name}

        # Return the JSON
        return azure.functions.HttpResponse(
            json.dumps(name),
            mimetype="application/json",
        )
    elif calls_resp.participants[5].wrapup_required == True:
        # Parse the user from the ConversationCalls Object
        user = calls_resp.participants[5].user.id

        # Make the API call for getting a user
        users_api = PureCloudPlatformClientV2.UsersApi(apiclient)
        user_resp = users_api.get_user(user)

        # Create dictionary with the users name
        name = {'agent': user_resp.name}
        
        # Return the JSON
        return azure.functions.HttpResponse(
            json.dumps(name),
            mimetype="application/json",
        )
    else:
        # Parse the user from the ConversationCalls Object
        user = calls_resp.participants[6].user.id

        # Make the API call for getting a user
        users_api = PureCloudPlatformClientV2.UsersApi(apiclient)
        user_resp = users_api.get_user(user)

        # Create dictionary with the users name
        name = {'agent': user_resp.name}

        # Return the JSON
        return azure.functions.HttpResponse(
            json.dumps(name),
            mimetype="application/json",
        )
        
# {
#     "id": "be9d3155-c3b6-4a6c-8ff1-5c48b4585135",
#     "participants": [
#         {
#             "id": "25a4edc4-1e04-4565-b280-ad0c02b7682d",
#             "name": "Lawrenceburg IN",
#             "address": "tel:+18125841533",
#             "startTime": "2022-12-13T13:14:02.857Z",
#             "connectedTime": "2022-12-13T13:14:03.071Z",
#             "endTime": "2022-12-13T13:14:47.084Z",
#             "purpose": "customer",
#             "state": "terminated",
#             "direction": "inbound",
#             "disconnectType": "endpoint",
#             "held": false,
#             "wrapupRequired": false,
#             "queue": {
#                 "id": "67ce2258-ff62-4f8e-8467-2d79c9b98e2b",
#                 "selfUri": "/api/v2/routing/queues/67ce2258-ff62-4f8e-8467-2d79c9b98e2b"
#             },
#             "attributes": {},
#             "provider": "Edge",
#             "externalContact": {
#                 "id": "eb1f3a2e-3504-4f86-8c34-6a61b76fb2fa",
#                 "selfUri": "/api/v2/externalcontacts/contacts/eb1f3a2e-3504-4f86-8c34-6a61b76fb2fa"
#             },
#             "muted": false,
#             "confined": false,
#             "recording": false,
#             "recordingState": "none",
#             "ani": "tel:+18125841533",
#             "dnis": "tel:+13129718321"
#         },
#         {
#             "id": "dd86d2a2-44ea-44d9-87b9-7f9ceb72ec74",
#             "name": "Chicago IL",
#             "address": "sip:feca3d09-2e84-495c-be29-6a33285d455d@127.0.0.1;language=en-US;user=ivr",
#             "startTime": "2022-12-13T13:14:02.920Z",
#             "connectedTime": "2022-12-13T13:14:02.978Z",
#             "endTime": "2022-12-13T13:14:10.381Z",
#             "purpose": "ivr",
#             "state": "terminated",
#             "direction": "inbound",
#             "disconnectType": "transfer",
#             "held": false,
#             "wrapupRequired": false,
#             "attributes": {},
#             "provider": "Edge",
#             "peer": "bb481cce-5ed1-419b-a9f1-be5f1067a048",
#             "muted": false,
#             "confined": false,
#             "recording": false,
#             "recordingState": "none",
#             "ani": "tel:+18125841533",
#             "dnis": "sip:feca3d09-2e84-495c-be29-6a33285d455d@127.0.0.1;language=en-US;user=ivr"
#         },
#         {
#             "id": "c9495cab-c342-4493-9f5b-298ad56b984b",
#             "name": "Helpdesk",
#             "address": "sip:67ce2258-ff62-4f8e-8467-2d79c9b98e2b@127.0.0.1;language=en-US;user=acd",
#             "startTime": "2022-12-13T13:14:10.401Z",
#             "connectedTime": "2022-12-13T13:14:10.469Z",
#             "endTime": "2022-12-13T13:14:23.251Z",
#             "purpose": "acd",
#             "state": "terminated",
#             "direction": "inbound",
#             "disconnectType": "transfer",
#             "held": false,
#             "wrapupRequired": false,
#             "queue": {
#                 "id": "67ce2258-ff62-4f8e-8467-2d79c9b98e2b",
#                 "selfUri": "/api/v2/routing/queues/67ce2258-ff62-4f8e-8467-2d79c9b98e2b"
#             },
#             "attributes": {},
#             "provider": "Edge",
#             "peer": "bb481cce-5ed1-419b-a9f1-be5f1067a048",
#             "conversationRoutingData": {
#                 "queue": {
#                     "id": "67ce2258-ff62-4f8e-8467-2d79c9b98e2b",
#                     "selfUri": "/api/v2/routing/queues/67ce2258-ff62-4f8e-8467-2d79c9b98e2b"
#                 },
#                 "priority": 0,
#                 "skills": [],
#                 "scoredAgents": []
#             },
#             "muted": false,
#             "confined": false,
#             "recording": false,
#             "recordingState": "none",
#             "ani": "tel:+18125841533",
#             "dnis": "sip:67ce2258-ff62-4f8e-8467-2d79c9b98e2b@127.0.0.1;language=en-US;user=acd"
#         },
#         {
#             "id": "87c56eff-0d74-42d3-a169-2fd71a4993fe",
#             "address": "sip:5f2885408f05c815b2b570e8+nmoritzdev.orgspan.com;tgrp=04b04117-a70c-4a05-a1ce-54062c7f0176;trunk-context=nmoritzdev@localhost",
#             "startTime": "2022-12-13T13:14:10.715Z",
#             "endTime": "2022-12-13T13:14:12.806Z",
#             "purpose": "agent",
#             "state": "terminated",
#             "direction": "inbound",
#             "disconnectType": "client",
#             "held": false,
#             "wrapupRequired": false,
#             "wrapupPrompt": "timeout",
#             "user": {
#                 "id": "5f6fe78e-dfbb-400f-a70b-d9b5c8340fdc",
#                 "selfUri": "/api/v2/users/5f6fe78e-dfbb-400f-a70b-d9b5c8340fdc"
#             },
#             "queue": {
#                 "id": "67ce2258-ff62-4f8e-8467-2d79c9b98e2b",
#                 "selfUri": "/api/v2/routing/queues/67ce2258-ff62-4f8e-8467-2d79c9b98e2b"
#             },
#             "attributes": {},
#             "wrapupTimeoutMs": 120000,
#             "alertingTimeoutMs": 8000,
#             "provider": "Edge",
#             "peer": "bb481cce-5ed1-419b-a9f1-be5f1067a048",
#             "muted": false,
#             "confined": false,
#             "recording": false,
#             "recordingState": "none",
#             "ani": "sip:+18125841533@10.87.26.159;user=phone",
#             "dnis": "sip:5f2885408f05c815b2b570e8+nmoritzdev.orgspan.com;tgrp=04b04117-a70c-4a05-a1ce-54062c7f0176;trunk-context=nmoritzdev@localhost"
#         },
#         {
#             "id": "27f19593-96f2-4e4f-9262-ea839787cbc8",
#             "address": "sip:5f2885408f05c815b2b570e8+nmoritzdev.orgspan.com;tgrp=04b04117-a70c-4a05-a1ce-54062c7f0176;trunk-context=nmoritzdev@localhost",
#             "startTime": "2022-12-13T13:14:16.570Z",
#             "endTime": "2022-12-13T13:14:19.062Z",
#             "purpose": "agent",
#             "state": "terminated",
#             "direction": "inbound",
#             "disconnectType": "client",
#             "held": false,
#             "wrapupRequired": false,
#             "wrapupPrompt": "timeout",
#             "user": {
#                 "id": "5f6fe78e-dfbb-400f-a70b-d9b5c8340fdc",
#                 "selfUri": "/api/v2/users/5f6fe78e-dfbb-400f-a70b-d9b5c8340fdc"
#             },
#             "queue": {
#                 "id": "67ce2258-ff62-4f8e-8467-2d79c9b98e2b",
#                 "selfUri": "/api/v2/routing/queues/67ce2258-ff62-4f8e-8467-2d79c9b98e2b"
#             },
#             "attributes": {},
#             "wrapupTimeoutMs": 120000,
#             "alertingTimeoutMs": 8000,
#             "provider": "Edge",
#             "peer": "bb481cce-5ed1-419b-a9f1-be5f1067a048",
#             "muted": false,
#             "confined": false,
#             "recording": false,
#             "recordingState": "none",
#             "ani": "sip:+18125841533@10.87.26.159;user=phone",
#             "dnis": "sip:5f2885408f05c815b2b570e8+nmoritzdev.orgspan.com;tgrp=04b04117-a70c-4a05-a1ce-54062c7f0176;trunk-context=nmoritzdev@localhost"
#         },
#         {
#             "id": "c3e76598-fb3c-40d4-997a-005541e34556",
#             "address": "sip:5f2885408f05c815b2b570e8+nmoritzdev.orgspan.com;tgrp=04b04117-a70c-4a05-a1ce-54062c7f0176;trunk-context=nmoritzdev@localhost",
#             "startTime": "2022-12-13T13:14:21.083Z",
#             "connectedTime": "2022-12-13T13:14:23.200Z",
#             "endTime": "2022-12-13T13:14:47.101Z",
#             "purpose": "agent",
#             "state": "terminated",
#             "direction": "inbound",
#             "disconnectType": "peer",
#             "held": false,
#             "wrapupRequired": true,
#             "wrapupPrompt": "timeout",
#             "user": {
#                 "id": "5f6fe78e-dfbb-400f-a70b-d9b5c8340fdc",
#                 "selfUri": "/api/v2/users/5f6fe78e-dfbb-400f-a70b-d9b5c8340fdc"
#             },
#             "queue": {
#                 "id": "67ce2258-ff62-4f8e-8467-2d79c9b98e2b",
#                 "selfUri": "/api/v2/routing/queues/67ce2258-ff62-4f8e-8467-2d79c9b98e2b"
#             },
#             "attributes": {},
#             "errorInfo": {
#                 "message": "session 55665ecd-3803-4675-a880-f6dfc9c3074c is inactive for command cloud.command.disconnect",
#                 "code": "error.ininedgecontrol.session.inactive",
#                 "messageWithParams": "session {sessionId} is inactive for command {type}",
#                 "messageParams": {
#                     "sessionId": "55665ecd-3803-4675-a880-f6dfc9c3074c",
#                     "type": "cloud.command.disconnect"
#                 },
#                 "details": [],
#                 "errors": []
#             },
#             "wrapupTimeoutMs": 120000,
#             "alertingTimeoutMs": 8000,
#             "provider": "Edge",
#             "wrapup": {
#                 "code": "560d87d0-ed4c-4662-903d-dce00bfae927",
#                 "notes": "",
#                 "tags": [],
#                 "durationSeconds": 14,
#                 "endTime": "2022-12-13T13:15:01.321Z"
#             },
#             "peer": "bb481cce-5ed1-419b-a9f1-be5f1067a048",
#             "startAcwTime": "2022-12-13T13:14:47.101Z",
#             "endAcwTime": "2022-12-13T13:15:01.321Z",
#             "muted": false,
#             "confined": false,
#             "recording": false,
#             "recordingState": "none",
#             "ani": "sip:+18125841533@10.87.26.159;user=phone",
#             "dnis": "sip:5f2885408f05c815b2b570e8+nmoritzdev.orgspan.com;tgrp=04b04117-a70c-4a05-a1ce-54062c7f0176;trunk-context=nmoritzdev@localhost"
#         }
#     ],
#     "otherMediaUris": [],
#     "recordingState": "none",
#     "selfUri": "/api/v2/conversations/calls/be9d3155-c3b6-4a6c-8ff1-5c48b4585135"
# }