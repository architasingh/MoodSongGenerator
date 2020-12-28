# MoodSongGenerator
VIDEO LINK: https://drive.google.com/file/d/1NfdFueA5cUcOHaT2lY9oH8FMfwPTN96T/view?usp=sharing 

Setup
The MoodSongGenerator was written in Python 3.9 OSX and utilizes a PyPi library "lyricsgenius". 
While in most cases pip should be preinstalled, there are rare cases where it must be manually 
installed with a terminal command. Any/all of the following commands should do the trick:

    sudo python3 -m pip install lyricsgenius
    python3 -m pip
        * If this command is used, then a follow-up command "pip install lyricsgenius" is 
        required to install the library.

Following the successful installation of the lyricsgenius module, the sourcecode is ready to 
be pasted and ran in IDLE. 

Installation
The client will need to have the following software installed:
- Python 3.9 Installation: https://www.python.org/downloads/
- Pip Installation: https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3
- LyricsGenius Installation (PyPi): https://pypi.org/project/lyricsgenius/

Usage
Running the MoodSongGenerator from IDLE takes the user to the IDLE shell, where they are prompted
to search for a song with its title and artist. With the LyricsGenius library, the user is able 
to enter however many songs of their choice. All of the songs that the user enters are then 
classified and presented based off of whether they are "happy", "sad", or "unorganized". 

Users may enter either the "done" or "auto" command as well. The "done" command is what initiates
the sorting process and returns the actual lists. The "auto" command showcases the function of the 
program by taking a pre-set bank of songs and organizing them into moods. If the user enters "auto" 
after entering songs of their own, the pre-set songs are added to the list of songs to be organized
and the command initiates the process. 
