import boto3
import time

session = boto3.Session(profile_name='account')

client = session.client('workspaces',region_name='eu-central-1')

paginator = client.get_paginator('describe_workspaces')

x = paginator.paginate(DirectoryId='d-awsdirectory')

for page in x:
    for i in page['Workspaces']:
        try:
            response = client.describe_workspaces_connection_status(WorkspaceIds=[i['WorkspaceId']])

            if response['WorkspacesConnectionStatus'][0]['ConnectionState'] == 'CONNECTED':
                print("User is CONNECTED ### " + i['UserName'])
                continue
                
            elif i['State'] == 'STOPPED':
                    #Start
                    client.start_workspaces(
                        StartWorkspaceRequests=[
                        {
                             'WorkspaceId': i['WorkspaceId'],
                        },
                    ])
            else:
                continue
        except:
            print("Error for user -->- " + i['UserName'])

print("done")
