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