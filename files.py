# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:09:24 2021

@author: Administrator
"""
import os
import numpy as np
class file:
    def __init__(self):
        self.file_name = ""
    def set_file(self,name):
        self.file_name = name
        return
    def read_file(self,chain):
        try:
            chain.blocks = np.load(self.file_name+"HL.dat", allow_pickle=True)
        except:
            print("文件读写出错")
            return False
        finally:
            return True
    def write_file(self,chain):
        try:
            name = self.file_name + "HL"
            np.save(name,chain.blocks, allow_pickle=True)
            os.remove(name+".dat")
            os.rename(name+".npy",name+".dat")
        except:
            print("文件写入出错")
            return False
        finally:
            return True

            
        