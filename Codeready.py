
from urllib.request import urlopen
from tkinter import *
from tkinter import filedialog
from tkinter import font
import os
#import routeros_api

#connection = routeros_api.RouterOsApiPool('IP', username='admin', password='')
#api = connection.get_api()

root = Tk()
root.title('IP DESTROYER')

canvas1 = Canvas(root, width = 1900, height = 1000)
canvas1.pack()

label1 = Label(root, text= 'Welcome to ip destroyer', fg='black', font=('helvetica', 40, 'bold'))
canvas1.create_window(950, 40, window=label1)

my_frame = Frame(root)
canvas1.create_window(980, 500, window=my_frame)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=140, height=35, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
my_text.pack()


#SCREEN FRO OPENING FILES 
def openlogfile():  
 text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
 name = text_file
 name = name.replace("C:/gui/", "")
 name = name.replace(".txt", "")
	
 text_file = open(text_file, 'r')
 stuff = text_file.read()

 my_text.insert(END, stuff)

 text_file.close()

 root.title(f'{name} - Textpad')
    

def save_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	text_file = open(text_file, 'w')
	text_file.write(my_text.get(1.0, END))



def add_image():
	# Add image
	global my_image
	my_image = PhotoImage(file="images/profile.png")
	position = my_text.index(INSERT)
	my_text.image_create(position, image=my_image)

	my_label.config(text=position)



  

def searchbadips():  

   textpage= urlopen("http://security-research.dyndns.org/pub/malware-feeds/ponmocup-malware-ips.txt")
   #OPEN THE SAMPLE FILE WITH BAD IPS
   badipss= open("badipss.txt","w+")
   #COPY THE WEB TXT FILE TO A FILE THAT I CREATE FOR BETTER HANDLING
   badipss.write(str(textpage.read(),'utf-8'))
   badipss.close()
   file1 = open("c:/Users/Panagiotis/badipss.txt",'r') 
  
   # defining object file2 to open GeeksforGeeksUpdated file in write mode 
   file2 = open('badips.txt','w') 
   for line in file1.readlines(): 
    
        # reading all lines that do not 
        # begin with "TextGenerator" 
   		if not (line.startswith('#')): 
       		 print(line)         
       		 file2.write(line) 
  

   file2.close() 
   file1.close()

   os.remove("c:/Users/Panagiotis/badipss.txt")


   #compare log with online file


   with open("c:/Users/Panagiotis/Desktop/log1.txt",'r') as file1:
    with open("c:/Users/Panagiotis/badips.txt",'r') as file2:
        same = set(file1).intersection(file2)

   same.discard('\n')

   with open('pcips.txt','w') as pcips:
      for line in same:
          pcips.write(line)

def ipstorouter():
    t=1;
    #  ipv4
    # /ip firewall filter 
    # ban action=accept chain=input comment="default configuration" connection-state=established,related
    # ban action=accept chain=input src-address-list=allowed_to_router
    # ban action=accept chain=input protocol=icmp
    # ban action=drop chain=input
    # /ip firewall address-list
    # f=open('pcips.txt','w'):
    #   for line in same: 
    #
    # ban address=line list=not_allowed_to_router
    
    #ipv6 for list allowed
    # /ipv6 firewall filter
    # add action=accept chain=input comment="allow established and related" connection-state=established,related
    # add chain=input action=accept protocol=icmpv6 comment="accept ICMPv6"
    # add chain=input action=accept protocol=udp port=33434-33534 comment="defconf: accept UDP traceroute"
    # add chain=input action=accept protocol=udp dst-port=546 src-address=fe80::/16 comment="accept DHCPv6-Client prefix delegation."
    # add action=drop chain=input in-interface=sit1 log=yes log-prefix=dropLL_from_public src-address=fe80::/16
    # add action=accept chain=input comment="allow allowed addresses" src-address-list=allowed
    # add action=drop chain=input
    # /ipv6 firewall address-list
    # add address=fe80::/16 list=allowed
    # add address=xxxx::/48  list=allowed
    # add address=ff02::/16 comment=multicast list=allowed

    

#BUTTON1
button1 = Button(text='Open file',command=openlogfile, bg='blue',fg='white')
canvas1.create_window(70, 200, window=button1)

#BUTTON2
button2 = Button(text='Search for bad ips',command=searchbadips, bg='red',fg='white')
canvas1.create_window(70, 300, window=button2)

#BUTTON3
button3 = Button(text='Pass ips to router',command=ipstorouter, bg='green',fg='white')
canvas1.create_window(70, 400, window=button3)

root.mainloop()