# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:09:24 2021

@author: Administrator
"""
from block import block
class chain:
    def __init__(self):
        self.num = 0
        self.blocks = []
    def verify(self,time,difficult,hashs):
        if(time[0] < time[1]):
            return False
        if(hashs[0] != hashs[1]):
            return False
        return True
    def add(self,block):
        global signal_syncing
        signal_syncing = True
        tmp = block.output()
        if(block.verify()):
            if(self.num == 0):
                self.blocks.append(tmp)
                self.num = self.num + 1
                return True
            tmpp = self.blocks[self.num-1]
            if(self.verify(
                    [tmp["time"],tmpp["time"]],
                    [tmp["difficult"],tmpp["difficult"]],
                    [tmp["prev_hash"],tmpp["self_hash"]])):
                self.blocks.append(tmp)
                self.num = self.num + 1
            else:
                return False
        else:
            return False
        return True
    def remove(self,nums):
        if(nums >= self.num):
            return False
        try:
            self.blocks = self.blocks[0:nums]
        except:
            return False
        finally:
            self.num = nums
    def generate(self,text,difficult):
        global signal_syncing_finished,signal_mining
        if(signal_syncing_finished == False):
            signal_mining = False
            return False
        a = block()
        a.make(self.blocks[self.num-1]["self_hash"],self.num+1)
        signal_mining = True
        a.mining(text,difficult)
        b.add(a)
a = block()
a.make("8000000000000000000000000000000000000000000000000000000000000000",1)
a.mining("你妈没了卧槽去你大爷的",'2')
signal_syncing_finished = True
b = chain()
b.add(a)
print(b.blocks)
b.generate("FUCKYOUBITCH","2")