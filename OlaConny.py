#!/usr/bin/python2.7
#-*- coding:utf-8 -*-
import socket
import sys
import time
import os
__author__   = "Gustav Fahlén"

class Bot:
    def __init__(self, ip, port, channel, botnick):
        'Connect to the server and join a channel!'
        
        self.channel = channel
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        print "connecting to: "+ip + ":" + str(port)
        
        self.irc.connect((ip, port))
        self.irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n")
        self.irc.send("NICK "+ botnick +"\n")
        self.irc.send("PRIVMSG nickserv :iNOOPE\r\n")
        self.irc.send("JOIN "+ channel +"\n")
        self.irc.send ( 'PRIVMSG ' + channel  + ' :I welcome you all.\r\n' )
        time.sleep(2)

    def mainLoop(self):
        'Actions that the bot can do :)'
        self.commands = "!Ola-Conny quit, hi Ola-Conny, hello Ola-Conny, fortune, ofreda, Ola-Conny join <channel>, thetime"
        while True:
            self.data = self.irc.recv ( 4096 )
            if self.data.find ( 'PING' ) != -1:
                self.irc.send ( 'PONG ' + self.data.split() [ 1 ] + '\r\n' )
                
            if self.data.find ( '!Ola-Conny quit' ) != -1:
            	self.data = self.data.split(' ')[2]
                self.irc.send ( 'PRIVMSG ' + self.data + ' :Fine, if you don\'t want me\r\n' )
                self.irc.send ( 'QUIT\r\n' )
                break
                
            if self.data.find ( 'hi Ola-Conny' ) != -1:
            	self.data = self.data.split(' ')[2]
                self.irc.send ( 'PRIVMSG ' + self.data + ' :I already said hi...\r\n' )
                
            if self.data.find ( 'hello Ola-Conny' ) != -1:
            	self.data = self.data.split(' ')[2]
                self.irc.send ( 'PRIVMSG ' + self.data + ' :I already said hi...\r\n' )
                
            if self.data.find ( 'KICK' ) != -1:
            	self.data = self.data.split(' ')[2]
                self.irc.send ( 'JOIN ' + self.data +'\r\n' )
                
            if self.data.find ( 'cheese' ) != -1:
            	self.data = self.data.split(' ')[2]
                self.irc.send ( 'PRIVMSG ' + self.data + ' :WHERE!!!!!!\r\n' )
                
            if self.data.find ( 'slaps Ola-Conny' ) != -1:
            	self.data = self.data.split(' ')[2]
                self.irc.send ( 'PRIVMSG ' + self.data + ' :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
                
            if self.data.find ( 'fortune' ) != -1:
                self.line = os.popen("fortune -n 100").read()
                self.data = self.data.split(' ')[2]      
                self.irc.send ( 'PRIVMSG ' + self.data + ' :' + self.line + '\r\n' )

            if self.data.find ( 'ofreda' ) != -1:
                self.offer = self.data.split(':')[ 2 ].replace(':','').split(' ')[1]
                self.offer = self.offer.split("\r\n")[0]
                msg = "BÖG "
                msg2 = "GAY "
                
                for i in range(1,15):
                    self.irc.send ( 'PRIVMSG ' + self.offer + ' :' + msg*i + '\r\n' )
                    
                for k in reversed(range(1,14)):
                    self.irc.send ( 'PRIVMSG ' + self.offer + ' :' + msg2*k + '\r\n' )
                    
            if self.data.find ( 'Ola-Conny join' ) != -1:
                self.data = self.data.split(':')[2]
                self.data = self.data.split(' ')[2]
                self.irc.send ( 'JOIN ' + self.data + '\n' )
                
            if self.data.find ( 'Ola-Conny leave' ) != -1:
                self.irc.send ('QUIT\r\n')
            
            if self.data.find ( 'thetime' ) != -1:
            	self.line = os.popen ( 'date' ).read()
            	self.data = self.data.split(' ')[2]
            	self.irc.send ( 'PRIVMSG ' + self.data + ' :' + self.line + '\r\n' )
            
            if self.data.find ( 'commands' ) != -1:
            	self.data = self.data.split(' ')[2]
            	self.irc.send ( 'PRIVMSG ' + self.data + ' :' + self.commands + '\r\n' )
            print self.data

bot = Bot('127.0.0.1',6667,'#Dev','Ola-Conny')
bot.mainLoop()

