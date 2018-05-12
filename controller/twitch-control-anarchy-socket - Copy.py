#!/usr/bin/env python3
import argparse
import serial
from time import sleep
import pynput
import pyautogui
import win32api
import win32con

# for time delaying the input:
from threading import Timer
import time
from math import sqrt

# switch controller:
from switchcontroller.switchcontroller import *

# twitch:
from twitchbot.twitchbot import *

# for time delaying the input:
from threading import Timer

# for socketio
from socketIO_client_nexus import SocketIO, LoggingNamespace, BaseNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

from threading import Thread


screenWidth, screenHeight = pyautogui.size()
x = screenWidth/2
y = screenHeight/2
prevX = 0
prevY = 0

controller = SwitchController()
controller.connect("COM6")

twitchBot = TwitchBot()
twitchBot.connect(HOST, PASS2, PORT, CHAN, NICK2)

# start = time.clock()
# botstart = time.clock()

def delayed_reset(delay=0.1):
	Timer(delay, controller.reset).start()


def accurateSleep(duration):
	s = time.clock()
	e = time.clock()

	diffInSeconds = 0
	diffInMilliSeconds = 0

	while (diffInMilliSeconds < duration):
		e = time.clock()
		diffInSeconds = e - s
		diffInMilliSeconds = diffInSeconds*1000

def send_and_reset(duration=0.1, reset=1):
	controller.getOutput()
	controller.send(controller.output)
	sleep(duration)
	if(reset):
		controller.reset()
		controller.getOutput()
		controller.send(controller.output)

validCommands = ["lockon", "hhsprint", "hsprint", "sprint", "!controls", "home", "lstick", "rstick", "spin", "swim", "back flip", "ground pound", "groundpound", "gp", "bf", "cap bounce", "sdive", "sdive2", "hdive", "hdive2", "hdive3", "dive", "dive2", "dive3", "roll", "roll2", "backflip", "backflip2", "sssu", "sssd", "sssl", "sssr", "sb", "suu", "", "up", "down", "left", "right", "u", "d", "l", "r", "hup", "hdown", "hleft", "hright", "hhup", "hhdown", "hhleft", "hhright", "hu", "hd", "hl", "hr", "su", "sd", "sl", "sr", "sup", "sdown", "sleft", "sright", "ssu", "ssd", "ssl", "ssr", "ssup", "ssdown", "ssleft", "ssright", "look up", "look down", "look left", "look right", "lu", "ld", "ll", "lr", "hlu", "hld", "hll", "hlr", "slu", "sld", "sll", "slr", "dup", "ddown", "dleft", "dright", "du", "dd", "dl", "dr", "a", "b", "x", "y", "ha", "hb", "hx", "hy", "hhb", "hhhb", "l", "zl", "r", "zr", "plus", "minus", "long jump", "long jump2", "long jump3", "jump forward", "jump forward2", "jump back", "jump back2", "dive", "dive2"]
whitelist = ["beanjr_yt", "yanchan230", "silvermagpi", "hoopa21", "opprose", "mrruidiazisthebestinsmo", "stravos96", "harmjan387", "twitchplaysconsoles", "fosseisanerd"]
adminlist = ["twitchplaysconsoles", "fosseisanerd"]

commandQueue = []
nextCommands = []


def on_ping2(*args):
	print("test")









class Client(object):

	def on_event(self, event):
		print(event)

	def on_controller_state(*args):
		print("controller state:", args)

		controller.reset()

		inputs = args[1].split()

		btns = inputs[0]
		LX = inputs[1]
		LY = inputs[2]
		RX = inputs[3]
		RY = inputs[4]

		controller.dpad = int(btns[0])
		if (btns[1] == '1'):
			controller.lclick = 1;
		if (btns[2] == '1'):
			controller.l = 1;
		if (btns[3] == '1'):
			controller.zl = 1;
		if (btns[4] == '1'):
			controller.minus = 1;
		if (btns[5] == '1'):
			controller.capture = 1;
		if (btns[6] == '1'):
			controller.a = 1;
		if (btns[7] == '1'):
			controller.b = 1;
		if (btns[8] == '1'):
			controller.x = 1;
		if (btns[9] == '1'):
			controller.y = 1;
		if (btns[10] == '1'):
			controller.rclick = 1;
		if (btns[11] == '1'):
			controller.r = 1;
		if (btns[12] == '1'):
			controller.zr = 1;
		if (btns[13] == '1'):
			controller.plus = 1
		if (btns[14] == '1'):
			controller.home = 1

		controller.LX = int(LX)
		controller.LY = 255-int(LY)
		controller.RX = int(RX)
		controller.RY = 255-int(RY)


		duration = 0
		reset = 0
		send_and_reset(duration, reset)



	def loop(self):
		return





	def __init__(self):
		self.socketio = SocketIO("http://fosse.co:8110")
		self.socketio.on("controllerState", self.on_controller_state)
		self.socketio.emit("IamController")

		self.receive_events_thread = Thread(target=self._receive_events_thread)
		self.receive_events_thread.daemon = True
		self.receive_events_thread.start()

		self.start = time.clock()
		self.end = time.clock()
		
		self.botstart = time.clock()
		self.botend = time.clock()

		while True:

			#self.loop()

			# so I don't get stuck:
			if(win32api.GetAsyncKeyState(win32con.VK_ESCAPE)):
				controller.send('RELEASE')
				controller.ser.close()
				exit()

	def _receive_events_thread(self):
		self.socketio.wait()

Client()

























