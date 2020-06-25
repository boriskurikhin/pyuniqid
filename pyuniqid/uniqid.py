#!/usr/bin/env Python3
import os
import netifaces
import time
from numpy import base_repr

def __get_pid():
    return os.getpid()
def __get_netifaces():
    networkInterfaces = netifaces.interfaces()
    for ni in networkInterfaces:
        nif = netifaces.ifaddresses(ni)
        if ni == 'lo' or netifaces.AF_LINK not in nif:
            continue
        return netifaces.ifaddresses(ni)[netifaces.AF_LINK][0]['addr']
    return '0'
def __get_mac():
    mac = __get_netifaces()
    return int(''.join(list(filter(lambda x: x.isdigit(), list(mac)))))
def __get_time():
    return str(time.time()).replace('.', '')[:13] #js equivalent
def __tob36(item):
    item_int = int(item)
    return base_repr(item_int, 36)
def uniqid(prefix = '', postfix = ''):
    return ''.join(
        [prefix, 
        __tob36(__get_mac()),
        __tob36(__get_pid()),
        __tob36(__get_time()),
        postfix]
    ).lower()
