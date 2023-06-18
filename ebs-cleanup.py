import boto3

session = boto3.Session(profile_name='sme-dashstats-dev')


# Scan for unattached EBS volumes
def scan_unattached_volumes():
    ec2 = session.client('ec2')
    response = ec2.describe_volumes(
        Filters=[
            {'Name': 'status', 'Values': ['available']}
        ]
    )
    
    unatt_volumes = response['Volumes']
    return unatt_volumes

# Take a snapshot of an EBS volume
def create_snapshot(v_id):
    ec2 = session.client('ec2')
    response = ec2.create_snapshot(
        VolumeId=v_id,
        Description='Snapshot of unattached volume'
    )
    snapshot_id = response['SnapshotId']
    
    print(f"Snapshot created: {snapshot_id}")
    return snapshot_id

# Delete an EBS volume
def delete_volume(volume_id):
    ec2 = session.client('ec2')
    ec2.delete_volume(VolumeId=volume_id)
    print(f"Volume deleted: {volume_id}")

# Main
unattached_volumes = scan_unatt_volumes()

for volume in unattached_volumes:
    volume_id = volume['VolumeId']
    snapshot_id = create_snapshot(volume_id)
    delete_volume(volume_id)
