import boto3
import datetime

class CWController:

    # A class for controlling AWS CloudWatch settings to monitor metrics
    # and create/use alarms.

    def __init__(self):

        # CWController Constructor
        pass

    def get_metric_statistics(self, cw, instance_id):
        metrics=['CPUUtilization', 'DiskReadBytes', 'NetworkIn', 'NetworkOut', 'ReadThroughput', 'WriteThroughput', 'FreeStorageSpace', 'CPUCreditBalance']
        i = 0
        while i < 8:
            if i < 8:
                for metric in metrics:
                    a = cw.get_metric_statistics(
                    Period=600,
                    StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
                    EndTime=datetime.datetime.utcnow(),
                    MetricName=metrics[i],
                    Namespace="AWS/EC2",
                    Statistics=["Average"],
                    Dimensions=[{"Name":"InstanceId", "Value":instance_id}]
                    )
                    print(a)
                    i += 1  

    def set_alarm( self, cw, instance_id, metric, value, unit_type ):

        # Create alarm for the instance 'instance_id' on the metric 'metric'
        # to trigger if it exceeds threshold 'value', using the CloudWatch
        # Client "cw". The "unit_type" specifies the units used by the given
        # metric.

        cw.put_metric_alarm(
            AlarmName="Your AWS VM CPU utilization is below 40%!",
            ComparisonOperator="GreaterThanThreshold",
            EvaluationPeriods=1,
            MetricName=metric,
            Namespace="AWS/EC2",
            Period=300, #INSUFFICIENT_DATA error if lower than the period of the metric
            Statistic="Average",
            Threshold=value,
            #turn this to true to enable SNS response
            ActionsEnabled=True,
            #add ARN for SNS email alert 
            AlarmActions=['arn:aws:sns:eu-west-1:243015836428:CPU-alarm'],
            AlarmDescription="Alarm for CPU utilization is below 40%!",
            Dimensions=[
                {
                    "Name":"InstanceId",
                    "Value": instance_id
                },
            ],
            Unit=unit_type
            )

# function to send an email to a topic...
    def send_sns_email(cw, self):
        client = boto3.client('sns')
        response = client.publish(
            TopicArn='arn:aws:sns:eu-west-1:243015836428:CPU-alarm',
            Message='CPU went below 40% blud. Sort it out!'
            )
        print("Response: {}".format(response))



#http://boto3.readthedocs.io/en/latest/guide/cw-example-creating-alarms.html
    def delete_alarm(self, cw, name):

        # Deletes an alarm with the given 'name', using the CloudWatch client "cw"
        cw.delete_alarms(
            AlarmNames=[name]
            )
