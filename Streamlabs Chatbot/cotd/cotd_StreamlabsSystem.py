# imports
import sys
import os
import codecs
import json
import re
import datetime

# get current working directory and add to path
workDir = os.path.dirname(__file__)
sys.path.append(workDir)
import pytz

ScriptName = "cotd"
Website = "https://github.com/MilkySalamander/Commands/tree/main/Streamlabs%20Chatbot/cotd"
Description = "Command to display customizable information about Trackmania's Track of the Day and Cup of the Day"
Creator = "MilkySalamander"
Version = "2.0.0"
Command= "!cotd"

settings = {}

def Init():
    global settings

    # retrieve settings from user
    with codecs.open(os.path.join(workDir, "settings.json"), encoding='utf-8-sig') as jsonFile:
        settings = json.load(jsonFile, encoding='utf-8-sig')
    return

def Tick():
    return

def SendMessage(message):
    Parent.SendStreamMessage(message)
    return

def TimeUntilCOTD(cetTime):

    #calculate time until 19:00:00 (when cotd starts)
    offset = pytz.timezone('Europe/Paris').localize(datetime.datetime(cetTime.year,cetTime.month,cetTime.day+[0,1][cetTime.hour>=19],19,0,0))-cetTime
    
    # extract hours, minutes, and seconds from calculated time until cotd 
    h, m, s = offset.seconds//3600, (offset.seconds%3600)//60, ((offset.seconds%3600)%60)
    
    # format countdown data as text string
    text=''
    if h>0:
        text+='{} hour{} '.format(h,['s',''][h==1])
    if m>0:
        text+='{} minute{} '.format(m,['s',''][m==1])
    if s>0:
        text+='{} second{}'.format(s,['s',''][s==1])
    
    #remove extra whitespace
    text.strip()

    #return time string
    return text

def FormatTime(ms):
    atDecimal = ms%1000
    atSeconds = ms/1000
    atString = ''
    
    # edit time information if longer than 1 minute
    if atSeconds>59:
        atMinutes=atSeconds//60
        atSeconds%=60
        if atSeconds<10:
            atSeconds='0'+str(atSeconds)
        atString+=str(atMinutes)+':'
    atString+=str(atSeconds)+'.'+str(atDecimal).rjust(3,'0')

    return atString

def TrackInfo():
    # get the track information using the trackmania.io api
    trackJSON = json.loads(json.loads(Parent.GetRequest('https://trackmania.io/api/totd/0',{}))['response'])['days'][-1]
    
    # get useful information about the track and set variables
    # trackname (using regex to escape color codes and formatting) thanks to Solux for the regex
    trackName = trackJSON['map']['name']
    trackRegexMatches = re.finditer(r"(?i)(?<!\$)((?P<d>\$+)(?P=d))?((?<=\$)(?!\$)|(\$([a-f\d]{1,3}|[ionmwsztg<>]|[lhp](\[[^\]]+\])?)))",trackName,re.MULTILINE)
    for match in trackRegexMatches:
        trackName=trackName.replace(match.group(),'')
    # track tmx link (If it exists)
    trackTMXID = str(trackJSON['map']['exchangeid'])
    trackTMXLink = "https://trackmania.exchange/maps/"+trackTMXID
    if trackTMXID=="0":
        trackTMXLink = "Track not found on TMX"
    # track author name
    authorName = trackJSON['map']['authordisplayname']
    # track author time
    authorTime = FormatTime(trackJSON['map']['authorScore'])
    # track gold time
    goldTime = FormatTime(trackJSON['map']['goldScore'])
    # track silver time
    silverTime = FormatTime(trackJSON['map']['silverScore'])
    # track bronze time
    bronzeTime = FormatTime(trackJSON['map']['bronzeScore'])
        

    # return track data as dictionary
    return {"trackName":trackName, "trackTMXLink":trackTMXLink, "authorName":authorName, "authorTime":authorTime, "goldTime":goldTime, "silverTime":silverTime, "bronzeTime":bronzeTime}

def Execute(data):

    # aborts the command if the user types something that isn't '!cotd'  or the commmand is on cooldown
    if data.GetParam(0) != Command or Parent.IsOnCooldown(ScriptName, Command):
        return
    
    # get the current CET time as of the command being called
    currentTime = datetime.datetime.now(pytz.timezone('Europe/Paris'))

    # create main dictionary
    mainDictionary = TrackInfo()
    mainDictionary["countdown"] = TimeUntilCOTD(currentTime)
    mainDictionary["stage"] = ['Qualification','Knockout'][currentTime.minute>15]

    # command message responses
    if currentTime.hour == 19:
        
        # What to display if cotd is in progress
        message = settings['messageDuringCOTD'].format(**mainDictionary)
    
    else:
        
        # What to display if cotd is NOT in progress
        message = settings['messageBeforeCOTD'].format(**mainDictionary)

    # ======================================================================================================

    # send final message in chat
    SendMessage(message)
    
    # create a command cooldown for the user-specified amount of seconds
    Parent.AddCooldown(ScriptName, Command, settings['commandCooldown'])
    return
