import boto3

session = boto3.Session(profile_name='account')

# Create an SNS topic
def create_sns_topic(topic_name):
    sns = session.client('sns')
    response = sns.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    print(f"SNS topic created: {topic_arn}")
    return topic_arn

# Create an SQS queue
def create_sqs_queue(queue_name):
    sqs = session.client('sqs')
    response = sqs.create_queue(QueueName=queue_name)
    queue_url = response['QueueUrl']
    print(f"SQS queue created: {queue_url}")
    return queue_url


sns_topic_name = 'example-topic'
sqs_queue_name = 'example-queue'

# Create 
topic_arn = create_sns_topic(sns_topic_name)

queue_url = create_sqs_queue(sqs_queue_name)

