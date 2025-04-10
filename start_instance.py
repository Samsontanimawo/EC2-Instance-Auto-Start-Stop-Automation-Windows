
import boto3

INSTANCE_ID = 'AWS INSTANCE ID'
REGION = 'AWS REGION'  # Change if your instance is in another region

def start_instance():
    ec2 = boto3.client('ec2', region_name=REGION)
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print(f"Instance {INSTANCE_ID} started.")

if __name__ == "__main__":
    start_instance()
