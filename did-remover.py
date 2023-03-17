from json import load
from dotenv import dotenv_values
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint
import time
import math
import os

config = dotenv_values(".env")

def main():
    print("SCIM User Phone Number Removal Start")

    PureCloudPlatformClientV2.configuration.logger.log_level = PureCloudPlatformClientV2.logger.LogLevel.LDebug
    PureCloudPlatformClientV2.configuration.logger.log_request_body = True
    PureCloudPlatformClientV2.configuration.logger.log_response_body = True
    PureCloudPlatformClientV2.configuration.logger.log_format = PureCloudPlatformClientV2.logger.LogFormat.JSON
    PureCloudPlatformClientV2.configuration.logger.log_to_console = False
    PureCloudPlatformClientV2.configuration.logger.log_file_path = "pythonsdk.log"

    ids = []
    userlist = []
    
    id_of_user = ""

    total_returned = 1
    
    division = config['division']
    presence = config['presence']
    state = config['state']
        
    # This sets the region for where you will be making the calls I.E. US-EAST-1
    region = PureCloudPlatformClientV2.PureCloudRegionHosts.eu_central_1
    PureCloudPlatformClientV2.configuration.host = region.get_api_host()

    PureCloudPlatformClientV2.configuration.access_token = config['token'] # This is the bearer token generated from Postman
    
    scim_api_instance = PureCloudPlatformClientV2.SCIMApi()
    users_api_instance = PureCloudPlatformClientV2.UsersApi()
    
    print("Gathering Division Users....")
    try:
        query = QueryUsers(users_api_instance,1,sort_order="ASC")
        totalpages = query[0]
        if totalpages == 0: 
            print("Exiting, adjust query page size")
            return;

        # requiredruns = math.ceil( totalpages / 100)
        i = 1

        while True:
            if total_returned < math.ceil(100001 / 100):
                api_response = query[1]
                # json_response = json.loads(api_response)
            
                for item in api_response.entities:
                    # print("DIVISION: {}".format(item.division.name))
                    for number in item.primary_contact_info:
                        if number.address is not None and "+" in number.address:
                            # print("PHONE NUMBER: {}".format(number.address))
                            if item.division.name == division:
                                if item.id not in ids:
                                    ids.append(item.id)
                    if item.id not in userlist:
                        userlist.append(item.id)
                    
                

                
                i = i + 1
                time.sleep(0.320)

                query = QueryUsers(users_api_instance,i,sort_order="ASC")

            elif total_returned > math.ceil(100001 / 100) and total_returned < math.ceil(250001 / 100):
                api_response = query[1]
                # json_response = json.loads(api_response)
            
                for item in api_response.entities:
                    # print("DIVISION: {}".format(item.division.name))
                    for number in item.primary_contact_info:
                        if number.address is not None and "+" in number.address:
                            # print("PHONE NUMBER: {}".format(number.address))
                            if item.division.name == division:
                                if item.id not in ids:
                                    ids.append(item.id)
                    if item.id not in userlist:
                        userlist.append(item.id)
                    
                

                
                i = i + 1
                time.sleep(0.320)
                
                query = QueryUsers(users_api_instance,i,sort_order="DESC")
            elif total_returned > math.ceil(250001 / 100):
                break

            total_returned += 1
            
            print(total_returned)
        
        print("Total users in list ", len(userlist))

        print("Total users to be processed ", len(ids))

        number_of_items = 0
        
        for user_id in ids:
            
            if number_of_items > config['stopafter']:
                print("Stop After Threshold reached")
                break
           
            body = PureCloudPlatformClientV2.ScimV2PatchRequest() # ScimV2PatchRequest | The information used to modify a user.
        
            body.operations = [
                {
                    "op": "remove",
                    "path": "phoneNumbers"
                }
            ]

            try:
                # Modify a user
                patch_response = scim_api_instance.patch_scim_v2_user(user_id, body)
                
                time.sleep(0.320)

                number_of_items += 1
                print("Processed count is: {}".format(number_of_items))
            except ApiException as e:
                print("Exception when calling SCIMApi->patch_scim_v2_user: %s\n" % e)
       
    except ApiException as e:
        print("Exception when calling SCIMApi->get_scim_user: %s\n" % e)
        
 
def QueryUsers(api_instance, page, sort_order):
    start_index = page
    page_size = 100
    integration_presence_source = presence
    state = state

    try:
        # Get a User
        api_response = api_instance.get_users(page_size=page_size, page_number=page, sort_order=sort_order, integration_presence_source=integration_presence_source, state=state)
        total_results = api_response.total
        print("QueryUsers Page %s Users %s" % (page,api_response.page_size))
        return total_results, api_response
    except ApiException as e:
                print("Exception when calling UsersApi->get_users_call: %s\n" % e)
                return 0,0
 

main()


