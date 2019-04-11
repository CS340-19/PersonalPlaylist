# Assignment 1: Deploying webserver 

The purpose of the assignment is to familiarize you with the automatic build, containers, and cloud computing

## The due date is TBD.

1. Create repo yougithubid/webserver
2. Add Dockerfile, for example as the one in this repo
3. Add index.html with your name in it
4. Create automatic build

       i. on hub.docker.com create id for yourself (if you have not done so before)
       ii. create automated build (pull out from the top menu)
       iii. connect to github repo you have just created
5. make a change on the github repo (to trigger build)
6. Verify that the build succeeded https://hub.docker.com/r/yourdockerhubid/webserver/builds/
7. Create a virual machine on GCP

       i. go to https://console.cloud.google.com/compute/instances select the class project and click on craete instance
       ii. Next to memory click customize and reduce 1G
       iii. Mark checkmark "Deploy a container image to this VM" and enter image 'yourdockerhubid/webserver'
       iv. Mark checkmark "Allow HTTP traffic"
       v. expand "Management, disks, networking, SSH keys"
       vi. in the "startup script" box enter    
```    
#!/bin/bash
docker rm ws
docker run -d --name ws -p80:80 yourdockerhubid/webserver
```
8. Click "Create" button at the bottom
9. Check if the webserver works
       
         i. enter the external ip adress (for the machine you created) in your browser (you should get your name)
         ii. If that does not work connect to the machine
         iii. Open shell
         iv. type gcloud compute ssh "your instance name"
         v. once connected to your instance type 'docker ps': your container should be running
10. Enter ip adress of the machine at the bottom of your netid.md file in the CS340-19/students repo and create a pull request
         
