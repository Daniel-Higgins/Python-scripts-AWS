import boto3

session = boto3.Session(profile_name='account')

# Create a VPC
def create_vpc(vpc_cidr_block):
    ec2 = session.client('ec2')
    response = ec2.create_vpc(
        CidrBlock=vpc_cidr_block,
        AmazonProvidedIpv6CidrBlock=False
    )
    vpc_id = response['Vpc']['VpcId']
    print(f"VPC created: {vpc_id}")
    return vpc_id

# Create subnets
def create_subnet(vpc_id, cidr_block, availability_zone):
    ec2 = session.client('ec2')
    response = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock=cidr_block,
        AvailabilityZone=availability_zone
    )
    subnet_id = response['Subnet']['SubnetId']
    print(f"Subnet created: {subnet_id}")
    return subnet_id

# Main
vpc_cidr_block = '10.0.0.0/16'
availability_zones = ['us-west-2a', 'us-west-2b', 'us-west-2c']
subnet_cidr_blocks = ['10.0.1.0/24', '10.0.2.0/24', '10.0.3.0/24']

vpc_id = create_vpc(vpc_cidr_block)

# Create subnets within the VPC
subnet_ids = []
for i in range(len(availability_zones)):
    subnet_id = create_subnet(vpc_id, subnet_cidr_blocks[i], availability_zones[i])
    subnet_ids.append(subnet_id)
	
