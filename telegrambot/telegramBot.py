import telebot
import sys
sys.path.append('../web/carontepass/')
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carontepass.settings")
import django
django.setup()
from carontepass.settings_local import TOKEN_BOT
from access.models import Log



commands = {  # command description used in the "help" command
              'start': 'Get used to the bot',
              'help': 'Gives you information about the available commands',
              'status': 'Know if the space is open or closed',
              'users_in': 'List of people inside the space',
              'open': 'Open Door'
}

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts


# only used for console output now
#def listener(messages):
   # for m in messages:
       # if m.content_type == 'text':
            # print the sent message to the console
            #print str(m.chat.first_name).encode('utf-8') + " [" + str(m.chat.id).encode('utf-8') + "]: " + m.text
            

bot = telebot.TeleBot(TOKEN_BOT)
#bot.set_update_listener(listener)  # register listener


# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hello, stranger, let me scan you...")
        msg = "Scanning complete, I know you now. Chatid: " + str(cid)
        bot.send_message(cid, msg)
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "I already know you, no need for me to scan you again!")


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page
    
  
# status page
@bot.message_handler(commands=['status'])
def command_status(m):
    cid = m.chat.id
    if Log.listUsersCount() > 0:
        bot.send_message(cid, "Site Open")
    else:
        bot.send_message(cid, "Site Closed")
        
        
# users_in page
@bot.message_handler(commands=['users_in'])
def command_users_in(m):
    cid = m.chat.id
    users_in = Log.listUsersInside()
    bot.send_message(cid, users_in) 
    
    
# open door page
@bot.message_handler(commands=['open'])
def command_open(m):
    cid = m.chat.id
    bot.send_message(cid, "Not implemented") 


bot.polling(none_stop=True)


