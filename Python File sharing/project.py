#! /usr/bin/python3



#--------------------------------------------------------------------------------------------------
#DEPENDENCIES           #(sudo apt install python3)
                        #(pip3 install os)
                        #(pip3 install socket)
                        #(sudo apt install qrencode)
#---------------------------------------------------------------------------------------------------                        
                
                        
                        
                        
import os                #importing the os library (pip3 install os )
import socket            #importing the socet module which helps us in getting our ip address(pip3 install socket)   

print("Using this program you can browse all your system files and you can share the files")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname) #this gets the hostname and your device ip address

s="Press the letter B to go to previous directory or Q to exit and H to Host"    
print("\033[1m" + s + "\033[0m")
while True:
    print("your current working directory is :"+ os.getcwd())          #prionting the current working directory
    dir_list=os.listdir()
    #print("The contents in this directory:" + str(dir_list))
    print("There are "+ str(len(dir_list)) +" Elements in this directory") #printing thr number of elements in the current working directory
    number=[]
    i=1
    for x in range(len(dir_list)):          #creating a list of numbers to assign as keys for the upcoming dictionary
        number.append(i)
        i+=1
    #print(number)
    #print(dir_list)   
    dict = {}                               #initializing the empty dictionary
    for key in number:                      #this loop combines the list of the numbers and the list of the names of the directories into a single dictionary called dict
        for value in dir_list:
            dict[key] = value
            dir_list.remove(value)
            break 
    #print(dict)
    for key, value in dict.items(): #prints the dictionary 'dict in a formatted way'
        print(key, ' : ', value)
  
    a=(input("Enter the number to select:"))       #This elif ladder takes input 'a' from the user and performs the following actions
    if a == 'b' or a == 'B':      #if the input is 'b' or 'B' then it points to the previous parent firectory
        os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
        print("New path ="+ os.getcwd())
    elif a == 'q' or a == 'Q':    #if the input is 'q' or 'Q' then the program/loop will be terminated
        break
    elif a == 'h' or 'H':         #if the input is 'h' or 'H' then the link and its qr code is displayed and also that present directory will gets hosted
        print("The link is "+ip_address+":8090")
        link="The link is "+ip_address+":8090"
        cmd = "{0} -{1} {2}".format("qrencode -t ASCII  ","o qrcode.txt",ip_address)# (sudo apt install qrencode)
        os.system(cmd)  
        os.system("cat qrcode.txt")
        os.system("sudo rm qrcode.txt")
        np="{0} {1}".format("cd ",os.getcwd())
        os.system(np)
        os.system("python3 -m http.server 8090")
           
    else:                #else if any number is entered the corresponding directory will be opened for further operations
        print(dict.get(int(a)))
        os.chdir(dict.get(int(a))) 
        print("New path ="+ os.getcwd())