import os
os.system("tput setaf 5")
print("       *************************")
os.system("tput setaf 1")
print("       HEY GENIUS! Welcome to my project")
os.system("tput setaf 3")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
os.system("tput setaf 6")
print("\tWant to launch , run and deploy OS in just 30 seconds, just Docker")
os.system("tput setaf 9")
print("Docker is a tool designed to make it easier to create , deploy and run application with the use of containers.It enables more efficient use of system resources.")
os.system("tput setaf 3")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 
print("tput setaf 5")
key=input("press any key to continue")
os.system("clear")
os.system("tput setaf 5")
ch='y'
while(ch=='y') :
  os.system("tput setaf 2")
  print("how would you like to execute-- local or remote",end="")
  os.system("tput setaf 4")
  location=input()

  if(location=='local') :

    print(""" BASIC COMMANDS
    press 1 to show date
    press 2 for calender
    press 3 for adding new user
    press 4 to create file
           DOCKER COMMANDS
    press 5 for starting docker
    press 6 for viewing docker images
    press 7 for creating docker container
    press 8 to pull any image 
                NETWORKING IN DOCKER
    press 9 for show list of network in docker
    press 10 to inspect any network
    press 11 to see no of hard disk attached with docker container
                    CREATING A PERSISTENT STORAGE--VOLUME
    press 12 to create volume
    press 13 to see the list of volumes
                    APPLICATION OF DOCKER
    press 14 to start wordpress from docker container""")
    print("enter your choice",end="")
    
    ch=input("...")
    if int(ch)==1 :
      os.system("date")

    elif(int(ch)==2) :
      os.system("cal")
    elif(int(ch)==4) :
      name=input("enter name of file")
      os.system("touch {}.txt".format(name))
      print("file created")
    elif (int(ch)==5) :
      os.system("docker info")
    elif (int(ch)==6):
      os.system("docker images")
    elif(int(ch)==7):
      name=input("enter name of the container")
      print("press exit to  exit from container ")
      os.system("docker run -it {}".format(name))
    elif(int(ch)==8) :
      name=input("enter name of container ")
      os.system("docker pull {}".format(name))
    elif(int(ch)==9) :
      os.system("docker network ls")
    elif(int(ch)==10) :
      name=input("enter name of the network you want to inspect")
      os.system("docker inspect {}".format(name))
      print("...")
    elif(int(ch)==11) :
      os.system("fdisk -l")
      ch=input("want to go inside a hard disk")
      if(ch=='y') :
        name=input("enter name of disk")
        os.system("fdisk /dev/{}".format(name))
       
    elif(int(ch)==12) :
      name=input("enter name of the volume you want to create")
      os.system("docker volume create {}".format(name))
    elif(int(ch)==13) :
      os.system("docker volume ls")
    
    elif(int(ch)==14) :
      os.system("docker run -id -p 80:80 wordpress:5.1.2-php7.3-apache")
    if int(ch)==1 :
      os.system("date")

    elif(int(ch)==2) :
      os.system("cal")
    elif (int(ch)==5) :
      os.system("docker info")
    elif (int(ch)==6):
      os.system("docker images")
    elif(int(ch)==7):
      name=input("enter name of the container")
      print("press exit to  exit from container ")
      os.system("docker run -it {}".format(name))
    elif(int(ch)==8) :
      name=input("enter name of container ")
      os.system("docker pull {}".format(name))
    elif(int(ch)==9) :
      os.system("docker network ls")
    elif(int(ch)==10) :
      name=input("enter name of the network you want to inspect")
      os.system("docker inspect {}".format(name))
   
    elif(ch=='3') :
      print("enter name of the new user")
      user=input()
      os.system("useradd {}".format(user))
    else :
      print("wrong choice")

  elif(location=='remote'):
    remoteIP=input("enter remote ip address")
    print(""" press 1 to show date
              press 2 for calender
              press 3 for adding new user
        press 4 for creating file
          DOCKER COMMANDS
    press 5 for starting docker
    press 6 for viewing docker images
    press 7 for creating docker container
    press 8 to pull any image 
                NETWORKING IN DOCKER
    press 9 for show list of network in docker
    press 10 to inspect any network
    press 11 to see no of hard disk attached with docker container
                    CREATING A PERSISTENT STORAGE--VOLUME
    press 12 to create volume
    press 13 to see the list of volumes
                    APPLICATION OF DOCKER
    press 14 to start wordpress from docker container""")
    ch=input()
    if(int(ch)==1) :
      os.system("ssh {} date".format(remoteIP))
    elif(int(ch)==2) :
      os.system("cal")
    elif ch=='3':
      user=input("enter name of new user")
      os.system("ssh {} useradd {}".format(remoteIP,user))
    elif (int(ch)==5) :
      os.system("docker info")
    elif (int(ch)==6):
      os.system("docker images")
    elif(int(ch)==7):
      name=input("enter name of the container")
      print("press exit to  exit from container ")
      os.system("docker run -it {}".format(name))
    elif(int(ch)==8) :
      name=input("enter name of container ")
      os.system("docker pull {}".format(name))
    elif(int(ch)==9) :
      os.system("docker network ls")
    elif(int(ch)==10) :
      name=input("enter name of the network you want to inspect")
      os.system("docker inspect {}".format(name))
    elif(int(ch)==11) :
      os.system("fdisk -l")
      ch=input("want to go inside a hard disk")
      if(ch=='y') :
        name=input("enter name of disk")
        os.system("fdisk /dev/{}".format(name))


    elif(int(ch)==12) :
      name=input("enter name of the volume you want to create")
      os.system("docker volume create {}".format(name))
    elif(int(ch)==13) :
      os.system("docker volume ls")

    elif(int(ch)==14) :
      os.system("docker run -id -p 80:80 wordpress:5.1.2-php7.3-apache")
       
    else:
      print("wrong choice")
  else:
     print("wrong location! no such ip address")

  print("want to enter more")
  ch=input()
  


                                                             
