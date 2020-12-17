import os
import speech_recognition as sr
import pyttsx3
def Docker():
	os.system("tput setaf 2")
	os.system("echo 'Docker' | figlet -f 3d_row -d ./fonts/ ")
	os.system("sleep 3")
	os.system("tput setaf 1")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		os.system("clear")
		os.system("tput setaf 1")
		print("The available Requriments in Docker")
		os.system("tput setaf 5") 
		print("\n\t\t\tDocker Images\n\t\t\tDocker Containers\n\t\t\tLaunch Docker Container\n\t\t\tRestart Docker Container\n\t\t\tAttach Docker Container\n\t\t\tStop Docker Container\n\t\t\tDocker Status\n\t\t\tRemove Docker Container\n\t\t\tRemove Docker All Container\n\t\t\tRemove Image\n\t\t\tTo go main menu")
		os.system("tput setaf 3")
		print("Start Saying your Requirement in Docker")
		pyttsx3.speak("Start Saying your Requirement in Docker")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	print("Processing your Requirement, plz wait....")
	pyttsx3.speak("Processing your Requirement, please wait")
	docker= r.recognize_google(audio)
	print(docker)
	
	if(("docker images") in docker):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Docker Images | figlet -f 3d_row -d ./fonts/ ")
		os.system("docker images")
		os.system("sleep 3")
	elif(("all docker container" in docker) or ("all docker containers" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Docker Containers| figlet -f 3d_row -d ./fonts/ ")	
		os.system("docker ps -a")
		os.system("sleep 3")
	elif(("launch docker container" in docker) or ("run docker container" in docker) or ("launch a os" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Launching Docker conatiner| figlet -f 3d_row -d ./fonts/ ")
		pyttsx3.speak("launch the container with available images")
		print("launch the container with available images")	
		os.system("docker images")
		image=input("enter image : ")
		tag=input("enter tag : ")
		conatiner_name=input("enter name for container : ")
		os.system("docker run -it --name {} {}:{}".format(conatiner_name,image,tag))
		os.system("exit")
		os.system("sleep 3")
	elif(("start docker container" in docker) or ("start docker containers" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo starting Docker Container| figlet -f 3d_row -d ./fonts/ ")
		pyttsx3.speak("start the container with before launch conatiner")
		print("start the container with before launch conatiner")	
		os.system("docker ps -a")
		start=input("Enter name launched container you want to start : ")
		os.system("docker start {}".format(start))
		os.system("sleep 3")
	elif(("attach docker container" in docker) or ("attach docker containers" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo attaching Docker Container| figlet -f 3d_row -d ./fonts/ ")
		pyttsx3.speak("start the container with before launch conatiner")
		print("attach the container with before launch conatiner")	
		os.system("docker ps")
		attach=input("Enter name launched container you want to attach: ")
		os.system("docker attach {}".format(attach))
		os.system("sleep 3")
	elif(("stop docker container" in docker) or ("stop docker containers" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo stopping Docker Container| figlet -f 3d_row -d ./fonts/ ")
		pyttsx3.speak("stop the container with before launched conatiner")
		print("stop the container with before launched conatiner")	
		os.system("docker ps")
		stop=input("Enter name launched container you want to stop: ")
		os.system("docker stop {}".format(stop))
		os.system("sleep 3")
	elif(("status of docker" in docker) or ("docker status" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Docker status| figlet -f 3d_row -d ./fonts/ ")
		os.system("systemctl status docker")
	elif(("remove container" in docker) or ("remove containers" in docker) or ("delete container" in docker) or ("delete containers" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo deleting Docker Container| figlet -f 3d_row -d ./fonts/ ")
		pyttsx3.speak("delete the container with before launch conatiner")
		print("delete the below container with before launch conatiner")	
		os.system("docker ps -a")
		container=input("Enter name of container you want to remove :")
		os.system("docker rm -f {}".format(container))
	elif(("remove all container" in docker) or ("remove all containers" in docker) or ("delete all container" in docker) or ("delete all containers" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo deleting all Docker Container| figlet -f 3d_row -d ./fonts/ ")
		os.system("docker rm -f $(docker ps -qa)")
	elif(("remove image" in docker) or ("remove images" in docker) or ("delete image" in docker) or ("delete images" in docker)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo deleting Docker image| figlet -f 3d_row -d ./fonts/ ")
		pyttsx3.speak("delete the iamge with before launch conatiner")
		print("delete the below docker images with before launch conatiner")	
		os.system("docker images")
		image=input("Enter name of iamge you want to remove :")
		os.system("docker rmi -f {}".format(image))
	elif("main menu" in docker):
		 main.main()
	else :
        	print("select Correct requirement...")

while(True):	
	Docker()
