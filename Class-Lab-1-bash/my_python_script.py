#!/home/vagrant/mambaforge/bin/python
import platform
import sys
import os

print('Enter your name:')
username = input()
print(f"Hello {username}!")
print(f"You are running python on {platform.system()}, release {platform.release()}.")
print(f"Your python version is {sys.version}, installed at {sys.exec_prefix}")
print(f"Your current working directory is {os.getcwd()}.", end=" ")
print(f"It has {len(os.listdir())} files and directories in it.")