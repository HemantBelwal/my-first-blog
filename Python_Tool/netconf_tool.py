#!/usr/bin/env python

import getpass
import sys
import telnetlib
import re
import pexpect


HOST = "10.121.234.87"
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()
user = "gss"
password = "pureethernet"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
f = open("/home/hemkumar/Python/startup-config","r")

def netconf():
    child = pexpect.spawn ("yangcli-pro --server=10.121.234.87  --user=gss --password=pureethernet --ncport=830 --timeout 10 --autoload-save-cache=false --autoload-cache=false")
	#print child.before
    child.expect ('gss@.*', timeout= None)
    child.sendline ('sget vlli')
    child.expect('gss@.*')
    a = child.before
    for valueTest in a.splitlines():
        matchobj1 = re.match(r'(\s+)vlli(.*)', valueTest, flags=0)
        if matchobj1:
           print matchobj1.group()
for value in f:
    #print value
    for value1 in value.splitlines():
        matchobj = re.match(r'virtual-link-loss-indication(.*)', value1, flags=0)
	if matchobj:
	   HOST = "10.121.234.87"
           user = "gss"
           password = "pureethernet"

           tn = telnetlib.Telnet(HOST)

           tn.read_until("login: ")
           tn.write(user + "\n")
           if password:
              tn.read_until("Password: ")
              tn.write(password + "\n")

           tn.write(matchobj.group() + "\n")
           tn.write("exit\n")

           test= tn.read_all()
           #print test
	   netconf()
 
