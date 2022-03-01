import asyncio
from http import client
from logging import raiseExceptions
from multiprocessing.sharedctypes import Value
import websockets
from uuid import uuid4
from utils import *

#from smartbot import smartbot

similarity_threshold = 0.8
faq_threshold = 0.1
serverIP = '127.0.0.1'
serverPort = 567

bots = []


async def server(ws:str, path:int):
    try:
        cost = 0
        bot, greet, botInst, status = initializeToken(path, bots, ws.remote_address[0])
        if (status == False):
            await ws.send("Something Went Wrong! Please Contact Support")
            raise ValueError("ERROR DISCONNECTION")
        else:
            await ws.send(greet)
        #print(bots)
    
        while True:
            message = await ws.recv()
            reply = processMsg(message) # bot.process_message
            cost += 1
            if reply != "":
                await ws.send(reply)
            #print(f'Msg [{message}]')
    except Exception as e:
        bots.remove(botInst)
        notes = f"Client Disconnected: {botInst} ip {botInst.ip}, remaining {bots} with Status {e} with cost {cost}"
        if cost > 1:
            reportCost(cost, botInst.token, botInst.ip)
        #print(notes)

Server = websockets.serve(server, serverIP, serverPort)

asyncio.get_event_loop().run_until_complete(Server)
asyncio.get_event_loop().run_forever()
