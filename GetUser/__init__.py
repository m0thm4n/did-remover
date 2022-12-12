import PureCloudPlatformClientV2
import os
import json
import azure.functions

def main(req: azure.functions.HttpRequest) -> azure.functions.HttpResponse:
    # Parse the URL for the conversationId
    conversation_id = req.params.get('conversationId')
    
    # This sets the region for where you will be making the calls I.E. US-EAST-1
    region = PureCloudPlatformClientV2.PureCloudRegionHosts.us_west_2
    PureCloudPlatformClientV2.configuration.host = region.get_api_host()

    # Sets the client credentials
    apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token('5c31273d-51dc-415c-b01e-83705b245b06',
                                                                                          'zqClcf3gnStwNNX7C9kHe34UVonG_lKKNKgyGtbJkc4')
    
    # Make the API call to get the conversation data
    calls_api = PureCloudPlatformClientV2.ConversationsApi(apiclient)
    calls_resp = calls_api.get_conversations_call(conversation_id=conversation_id)

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