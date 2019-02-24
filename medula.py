#jam

import sys,os,platform
import subprocess
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

def medula():
    print("medu the wifi y/n")
    x=input()
    if(x=="y"):
        start_monitorMode()
        
    else:
        medula()
def start_monitorMode():
    IFace=find_interface()
    act_Mon1_string="sudo ip link set "+IFace+" down"
    act_Mon2_string="sudo iw "+IFace+" set monitor control"
    act_Mon3_string="sudo ip link set "+IFace+" up"
    cmd1=subprocess.Popen(act_Mon1_string.split(" "),)
    cmd2=subprocess.Popen(act_Mon2_string.split(" "),)
    cmd3=subprocess.Popen(act_Mon3_string.split(" "),)

    print("\t\t\tShould disabled network Manager \n Press y/n (yes/no)")
    x=input()
    if(x=='y'):
        dis_networkManager_string="service NetworkManager stop"
        # cmd4=subprocess.Popen(act_Mon3_string.split(" "),)
    else:
        print("Cant continue with out disabling network")



def find_interface():
    moni=subprocess.Popen(['iwconfig'],text=True,stdout=subprocess.PIPE)
    all_infac=(moni.communicate())
    wireless_inter=all_infac[0].split("\n")[0]
    wireless_inter=wireless_inter[0:5]
    return wireless_inter

system_os=platform.system()
print(system_os)
if system_os == 'Linux':
    medula()
else:
    print('no')

# str=subprocess.run(["ls","-al"],capture_output=True,text=True)
# print(str.stdout.split("\n"))
