#jam

import sys,os,platform
import time
import subprocess
from threading import Timer

#subprocess.call(["python3","test.py"])
#abc=subprocess.check_output(["python3","test.py"])
# print("abc")
# lists=subprocess.Popen(["python3","test.py"],stdout=subprocess.PIPE)
# try:
# 	abc=lists.communicate(timeout=2)
# except subprocess.TimeoutExpired:
# 	lists.kill()
# 	abc=lists.communicate()
# print(abc)


def find_interface():
    moni=subprocess.Popen(['iwconfig'],text=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    all_infac,err=(moni.communicate())
    wireless_inter=all_infac.split("\n")[0].split()[0]
    return wireless_inter

def start_monitorMode():
    IFace=find_interface()
    # act_Mon1_string="sudo ip link set "+IFace+" down"
    # act_Mon2_string="sudo iw "+IFace+" set monitor control"
    # act_Mon3_string="sudo ip link set "+IFace+" up"
    # cmd1=subprocess.Popen(act_Mon1_string.split(" "),)
    # cmd2=subprocess.Popen(act_Mon2_string.split(" "),)
    # cmd3=subprocess.Popen(act_Mon3_string.split(" "),)
    #
    # print("\t\t\tShould disabled network Manager \nPress y/n (yes/no)")
    # x=input()
    # if(x=='y'):
    #     dis_networkManager_string="service NetworkManager stop"
    #     # cmd4=subprocess.Popen(act_Mon3_string.split(" "),)
    # else:
    #     print("Cant continue with out disabling network")
    act_mon="sudo airmon-ng start "+IFace
    cmd_start_mon=subprocess.Popen(act_mon.split(" "),text=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    cmd_start_mon.wait()
    cmd_start_mon.terminate()
    # print(get_InterFace)



def getting_bssid():
    InterFace=find_interface()
    act_bssid="timeout 10s airodump-ng -w out --output-format csv "+InterFace
    print(act_bssid.split())
    try:
        cmd_bssid = subprocess.run(
            act_bssid.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,check=True,timeout=10,)
    except subprocess.TimeoutExpired:
        # Handle exception
        print("sucessfull data")

    # print(stdout)


    pass



def medula():
    print("medu the wifi y/n")
    x=input()
    if(x=="y"):
        # start_monitorMode()
        getting_bssid()
        print("yahooo")

    else:
        medula()

system_os=platform.system()
print(system_os)
if system_os == 'Linux':
    medula()
else:
    print('no')

# str=subprocess.run(["ls","-al"],capture_output=True,text=True)
# print(str.stdout.split("\n"))
