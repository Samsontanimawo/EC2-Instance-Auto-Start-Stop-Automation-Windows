import boto3

INSTANCE_ID = 'AWS INSTANCE ID'
REGION = 'AWS REGION'  # Change if your instance is in another region

def stop_instance():
    ec2 = boto3.client('ec2', region_name=REGION)
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print(f"Instance {INSTANCE_ID} stopped.")

if __name__ == "__main__":
    stop_instance()
