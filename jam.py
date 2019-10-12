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


import subprocess

from threading import Timer

kill = lambda process: process.kill()
cmd = ['ping', 'www.google.com']
ping = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

my_timer = Timer(5, kill, [ping])

try:
    my_timer.start()
    stdout, stderr = ping.communicate()
finally:
    my_timer.cancel()

print(stdout)
