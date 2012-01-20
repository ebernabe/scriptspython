#!/usr/bin/python
#Filename: axx.py
# editando registro de dns bind cambiando serial e ip
import os
import sys
import time

ip1 = "174.129.214.228"
ip2 = "184.72.58.15"

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text


dir_dns = raw_input("Digite la direccion del archivo: ")
dns = open(dir_dns)
archivo = dns.read()

print archivo

serial1 = raw_input("Digite el serial: ")
#serial2 = raw_input("nuevo el serial: ")

if time.strftime("%Y%m%d") == serial1[:8]:
      serial2 = str(int(serial1)+1)
else:
      serial2 = time.strftime("%Y%m%d")+"01"

resultado = replace_all(archivo, {ip1:ip2,serial1:serial2})

dns.close()

dnswrite = open(dir_dns,"w")
dnswrite.write(resultado)
dnswrite.close()

print resultado