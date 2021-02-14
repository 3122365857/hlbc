# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:09:24 2021

@author: Administrator
"""
import json
import numpy as np
import hashlib
import time
import random
import binascii
class block:
    default_difficult = int(0x00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    max_difficult = int(0x0)
    def __init__(self):
        self.prev_hash,self.time,self.self_hash,self.nonce,self.difficult,self.id=[""]*6
        self.out = {}
    def str_to_hex(self,s):
        b = 0
        for i in range(len(s)-1,0,-1):
            a = s[i]
            a = a.replace('a','10').replace('b','11').replace('c','12').replace('d','13').replace('e','14').replace('f','15')
            b = b + int(a) * (16**(i-1))
        return b
    def make(self,ph,id):
        self.prev_hash = ph
        self.id = id
    def mining(self,text,difficult):
        global signal_mining
        self.text = text
        self.difficult = int(difficult)
        signal_mining = True
        target = self.default_difficult/self.difficult
        target = int(target)
        print(hex(target))
        t_t = time.time()
        t_count = 0
        nonce = 0
        while signal_mining:
            nonce = nonce + 1
            tmp = hashlib.sha256((str(nonce)+self.prev_hash+self.text).encode('utf-8'))
            #tmp = hashlib.sha512(str(tmp).encode('utf-8'))
            tmp = tmp.hexdigest()
            tmp = hashlib.sha256(str(tmp).encode('utf-8'))
            tmp = tmp.hexdigest()
            t_count = t_count + 1
            if(time.time()>t_t+4):
                print("挖矿速度： "+str(t_count/4)+"H/s")
                t_count = 0
                t_t = time.time()
            if(self.str_to_hex(tmp) <= target):
                self.nonce = nonce
                self.self_hash = tmp
                break
        print("挖矿成功，正在生成区块")
    def output(self):
        a = {}
        try:
            a["id"] = self.id
            a["prev_hash"] = self.prev_hash
            a["nonce"] = self.nonce
            a["time"] = int(time.time())
            a["text"] = self.text
            a["self_hash"] = self.self_hash
            a["difficult"] = self.difficult
            self.out = a
            a["error"] = 0
            return a
        except:
            return {"error":1}
    def write(self,p,t,s,n,d,i):
        self.prev_hash,self.time,self.self_hash,self.nonce,self.difficult,self.id=[p,t,s,n,d,i]
    def verify(self):
        if(self.output()["error"] == 1):
            return False
        nonce = self.nonce
        prev_hash = self.prev_hash
        text = self.text
        self_hash = self.self_hash
        difficult = self.difficult
        target = self.default_difficult/self.difficult
        target = int(target)
        tmp = hashlib.sha256((str(nonce)+prev_hash+text).encode('utf-8'))
        #tmp = hashlib.sha512(str(tmp).encode('utf-8'))
        tmp = tmp.hexdigest()
        tmp = hashlib.sha256(str(tmp).encode('utf-8'))
        tmp = tmp.hexdigest()
        if(tmp == self_hash and self.str_to_hex(tmp) <= target):
            return True
        return False
#class chain:
    #self.block = 
a = block()
a.make("8000000000000000000000000000000000000000000000000000000000000000",0)
a.mining("你妈没了卧槽去你大爷的",'4')
print(a.output())

b = a.output()["self_hash"]
c = block()
c.make(b,1)
c.mining("fuckkckck",'4')
print(c.output())


    
