# imports
import json
import datetime

ScriptName = "cotd"
Website = "https://github.com/MilkySalamander/Commands"
Description = "Command to display customizable information about Trackmania's Track of the Day and Cup of the Day"
Creator = "MilkySalamander"
Version = "1.0.0"

def Init():
    return


def Tick():
    return


def TimeUntilCOTD(t):

    # get time offset from t (current time) until 19:00:00 (when cotd starts)
    offset = datetime.datetime(2000,1,1,19,0,0)-t

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


def TrackInfo():

    # create dictionary of track info
    track = {}

    # get the track id of the totd using the tmx api
    track['Id'] = json.loads(Parent.GetRequest('https://trackmania.exchange/mapsearch2/search?api=on&mode=25&limit=1',{}))['response'][23:28]

    # get more detailed information about the totd
    jsonInfo = json.loads(json.loads(Parent.GetRequest('https://trackmania.exchange/api/maps/get_map_info/multi/'+track['Id'],{}))['response'][1:-1])
    
    # put useful information into dictionary
    track['TrackName'] = jsonInfo['Name']
    track['AuthorName'] = jsonInfo['Username']
    track['Difficulty'] = jsonInfo['DifficultyName']
    track['AwardCount'] = str(jsonInfo['AwardCount'])
    track['TmxLink'] = 'https://trackmania.exchange/maps/'+track['Id']

    # reformat author time info and add to track dictionary
    atDecimal = jsonInfo['AuthorTime']%1000
    atSeconds = int(jsonInfo['AuthorTime']/1000)
    atString = ''
    
    # edit author time information if longer than 1 minute
    if atSeconds>59:
        atMinutes=atSeconds//60
        atSeconds%=60
        if atSeconds<10:
            atSeconds='0'+str(atSeconds)
        atString+=str(atMinutes)+':'
    atString+=str(atSeconds)+'.'+str(atDecimal)

    track['AuthorTime'] = atString

    # return track dictionary with useful variables
    return track


def Execute(data):

    # aborts the command if the user types something that isn't '!cotd' 
    if data.GetParam(0) != '!cotd':
        return
    
    # get the current CET time as of the command being called
    currentTime = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
    
    # initialize variables
    countdown = TimeUntilCOTD(currentTime)
    track = TrackInfo()
    stage = ['qualification','knockout'][currentTime.minute>15]


    # COMMAND MESSAGE RESPONSES BEGIN HERE
    # ======================================================================================================
    if currentTime.hour == 19:
        
        # What to display if cotd is in progress
        message = "The current TOTD is '" + track['TrackName'] + "' by " + track['AuthorName'] + " with an author time of " + track['AuthorTime'] + ". COTD " + stage + " stage in progress"
    
    else:
        
        # What to display if cotd is NOT in progress
        message = "The current TOTD is '" + track['TrackName'] + "' by " + track['AuthorName'] + " with an author time of " + track['AuthorTime'] + ". The next COTD starts in " + countdown
    # ======================================================================================================

    Parent.SendStreamMessage(message)
    return