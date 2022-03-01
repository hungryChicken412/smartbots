import requests
import json
#import smartbot from smartbot
url = "http://localhost:8000/api"
url2 = "http://localhost:8000/costRegistration/"

class BotInstance:
    def __init__(self, bot, token, ip):
        self.bot = bot
        self.token = token
        self.ip = ip
        
def initializeToken(token, dict, Userip):
    greet, context, questions, status = getInformationFromDjangoDB(token)
    bot = "ok" #smartbot(questions, context, similarity_threshold,faq_threshold)
    botInst = BotInstance(bot, token, Userip)
    dict.append(botInst)
    
    return bot, greet, botInst, status

def closeConnection(bots, botInstance:BotInstance, e:Exception):
    bots.remove(botInstance)
    notes = f"Client Disconnected: {botInstance} ip {botInstance.ip}, remaining {bots} with Exception  {e}"

    print(notes)

def getInformationFromDjangoDB(token):
    try:         
        data = requests.get(url+token)
        content = data.json()[0]
        questions = content["faqs"]
        context = content["context"]
        greet = content["greeting"]#context#"WELCOME TO THE CHAT GUYS <DIVIDER> OPTION 1 <OPTION> OPTION 2 <OPTION> OPTION 3"
        status = True
            
            
        return greet, context, questions, status
    except Exception as e:
        status = False
        error = f"something went wrong with Exception {e}, Please contact support"
        return error, error, error, status
        
def processMsg(message): 
    
    reply = ""
    if message == "hi":
        reply = "how are you man?"
    elif message == "fine":
        reply = "that's cool"
    elif message == "cool":
        reply = "noiece"

    return reply

def reportCost(cost, token, ip):
    data = {
        'cost':cost,
        'token':token,
        'ip': ip,
        'auth':'123',
    }
    requests.post(url2, data=data)



'''
testContext = """Vavecorp is a webdevelopment agency. 
We provide website solutions. Vavecorp charges depending on the job. 
Contact us not at our email: contact@vavecorp.com
Our engineers are experts and will be able to help you.
We help you shape and manage your entire IT Eco-system!
We create everything from a simple landing page to a GIANT E-commerce, 
we provide a wide range services covering nearly every aspect of the "internet" side of your business, 
We Help you in expanding your business to new horizons! unlock new levels of your potential and enjoy unlimited growth
We take care of your websites for you
"""


questions = ["How much do you guys charge?", 
    "what is your name?", 
    "What is the pricing?",
    "How long does a project take?",
    ]
questionDict = {"How much do you charge?":"We charge around 100$ per site on a landing page, contact us on our email for more info.",
    "what is your name?":"I'm a smartbot agent working for Vavecorp", 
    "What is the pricing?":"Pricing depends on the project we take on",
    "How long does a project take?":"a project takes around 1 week to complete, but we can work faster too",
    }


greet = "Welcome to Vavecorp Customer Support!\n I am a smartbot agent, how may I help you? <DIVIDER> How much do you guys charge? <OPTION> what is your name? <OPTION> What is the pricing? <OPTION> How long does a project take?"

'''
