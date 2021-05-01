# Installation and Customization Instructions

### Installing and Configuring Python 2.7
Hello!
This command was designed to generate a customizable message for Trackmania's Cup of the Day, with information about track author, name, author time, and much more. 
If you don't have python 2.7 installed on your computer, or have never used a custom script with Streamlabs Chatbot, I recommend following [this link](https://streamlabs.com/content-hub/post/chatbot-scripts-desktop) for instructions on how to install and configure python 2.7 for Streamlabs. 


Once this is done, you have 2 options: 

### Basic Command
1. You can [download the cotd.zip file](https://github.com/MilkySalamander/Commands/raw/main/Streamlabs%20Chatbot/cotd/cotd.zip), and simply use the 'Import' feature in the streamlabs chatbot scripts tab to install the default commmand.
 
   If you download the cotd.zip file, you should be all set after importing the file into the streamlabs scripts tab. Once you refresh (click the reload scripts button in the top right), don't forget to check the box on the far right to enable the cotd script, and you should be set!

### Customizable Command
2. You can opt to customize the command, and [download the raw cotd_StreamlabsSystem.py file](https://raw.githubusercontent.com/MilkySalamander/Commands/main/Streamlabs%20Chatbot/cotd/cotd_StreamlabsSystem.py) by right-clicking and selecting "Save as".

   If you choose this option, save the file and open it with your text editor of choice (notepad works as well). Once opened, scroll to the very bottom of the file, and look for the area surrounded by equals signs (=). This will be the area you can edit. 
   One of the lines will say "# What to display if cotd is in progress", and the line directly beneath it is the contents of the message. Same follows for the line that says "# What to display if cotd is NOT in progress"

   In order to not break the program, you should surround all of the pure text (messages, punctuation, etc.) in quotation marks (""). When you want to add a variable, end the text you have typed so far with a quotation mark, add a plus sign (+), and then add the variable name you would like to add in that spot. Then add another plus sign (+) and you can continue typing text by opening another quotation mark. 

   Generally, the line should look something like this:  
```python
message = "some text you would like to see in the command" + variableName + "more text" + maybeAnotherVariable + "you get the idea"
```

### Variable Names and Contents
   A list of the available variable names and their contents for your convenience:
Variable Name | Example | Description
--------------|---------|------------
track['TrackName']  | MIXTA VIA | The name of the track of the day
track['AuthorName'] | Erizel  | The name of the author of the track (only displays the first name listed in tmx)
track['Difficulty'] | Intermediate  | The listed difficulty of the track in tmx
track['AwardCount'] | 40  | The number of awards the track has recieved in tmx
track['TmxLink']  | https://trackmania.exchange/maps/26727  | The tmx link to the track of the day
track['AuthorTime'] | 44.981  | The author time of the track of the day
countdown | 1 hour 5 minutes 58 seconds | How much time remains before the start of the next cotd
stage | qualification | The current stage of the cotd (will either return 'qualification' or 'knockout')


   One you have edited these two lines to your liking, save the new cotd_StreamlabsSystem.py file and zip it into a folder titled "cotd.zip".
   Next, navigate to the scripts section of streamlabs chatbot and import your new cotd.zip folder by clicking the 'Import' button in the top right. Once you refresh the scripts (click the reload scripts button in the top right), don't forget to check the box on the far right to enable the cotd script, and you should be set!


If you have any questions at all feel free to email me at MilkySalamander@gmail.com or message me on discord at MilkySalamander#6627

Enjoy!
