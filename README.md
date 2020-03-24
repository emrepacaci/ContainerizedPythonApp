# DevOpsProject

In this project, we created a web site that allows users to upload hash file and generates a simple report using information provided by
querying VirusTotal's public API. I have used Redis for caching so that When you user request same hashes, the side will provide report from cache rather than calling virustotal API again which makes our application fast.
Also, this virustotal public API has limits which is 4 requests/minute so that using local caching system is make sense in this case. This web app deployed both to AWS Elastic Beanstalk environment.

**Used Technologies**

* Python bottle web framework 
* Redis  
* AWS PaaS, Elastic Beanstalk environment for single containerized app. 


**Files explanation**

* app.py: Python app that provides report about hashes through API call 
* Dockerfile :for building the docker image 
* requirements.txt :requirements modules for building our app 
* run_docker.sh:file to be able to get Docker running, locally 
* upload_docker.sh: file to upload the image to docker Hub for Elastic Beanstalk 
* Dockerrun.aws.json: used by Elastic Beanstalk to deploy on environment 
