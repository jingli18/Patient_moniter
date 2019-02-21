#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

'''
Create on 02/10/2019
@author: Zhangyu Wan
I use new version of alert system module modified by XiangKun Ye
'''

'''
Created on 02/10/2019
@author: Xiangkun Ye
Source code copied from https://github.com/alexlin0625/EC500_Spring19/blob/alert-system/alert_system.py.
With lots of modifications to make it work.
Basically I rewrited the whole file.
The original one by mohitbeniwal is bullshit.
'''

"""
Created on Wed Feb  6 09:29:32 2019

@author: mohitbeniwal
"""


def alertCheck(j_o):
    j=json.loads(j_o)
    alert_message=""

    
    if(j["bloodPressure"]<j["pressureRange"]["lower"]):
        alert_message+="BloodPressure is Too low, "
    elif(j["bloodPressure"]>j["pressureRange"]["upper"]):
        alert_message="BloodPressure is Too high, "
    if(j["pulse"]<j["pulseRange"]["lower"]):
        alert_message+="Pulse is Too low, "
    elif(j["pulse"]>j["pulseRange"]["upper"]):
        alert_message+="Pulse is Too high, "
    if(j["bloodOx"]<j["oxRange"]["lower"]):
        alert_message+="BloodOx is Too low, "
    elif(j["bloodOx"]>j["oxRange"]["upper"]):
        alert_message+="BloodOx is Too high, "
    return alert_message
