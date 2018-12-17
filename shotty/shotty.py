import boto3
import click

session = boto3.Session(profile_name='s3-session')
ec2 = session.resource('ec2')

@click.command()

def ec2_instances_list():
    "List the EC2 instances"
    for i in ec2.instances.all():
        #print (ec2.instances.all())
        print(','.join((i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name)))

    return

if __name__ == '__main__' :
    ec2_instances_list()
