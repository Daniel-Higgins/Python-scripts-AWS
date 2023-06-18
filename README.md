# Python-scripts-AWS
here are a few Python scripts that can help you manage your AWS resources.


IAM_policy-cleanup - this script cleans up any misspelled policy names, in this example anything that ends in .json, and removes them. Then the script creates a new policy with the same permission but correctly spells the policy and then attaches it to the role/group.

create s3 - that python script creates a simple private s3 bucket to any region of your choice

vpc-subnet creation - creates vpc and subnets of your choosing in a specific account

sns-sqs - this creates a simple SNS and SQS queue


launch-rds - this script takes a snapshot of an RDS and launches a new RDS based off of the snapshot taken
