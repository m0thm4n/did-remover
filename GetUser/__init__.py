import PureCloudPlatformClientV2
import os
import json
import azure.functions

# (req: azure.functions.HttpRequest) -> str
def main(req: azure.functions.HttpRequest) -> azure.functions.HttpResponse:
    conversation_id = 'd6d3b70f-0787-49ac-9b48-23703fdbde9a'
    # conversation_id = req.params.get('conversationId')
    
    region = PureCloudPlatformClientV2.PureCloudRegionHosts.us_west_2
    PureCloudPlatformClientV2.configuration.host = region.get_api_host()

    apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token('5c31273d-51dc-415c-b01e-83705b245b06',
                                                                                          'zqClcf3gnStwNNX7C9kHe34UVonG_lKKNKgyGtbJkc4')
    
    calls_api = PureCloudPlatformClientV2.ConversationsApi(apiclient)
    calls_resp = calls_api.get_conversations_call(conversation_id=conversation_id)

    user = calls_resp.participants[3].user.id

    users_api = PureCloudPlatformClientV2.UsersApi(apiclient)

    user_resp = users_api.get_user(user)

    name = {'agent': user_resp.name}

    return azure.functions.HttpResponse(
        json.dumps(name),
        mimetype="application/json",
    )