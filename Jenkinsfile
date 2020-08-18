pipeline {
	agent any
	stages {
		stage ('CleanUp Stage') {
			steps {
				echo 'CleanUp of existing code and folder in jenkins'
				//cleanWs()
			}
		}
		stage('CheckOut Stage') {
			steps {
				echo 'Updates files in the working tree to match the version in the index or the specified tree.'
				checkout scm
			}
		}
		stage ('Build Stage') {
			steps {
				sh 'sudo su'
				sh 'sudo yum -y update'
				echo 'Creating a virtual environment'
				sh 'sudo yum -y install python-virtualenv'
				sh 'virtualenv myvirtualenv'
				sh 'source myvirtualenv/bin/activate'
				echo 'Installing python and other packages'
				sh 'sudo yum -y install python3'
				echo 'Running the unit test case file'
				sh 'python test_bank.py'
			}
		}
		stage ('Deploy Stage') {
			steps {
				sh "sudo scp -i  '$WORKSPACE/jenkins-20902' -o StrictHostKeyChecking=no -r bank.py ec2-user@54.152.2.54:/home/ec2-user"
				sh "sudo scp -i  '$WORKSPACE/jenkins-20902' -o StrictHostKeyChecking=no -r test_bank.py ec2-user@54.152.2.54:/home/ec2-user"
				sh '''sudo ssh -i "jenkins-20902" -o StrictHostKeyChecking=no ec2-user@ec2-54-152-2-54.compute-1.amazonaws.com 
				echo "Hello Quantiphi!" 
				sudo yum install -y python3
				sudo yum install -y python-virtualenv
				virtualenv env
				source env/bin/activate
				sudo pip3 install unittest2
				python3 bank.py
				python3 test_bank.py
				<<EOT'''
				echo 'Hello'
			}
		}
	}
}
