# Deployment and Building Containerized Python App

In this project, we created a web site that allows users to upload hash file and generates a simple report using information provided by
querying VirusTotal's public API and have used Redis for caching so that when you user request same hashes next time, the side will provide data from in-memory rather than calling virustotal API again, which makes our app provide data fast. This web app deployed both to AWS Elastic Beanstalk environment.

**Used Technologies**

* Python Bottle web framework 
* Redis for in-memory caching
* Docker
* AWS PaaS, Elastic Beanstalk environment for single containerized app. 


**Files explanation**

* app.py: Python app that provides report about hashes through API call 
* Dockerfile :for building the docker image 
* requirements.txt :requirements modules for building our app 
* run_docker.sh:file to be able to get Docker running, locally 
* upload_docker.sh: file to upload the image to docker Hub for Elastic Beanstalk 
* Dockerrun.aws.json: under the remote-docker directory, used by Elastic Beanstalk to deploy app to eb environment 

### How to Run

To run this app in docker image locally, type terminal command:

        ./run_docker.sh
        
After running this app locally, push it to Docker Hub, type terminal command:

    ./upload_docker.sh
