#   ==TOASTMOD==
#   This script generates a backup of the current VM.
#   Make sure the VM is properly shut down first.

import os
from shutil import copyfile
import time

index = 0
date = time.strftime("%Y-%m-%d")
backupname = str(date+"-#"+str(index))

def backupFiles():
	global backupname
	copyfile("debian_squeeze_mipsel_standard.qcow2", backupname+"/debian_squeeze_mipsel_standard.qcow2")
	copyfile("vmlinux-2.6.32-5-4kc-malta", backupname+"/vmlinux-2.6.32-5-4kc-malta")
	copyfile("startvm.sh", backupname+"/startvm.sh")
	copyfile("startvm-nographic.sh", backupname+"/startvm-nographic.sh")

def makenewDir():
	global index
	global date
	global backupname

	while os.path.exists(backupname) == True:
		index = index+1
		backupname = str(date+"-#"+str(index))

	if not os.path.exists(backupname):
		print("making new backup #"+str(index))
		print("@: "+backupname)
		os.makedirs(backupname)
		backupFiles()
		exit()

makenewDir()








