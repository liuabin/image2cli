#!python3
import os
# os.system("echo -e \'dafasdfa\' ")
cmd = r"echo -e '\e[43;33;4m  \e[0m'"
f = open("temp.sh", 'w')
f.write(r"#!/bin/bash" + "\n")
f.write(cmd + "\n")
os.system("bash temp.sh" + "\n")