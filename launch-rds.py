import boto3

session = boto3.Session(profile_name='account')

# Create an RDS snapshot
def create_rds_snapshot(db_instance_identifier, snapshot_identifier):
    rds = session.client('rds')
    response = rds.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceIdentifier=db_instance_identifier
    )
    snapshot_arn = response['DBSnapshot']['DBSnapshotArn']
    
    print(f"RDS snapshot created: {snapshot_arn}")
    return snapshot_arn

# Launch an RDS instance from a snapshot
def launch_rds_instance_from_snapshot(snapshot_identifier, db_instance_identifier):
    rds = session.client('rds')
    response = rds.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=db_instance_identifier,
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceClass='db.t2.micro',  
        Engine='mysql',  )
        MultiAZ=False,  # Set to True for Multi-AZ deployment
        PubliclyAccessible=False,
        
      Tags=[]
    )
    instance_arn = response['DBInstance']['DBInstanceArn']
    
    print(f"RDS instance launched: {instance_arn}")
    return instance_arn


db_instance_identifier = 'db-instance'
snapshot_identifier = 'example-snapshot'

# Create an RDS snapshot
snapshot_arn = create_rds_snapshot(db_instance_identifier, snapshot_identifier)

# Launch an RDS instance from a snapshot
instance_arn = launch_rds_instance_from_snapshot(snapshot_identifier, db_instance_identifier)
