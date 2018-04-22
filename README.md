# aws-conf

AWS-conf is a simple command line app for controlling AWS using Python and the boto library. To run the application, double click on aws-conf.py or open it at the command line.

# How does the application work?

The entire application is built on top of a simple  while loop that takes user input (numbers 1-23) to decide which part of the application to execute. When further text input is required, the relevant infomration is presented and the user copy/pastes values as input.
   
    if choice==1
    <application code>

    if choice==2
    <applcation code>

    etc 

Functions for each of the part of the application are kept in python modules included in the application directory, one for each AWS compoent, EC2.py, S3.py, etc. Modules are imported at the start of the the main aws-conf file, and functions are called throughout the rest of the application. The AWS resources are instantiated from the Resources.py class.

# Security

The application secret keys are stored in a config.py file that has been added to the .gitignore to prevent it from being accidentally commited to a public github. The keys are called by reference in the rest of the application code.

    #owner id from config.py
    self.owner_id = config.owner_id


