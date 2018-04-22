## AWS CONF a boto3 program for controling AWS objects by Aidan Reilly

#boto/AWS components
import boto3
import Resources
import EC2
import Volumes
import S3
import CloudWatch
import os
import sys
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

#silly thing to put a nerdy ascii banner in
print (" ")
print (" ")
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
cprint(figlet_format('AWS CONF', font='doom'),
       'red', attrs=['bold'])
os.system('pause')

#instantiate all the AWS objects
res = Resources.Resource()
ec2 = res.EC2Resource()
ec2_cont = EC2.EC2Controller()
ebs_cont = Volumes.Volumes()
s3 = res.S3Resource()
contS3 = S3.S3Controller()
cw = res.CWClient()
contCW = CloudWatch.CWController()

tags = [
    { "Key": "key1", "Value": "value1"  },
    { "Key": "key2", "Value": "value2"  }
    ]

def print_menu():
    #build the splash
    print (75 * "-")
    print ("---Aidan Reilly - R00156542---" + 45 * "-")
    print (" ")
    print (" ")
    print (75 * "-")
    print ("Use this program to work with AWS using Python and Boto3.")
    print ("Select from the options below.")
    print (75 * "-")      
    print (" ")
    print (75 * "-")
    print ("---EC2---" + 66 * "-")
    print (" ")
    print ("<  1  > - List all running EC2 instances")
    print ("<  2  > - Enter an instance ID to view the instance status")
    print ("<  3  > - Stop all EC2 instances")
    print ("<  4  > - Stop a specific instance")
    print ("<  5  > - Create an AMI from an existing instance")
    print ("<  6  > - Launch a new instance from an existing AMI")
    print (" ")
    print (75 * "-")
    print ("---EBS Storage---" + 58 * "-")
    print (" ")
    print ("<  7  > - List all volumes")
    print ("<  8  > - Attach an existing volume to an instance")
    print ("<  9  > - Detach a volume from an instance")
    print ("<  10  > - Take a snapshot of a specific volume")
    print ("<  11  > - List all snapshots")
    print ("<  12  > - Create a volume from a snapshot")
    print (" ")
    print (75 * "-")
    print ("---Work with S3 Storage---" + 49 * "-")
    print (" ")
    print ("<  13  > - List all buckets")
    print ("<  14  > - List all objects in a bucket")
    print ("<  15  > - Upload an object")
    print ("<  16  > - Download an object")
    print ("<  17  > - Delete an object")
    print (" ")
    print (75 * "-")
    print ("---Monitoring---" + 59 * "-")
    print (" ")
    print ("<  18  > - Display metrics gathered for an EC2 instance")
    print ("<  19  > - Set a CPU alarm")
    print (" ")
    print (75 * "-")
    print ("---Autoscaling---" + 58 * "-")
    print (" ")
    print ("<  20  > - Do summit")
    print ("<  21  > - Do summit")
    print ("<  22  > - Do summit")
    print ("<  23  > - Do summit")
    print ("<  24  > - Do summit")
    print (" ")
    print (75 * "-")
    print ("---Exit---" + 65 * "-")
    print (" ")
    print ("<  0  > - Exit the program")
    print (" ")

loop=True      

while loop:          ## While loop which will keep going until loop = False
    try:
        print_menu()
        choice = input("Enter your choice 1-24, or 0 to exit: ")
        ### Convert string to int type ##
        choice = int(choice)

        if choice==1:     
            print ("Item < 1 > has been selected")
            print ("")
            print ("Running AWS EC2 instances:")
            print ("")
            try:
                ec2_cont.list_instances( ec2 )
            except:
                print ("")
                print ("No running instances...")
            print ("")
            os.system('pause')

        elif choice==2:
            print ("Item < 2 > has been selected")
            print ("")
            print ("Running AWS EC2 instances:")
            print ("")
            ec2_cont.list_instances_ids( ec2 )
            instance_id = input("Enter the id of the instance you want to query: ")
            ec2_cont.list_instance( ec2, instance_id )
            os.system('pause')

        elif choice==3:
            print ("Item < 3 > has been selected")
            print ("")
            print ("Stopping all AWS EC2 instances...")
            print ("")
            ec2_cont.stop_instances( ec2 )
            print ("All AWS EC2 instances stopped.")
            os.system('pause')

        elif choice==4:
            print ("Item < 4 > has been selected")
            print ("")
            print ("Running AWS EC2 instances:")
            print ("")
            ec2_cont.list_instances_ids( ec2 )
            instance_id = input("Enter the id of the instance you want to stop: ")
            ec2_cont.stop_instance( ec2, instance_id )
            print ("Instance stopped.")
            os.system('pause')

        elif choice==5:
            print ("Item < 4 > has been selected")
            print ("")
            print ("Running AWS EC2 instances:")
            print ("")
            ec2_cont.list_instances_ids_AMIs( ec2 )
            image_id = input("Enter the AMI id of the instance you want to create: ")
            ec2_cont.create_instance( ec2, image_id )
            print ("Instance created from image", image_id)
            os.system('pause')

        elif choice==6:
            print ("Item < 6 > has been selected")
            print ("")
            print ("Running AWS EC2 instances:")
            print ("")
            ec2_cont.list_instances_ids_AMIs_OS( ec2 )
            print ("")
            image_id = input("Enter the AMI id of the running instance that you want to duplicate: ")
            ec2_cont.create_instance( ec2, image_id )
            print ("Instance created from image", image_id)
            os.system('pause')

        elif choice==7:
            print ("Item < 7 > has been selected")
            print ("")
            print ("All current EBS volumes:")
            ebs_cont.list_volumes(ec2)
            os.system('pause')

        elif choice==8:
            print ("Item < 8 > has been selected")
            print ("")
            print ("All current stopped EC2 instances:")
            print ("")
            ec2_cont.list_stopped_instances(ec2)
            print ("")
            print ("All current EBS volumes:")
            print ("")
            ebs_cont.list_volumes(ec2)
            print ("")
            inst_id = input("Enter the EC2 instance id of the instance that you want to attach a volume to: ")
            print ("")
            vol_id = input("Enter the volume id of the volume that you want to attach to the EC2 instance: ")
            print ("")
            #dev input must be xvd[f-z]
            dev = input("Enter the volume device name: ")
            print ("")
            ebs_cont.attach_volume( ec2, inst_id, vol_id, dev) 
            print ("Volume", vol_id, "attached to instance ", inst_id)
            print ("")
            os.system('pause')

        elif choice==9:
            print ("Item < 9 > has been selected")
            print ("")
            print ("All current EBS volumes:")
            ebs_cont.list_volumes(ec2)
            print ("")
            inst_id = input("Enter the EC2 instance id of the instance that you want to detach a volume from: ")
            print ("")
            vol_id = input("Enter the volume id of the volume that you want to detach: ")
            print ("")
            #dev input must be xvd[f-z]
            dev = input("Enter the volume device name: ")
            print ("")
            ebs_cont.detach_volume( ec2, inst_id, vol_id, dev)
            print (vol_id, "detached from", "instance", inst_id)
            os.system('pause')

        elif choice==10:
            print ("Item < 10 > has been selected")
            print ("")
            print ("All current EBS volumes:")
            ebs_cont.list_volumes(ec2)
            vol_id = input("Enter the volume id of the volume that you want to take a snapshot of: ")
            ebs_cont.create_snapshot(ec2, vol_id, "Snapshot")
            print ("Snapshot of volume", vol_id, "created.")
            os.system('pause')

        elif choice==11:
            print ("Item < 11 > has been selected")
            print ("")
            print ("All current EBS volume snapshots:")
            print ("")
            try:
                ebs_cont.list_snapshots(ec2)
            except:
                print ("No EBS snapshots found.") 
            os.system('pause')

        elif choice==12:
            print ("Item < 12 > has been selected")
            print ("All current EBS volume snapshots: ")
            print ("")
            try:
                ebs_cont.list_snapshots(ec2)
            except:
                print ("")
                print ("No EBS snapshots found.") 
            print ("")    
            vol_id = input("Enter the volume snapshot id that you want to create a volume from: ")
            #create volume
            ebs_cont.create_volume( ec2, vol_id, "New Snapshot")
            print ("Volume created")
            os.system('pause')

        elif choice==13:
            print ("Item < 13 > has been selected")
            print ("All current S3 buckets: ")
            try:
                contS3.list_buckets(s3) 
            except:
                print ("No S3 buckets found.") 

            os.system('pause')

        elif choice==14:
            print ("Item < 14 > has been selected")
            print (" ")
            print ("All S3 buckets: ")
            try:
                contS3.list_buckets(s3) 
            except:
                print ("No S3 buckets found.") 
                print (" ")
            print (" ")
            bucky = input("please enter the bucket you want to investigate: ")
            print (" ")
            print ("Bucket", bucky, "contains the following objects: ")
            print (" ")
            contS3.list_objects( s3, bucky)
            print (" ")
            os.system('pause')

        elif choice==15:
            print ("Item < 15 > has been selected")
            print (" ")
            print ("All S3 buckets: ")
            try:
                contS3.list_buckets(s3) 
            except:
                print ("No S3 buckets found.") 
            print ("")
            bucky = input("Upload an object; please enter the bucket to upload to: ")
            print ("")
            filename = input("Enter the filename to upload (must be in project dir): ")
            print (" ")
            print ("Uploading...")
            #last argument encodes the filename as the object key, makes it easier to download
            contS3.upload_file( s3, bucky, filename, filename)
            print (" ")
            print ("Object uploaded!")
            print (" ")
            os.system('pause')

        elif choice==16:
            print ("Item < 16 > has been selected")
            print ("Download an object from one of the following buckets...")
            print (" ")
            try:
                contS3.list_buckets(s3) 
            except:
                print ("No S3 buckets found.") 
            print (" ")
            bucky = input("Enter the bucket name: ")
            print (" ")
            print ("Bucket", bucky, "contains the following objects: ")
            print (" ")
            contS3.list_objects(s3, bucky)
            print (" ")
            key = input("Enter the key of the object want to download: ")
            print (" ")
            #the last key argument names the file the same as the key it was named as going in.  
            contS3.download_file(s3, bucky, key, key)
            print (" ")
            print ("Object downloaded to project folder!")
            print (" ")
            os.system('pause')

        elif choice==17:
            print ("Item < 17 > has been selected")
            print ("Delete an object from one of the following buckets...")
            print (" ")
            try:
                contS3.list_buckets(s3) 
            except:
                print ("No S3 buckets found.") 
            print (" ")
            bucky = input("Enter the bucket name: ")
            print (" ")
            print ("Bucket", bucky, "contains the following objects: ")
            print (" ")
            contS3.list_objects(s3, bucky)
            print (" ")
            key = input("Enter the key of the object want to delete: ")
            print (" ")
            #the last key argument names the file the same as the key it was named as going in.  
            contS3.delete_file(s3, bucky, key)
            ## contS3.delete_file( s3, "bucket2018stynesnew", "S3copyOfS3" )
            print (" ")
            print ("Object deleted!")
            print (" ")
            os.system('pause')

        elif choice==18:
            print ("Item < 18 > has been selected")
            print ("")
            print ("All current EC2 instances:")
            ec2_cont.list_instances(ec2)
            print ("")
            #Display all default performance metrics gathered for a particular EC2 instance (Prompt the user for the EC2 instance in question), averaged over the last 10minutes.
            instance = input("Enter the instance id of the VM you want to investigate: ")
            print (" ")
            print ("Statistics for instance", instance, ": ")
            contCW.get_metric_statistics(cw, instance)
            print (" ")
            os.system('pause')

        elif choice==19:
            print ("Item < 19 > has been selected")
            #Set an alarm such that if the CPU utilization is less than 40% an alarm will be raised. When an alarm is raised, use the AWS SNS to send a notification to an email account. The user should be able to specify the email address as a menu option at the command line.
            print ("")
            print ("Set an alarm for CPU utilization < 40%. AWS will send a notification via email.")
            print ("")
            email = input("Enter your email address: ")
            print ("")
            print ("Running AWS EC2 instances:")
            print ("")
            ec2_cont.list_instances( ec2 )
            print ("")
            inst_id = input("Enter the instance id of the VM you want to set an alarm for: ")
            print ("")
            contCW.set_alarm(cw, inst_id, "CPUUtilization", 40.0, "Percent" )
            print ("Alarm Created!")
            print ("")
            os.system('pause')

        elif choice==20:
            print ("Item < 20 > has been selected")
            #Choose from one of the following free tier Amazon services. Describe what it does (in the python script) and provide a detailed exa mple of how you can manipulate it using boto3 (give 4 short examples). You should describe how you tested these features.  
            #- Autoscaling
            #- AmazonDB
            #- Relational DB Service
            #- Elastic Load Balancing
            os.system('pause')

        elif choice==21:
            print ("Item < 21 > has been selected")
            #this works, just send a mail
            contCW.send_sns_email(cw)
            os.system('pause')

        elif choice==22:
            print ("Item < 22 > has been selected")
            os.system('pause')

        elif choice==23:
            print ("Item < 23 > has been selected")
            os.system('pause')

        elif choice==24:
            print ("Item < 24 > has been selected")
            os.system('pause')

        elif choice==0:
            print ("")
            print ("Exiting program...")
            print ("")
            loop=False

        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Did you make an incorrect selection? Hit any key to start again...")

    except Exception as e: 
        print(e)
        os.system('pause')

