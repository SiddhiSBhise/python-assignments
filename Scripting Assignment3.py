import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def fetch_ec2_instances():
    """
    Fetch all EC2 instances in the AWS account and region.
    :return: List of EC2 instances with ID, state, and launch time.
    """
    try:
        ec2 = boto3.client('ec2')  # Initialize EC2 client
        response = ec2.describe_instances()  # Fetch instance details
        instances = []

        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instances.append({
                    'InstanceId': instance['InstanceId'],
                    'State': instance['State']['Name'],
                    'LaunchTime': instance['LaunchTime']
                })

        return instances
    except NoCredentialsError:
        print("Error: AWS credentials not found. Please configure your credentials.")
        return []
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials. Ensure both access key and secret key are set.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def identify_idle_instances(instances):
    """
    Identify idle EC2 instances (stopped state).
    :param instances: List of EC2 instance data.
    :return: List of idle instances.
    """
    idle_instances = [inst for inst in instances if inst['State'].lower() == 'stopped']
    return idle_instances

if __name__ == "__main__":
    print("Fetching EC2 instances...")
    ec2_instances = fetch_ec2_instances()

    if not ec2_instances:
        print("No EC2 instances found or an error occurred.")
    else:
        print("Identifying idle instances...")
        idle_instances = identify_idle_instances(ec2_instances)

        if idle_instances:
            print(f"Found {len(idle_instances)} idle instance(s):")
            for instance in idle_instances:
                print(f"- Instance ID: {instance['InstanceId']}, Launch Time: {instance['LaunchTime']}")
        else:
            print("No idle instances found.")
