pipeline {
	agent any
	stages {
		//This is the cleanup stage for removing all the existing code and folder from jenkins server	
		stage ('CleanUp Stage') {
			steps {
				echo 'CleanUp of existing code and folder in jenkins'
				cleanWs()  //This is the command for cleaning up
			}
		}
		
		//This stage is used to checkout from the scm	
		stage('CheckOut Stage') {
			steps {
				echo 'Updates files in the working tree to match the version in the index or the specified tree.'
				checkout scm //This is the command for checking out from scm
			}
		}
		
		//This stage is used to build and test the code before the acutal deployment of main file		
		stage ('Build Stage') {
			steps {
				sh 'sudo su'
				sh 'sudo yum -y update'
				echo 'Creating a virtual environment'
				sh 'sudo yum -y install python-virtualenv' //Creating the virtual python environment to run the code
				sh 'virtualenv myvirtualenv'
				sh 'source myvirtualenv/bin/activate'	  //Activating the virtual environment
				echo 'Installing python and other packages'
				sh 'sudo yum -y install python3' 	  //Installing python3 for running the code
				echo 'Running the unit test case file'
				sh 'python test_bank.py'		//This is the unittest file to test my main python file
			}
		}
		
		//This is the deployment stage where the acutal deployment of application is done in ec2 instance
		stage ('Deploy Stage') {
			steps {
				sh "sudo scp -i  '/var/lib/jenkins/jenkins-20902.pem' -o StrictHostKeyChecking=no -r bank.py ec2-user@54.237.44.226:/home/ec2-user" //Copying files from jenkins to ec2 instance 
				sh "sudo scp -i  '/var/lib/jenkins/jenkins-20902.pem' -o StrictHostKeyChecking=no -r test_bank.py ec2-user@54.237.44.226:/home/ec2-user"
				sh '''sudo ssh -i "/var/lib/jenkins/jenkins-20902.pem" -o StrictHostKeyChecking=no ec2-user@ec2-54-237-44-226.compute-1.amazonaws.com  //Providing the credentials files to ssh into ec2 instance
				echo "Hello Quantiphi!"  		//Simple echo message to check in output
				sudo yum install -y python3 		//Intstalling python3 to run the main file in ec2 instance
				sudo yum install -y python-virtualenv	//Installing virtual env on runtime in ec2 instance
				virtualenv env
				source env/bin/activate			//Activating the virtual environment
				sudo pip3 install unittest2		//Installing the dependencies to run the main file
				python3 bank.py				//Running the mail file in ec2 isntance
				python3 test_bank.py
				<<EOT'''
				echo 'Hello'
			}
		}
	}
}
