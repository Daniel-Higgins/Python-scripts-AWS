#/usr/local/bin/python3
from aws_conf import *

import datetime, boto3, csv, json

session = boto3.Session(profile_name='account-name')
IAM = session.client('iam')

acc = {
        'account-name' : 'account-id'
        }

policyList=[]
paginator = IAM.get_paginator('list_policies')
for response in paginator.paginate(Scope="Local"):
        for policy in response["Policies"]:
            if policy['PolicyName'].endswith(".json"):
                policyList.append(policy)
                #print(f"Policy Name: {policy['PolicyName']} ARN: {policy['Arn']}")
#roles
def pDeetsR(arn):
    iam = session.resource('iam')
    policy = iam.Policy(arn)
    x = policy.attached_roles.all()
    return x

#groups
def pDeetsG(arn):
    iam = session.resource('iam')
    policy = iam.Policy(arn)
    x = policy.attached_groups.all()
    return x

def getPolBody(arn):
    policy = IAM.get_policy(PolicyArn=arn)
    policy_version = IAM.get_policy_version(
        PolicyArn = arn,
        VersionId = policy['Policy']['DefaultVersionId']
    )
    body = json.dumps(policy_version['PolicyVersion']['Document'])
    return body

def create_iam_policy(po):

    new_policy = getPolBody(po['Arn'])
    response = IAM.create_policy(
        PolicyName=po['PolicyName'].strip(".json"),
        PolicyDocument=json.dumps(new_policy)
    )
    newPolicyNames.append(po['PolicyName'].strip(".json"))
    print(response)


#main
for p in policyList:
    create_iam_policy(p)
    roles_attached = pDeetsR(p['Arn'])

    for r in roles_attached:
        IAM.detach_role_policy(PolicyArn=p['Arn'],RoleName=r.name)
        IAM.attach_role_policy(PolicyArn=f"arn:aws:iam::{acc['account-name']}:policy/"+p['PolicyName'].strip(".json"),RoleName=r.name)
        #detaches corrupt policy and attaches correct policy to role


#--copy current policy body
#--detatch current policy from role
#attach new copied policy to role
