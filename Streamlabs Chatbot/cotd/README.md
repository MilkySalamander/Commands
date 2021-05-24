# Installation and Customization Instructions

Hello!
This command was designed to generate a customizable message for Trackmania's Cup of the Day, with information about track author, name, author time, and much more. 

## Installing and Configuring Python 2.7
If you don't have python 2.7 installed on your computer, or have never used a custom script with Streamlabs Chatbot, I recommend following the instructions on [this link](https://streamlabs.com/content-hub/post/chatbot-scripts-desktop) for details on how to install and configure python 2.7 for Streamlabs. 


Once this is done, follow the steps below to add the command to your streamlabs chatbot: 

## Installing the Script
1. [Download the cotd.zip file](https://github.com/MilkySalamander/Commands/raw/main/Streamlabs%20Chatbot/cotd/cotd.zip) 
2. Go to the 'Scripts' tab in streamlabs chatbot and click the 'Import' button in the top right.
3. Navigate to the .zip file downloaded earlier and select it
5. Click the 'Reload Scripts' button in the top right, and check the box on the far right to enable the cotd script

## Customize the Command

The command comes loaded with a default message for ease of use, but certain aspects can be customized by clicking on the command in the scripts tab.
Here, you can specify the cooldown of the command (in seconds), and the message to display to the user before, or during the cup of the day.

You will see the default messages in both the 'Displayed Message (during COTD)' and 'Displayed Message (before COTD)' boxes, and they are formatted like this:

```
Some text to display literally {variableName} some more text to display {anotherVariable}
```

**To create your own custom message, you can type any text you would like to appear in the message, but any variables (information that changes with each COTD) must be surrounded in curly brackets: {}**

### Variable Names and Contents
A list of the available variable names and their contents for your convenience:
Variable Name | Example | Description
--------------|---------|------------
{trackName} | MIXTA VIA | The name of the track of the day
{authorName} | Erizel  | The name of the author of the track
{trackTMXLink} | https://trackmania.exchange/maps/26727  | The tmx link to the track of the day (returns "Track not found on TMX" if no link can be found)
{authorTime} | 44.981 | The author time of the track of the day
{goldTime} | 48.000 | The gold medal time of the track of the day
{silverTime} | 54.000 | The silver medal time of the track of the day
{bronzeTime} | 1:08.000 | The bronze medal time of the track of the day
{countdown} | 1 hour 5 minutes 58 seconds | How much time remains before the start of the next cotd
{stage} | Qualification | The current stage of the cotd (will either return 'Qualification' or 'Knockout')

### Premade Examples
Here are some premade examples of what to put in the Displayed Message boxes if you desire a different output, or if you are looking for inspiration:
Text to Copy/Paste | Example Evaluation | Notes
-------------------|--------------------|------
The current TOTD is '{trackName}' by {authorName} with an author time of {authorTime}. COTD {stage} stage in progress! | The current TOTD is 'MIXTA VIA' by Erizel with an author time of 44.981. COTD Qualification stage in progress! | (during COTD), Default
The current TOTD is '{trackName}' by {authorName} with an author time of {authorTime}. The next COTD starts in {countdown} | The current TOTD is 'MIXTA VIA' by Erizel with an author time of 44.981. The next COTD starts in 1 hour 5 minutes 58 seconds | (before COTD), Default
The Track of the Day is {trackName} by {authorName}. Times: 🔰 {authorTime} 🥇 {goldTime} 🥈 {silverTime} 🥉 {bronzeTime}. Don't miss the next COTD in {countdown}! | The Track of the Day is MIXTA VIA by Erizel. Times: 🔰 44.981 🥇 48.000 🥈 54.000 🥉 1:08.000. Don't miss the next COTD in 1 hour 5 minutes 58 seconds! | (before COTD)
The Track of the Day is {trackName} by {authorName}. Times: 🔰 {authorTime} 🥇 {goldTime} 🥈 {silverTime} 🥉 {bronzeTime}. We are in the {stage} stage! | The Track of the Day is MIXTA VIA by Erizel. Times: 🔰 44.981 🥇 48.000 🥈 54.000 🥉 1:08.000. We are in the Qualification stage! | (during COTD)

**If you make any changes to the default options, make sure to click on "Save Settings" to ensure that your changes are reflected in the command.**

If you have any questions or problems at all feel free to email me at MilkySalamander@gmail.com or message me on discord at MilkySalamander#6627

gl hf!
