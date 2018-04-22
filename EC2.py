import boto3

class EC2Controller:
    # A class for controlling interactions with the boto3 EC2 Resource Interface

    def __init__( self ):
        # EC2Controller Constructor
        pass

    def list_instances( self, ec2 ):
        # List all instances for the EC2 Resource 'ec2'
        count = 0
        for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]) :
            print("Instance", count, "-", "AMI id:",  instance.image_id, "Instance id:", instance.id, " Launched:", instance.launch_time)
            count += 1
        #count == 0 basically says: "if there are no hits on the filter search"   
        if count == 0:
            print( "No EC2 instances detected!" )

    def list_instance( self , ec2, instance_id):
        try:     
            count = 0
            # Return an instance with id of instance_id using a filter on the kwarg InstanceIds
            for instance in ec2.instances.filter(InstanceIds=[instance_id]):
                print("Instance", count, "-", "AMI id:",  instance.image_id, "Instance id:", instance.id, " Launched:", instance.launch_time)
                count += 1

        except:
            print ("No instance found for that input, please try again.")     

    def list_stopped_instances(self , ec2):
        #list stopped instances
        try:
            instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'terminated']}])
            for instance in instances:
                print("Instance: ", instance.id, "instance type: ", instance.instance_type)
        except:
            print ("No stopped instances found...")  

    def list_instances_ids( self, ec2 ):
        # List all running EC2 instance ids for the EC2 Resource 'ec2'
        count = 0
        for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]) :
            print("Instance", count, "-", "Instance id:", instance.id)
            count += 1
        if count == 0:
            print( "No running EC2 instances detected!" )

    def start_instance( self , ec2, instance_id):

        # Start instance with id 'instance_id' using interface 'ec2'
        #ec2.instances.filter(InstanceIds=[instance_id]).start()
        ec2.Instance(instance_id).start()

    def stop_instance( self , ec2, instance_id):
        try:
            # Stop instance with id 'instance_id' using interface 'ec2'
            ec2.Instance(instance_id).stop()
        except:
            print ("No instance found for that input, please try again.")    

    def stop_instances( self , ec2 ):
        #stop all instances
        for instance in ec2.instances.all():
            instance.stop()

    #when it absolutely has to be nuclear
    def terminate_instances( self , ec2 ):
        for instance in ec2.instances.all():
            instance.terminate()

    def add_tags( self, ec2, instance_id, tags ):
        # Add the contents of the list of dictionaries 'tags' as tags
        # to EC2 instance with id 'instance_id', using interface 'ec2'
        ec2.Instance(instance_id).create_tags(Tags=tags)

    def delete_tags( self, ec2, instance_id, tags ):
        # Delete the contents of the list of dictionaries 'tags' as tags
        # in instance with id 'instance_id', using interface 'ec2'
        ec2.Instance(instance_id).delete_tags(Tags=tags)

    def create_instance( self, ec2, image_id ):
        # Create a new instance of the given AMI, using the 'ec2' Resource
        ec2.create_instances(ImageId=image_id, MinCount=1, MaxCount=1)

    def list_instances_ids_AMIs( self, ec2 ):
    # List all EC2 instance ids for the EC2 Resource 'ec2'
        try:
            count = 0
            for instance in ec2.instances.all() :
                print("Instance", count, "-", "AMI id:",  instance.image_id, "id:", instance.id)
                count += 1
                if count == 0:
                    print( "No running EC2 instances detected!" )
        except:
            print ("No instance found for that input, please try again.")    

    def list_instances_ids_AMIs_OS( self, ec2 ):
    # List all EC2 instance ids for the EC2 Resource 'ec2'
        try:
            count = 0
            for instance in ec2.instances.all() :
                print("Instance", count, "-", "AMI id:",  instance.image_id, "OS:", instance.platform)
                count += 1
                if count == 0:
                    print( "No running EC2 instances detected!" )
        except:
            print ("No instance found for that input, please try again.")    

    def autoscale_id(self, ec2):
        #set up default autoscale config
        autoscale = ec2.autoscale.connect_to_region('eu-west-1')


                         
