#jam

import sys,os
import subprocess
import http
#subprocess.call(["python3","test.py"])
#abc=subprocess.check_output(["python3","test.py"])
print("abc")
lists=subprocess.Popen(["python3","test.py"],stdout=subprocess.PIPE)
try:
	abc=lists.communicate(timeout=2)
except subprocess.TimeoutExpired:
	lists.kill()
	abc=lists.communicate()
print(abc)
