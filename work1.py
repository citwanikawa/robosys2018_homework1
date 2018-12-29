#!/usr/bin/python
# -#- coding: utf-8 -*-

import time
import subprocess

while True:
	print"count:"
	count = input()

	if(count != 0):
		for num in range(count):
			cmd = "echo 1 > /dev/myled0"
			subprocess.call(cmd, shell=True)


			time.sleep(0.5)


			cmd = "echo 0 > /dev/myled0"
			subprocess.call(cmd, shell=True)

			time.sleep(0.5)

	else:
		pass

