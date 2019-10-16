#jam

# import sys,os,time
# import subprocess
# #subprocess.call(["python3","test.py"])
# #abc=subprocess.check_output(["python3","test.py"])
# with open('output.txt', 'w') as output:
#  process = subprocess.Popen(["ping","127.0.0.1"], stdout=output)
#  process.communicate()
#  # time.sleep(5)
#  process.terminate()


# import subprocess
# import os
# from threading import Timer
#
# kill = lambda process: process.kill()
# cmd = "sudo timeout 10s airodump-ng -w out --output-format csv wlan0mon"
# # cmd = ['timeout','5s', 'airodump-ng','wlan0mon']
# # subprocess.call(cmd)
# # os.system("timeout 10s airodump-ng wlan0mon")
# try:
#     ping = subprocess.run(
#         cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,check=True,timeout=10,)
# except subprocess.TimeoutExpired:
#     # Handle exception
#     print("sucessfull data")



# my_timer = Timer(5, kill, [ping])
#
# try:
#     my_timer.start()
#     p=1234
#     ping.wait()
# finally:
#     my_timer.cancel()

# print(stdout)




# import subprocess
# import sys
# with open('output.txt', 'w') as f:  # replace 'w' with 'wb' for Python 3
#     cmd = ['timeout','5s', 'airodump-ng','wlan0mon']
#     process = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE)
#     for c in iter(lambda: process.stdout.read(1), b''):  # replace '' with b'' for Python 3
#         sys.stdout.write(c)
#         f.write(c)

import pandas as pd
a = pd.read_csv('./out-01.csv')
print(type(a))
a=a.sort_values(" Power",ascending = False,)
a= a.loc[(a[" Power"]<=-10) & (a[" Power"]>=-80)]
# print(a)
list=a.loc[:,['BSSID',' channel',' ESSID',' Power']]
list = list.dropna()
print(list)
# print(list.dropna())
