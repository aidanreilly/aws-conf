import boto3
import config

class Volumes:
    # A class which functions as a controller for AWS EBS volumes

    def __init__(self):        
        #owner id from config.py
        self.owner_id = config.owner_id
        pass

    def list_volumes( self, ec2 ):

        # List all volumes associated with the given 'ec2' resource
        count = 0
        for volume in ec2.volumes.all():
            #print( volume )

            print( "***************************************************" )

            print( "Volume ID:", volume.volume_id )
            print( "Volume State:", volume.state )
            #str method here is casting the int volume.size to a string 
            print( "Volume Size:", str(volume.size)+"GB" )
            print( "Volume Zone:", volume.availability_zone )
            print( "Volume Type:", volume.volume_type )

            attach_data = volume.attachments
            #print( attach_data )
            for attachment in attach_data:
                print( "EC2 Instance ID:", attachment["InstanceId"] )
                print( "Time of Attachment:", attachment["AttachTime"] )
                print( "Device:", attachment["Device"] )

            print( "***************************************************" )

            count += 1

        if count == 0 :
            print( "No EBS Volumes Detected!" )


    def attach_volume(self, ec2, instance_id, volume_id, dev_name):

        # Attach volume with id "volume_id" to the EC2 instance with
        # id "instance_id", where it is the device "dev_name",
        # using the Resource "ec2"
        try:
            ec2.Instance(instance_id).attach_volume(VolumeId=volume_id, Device=dev_name)
        except error as e:
            print (e)

    def detach_volume(self, ec2, instance_id, volume_id, dev_name):
        # Detach the volume with id "volume_id" from the EC2 instance with
        # id "instance_id" where it is device "dev_name",
        # using the given 'ec2' Resource
        try:
            ec2.Instance(instance_id).detach_volume(VolumeId=volume_id, Device=dev_name)
        except error as e:
            print (e)

    def create_snapshot( self, ec2, volume_id, description ):
        # Creates and returns a snapshot, with the given 'description',
        # of the EBS volume 'volume_id', using the "ec2" Resource.

        snapshot = ec2.create_snapshot(VolumeId=volume_id, Description=description)
        return snapshot

    def list_snapshots(self, ec2):
        #ec2.snapshots.all() gets you ALL snapshots in existence in your region(uh oh!)
        for snapshot in ec2.snapshots.filter(OwnerIds=[self.owner_id]):
            print( "Snapshot ID:", snapshot.snapshot_id )
            print( "Snapshot Volume ID:", snapshot.volume_id )
            print( "Snapshot Size:", snapshot.volume_size )
            print( "Snapshot State:", snapshot.state )

    def delete_snapshot( self, ec2, snapshot_id ):
        # Deletes the snapshot with id 'snapshot_id'
        snapshot = ec2.Snapshot(snapshot_id)
        snapshot.delete()
    

        
