# -*- coding: utf-8-*-
import re
from imdb import IMDb
import subprocess

WORDS = ["MOVIE"]

def handle(text, mic, profile):

    if 'MOVIE' in text:
        mic.say('What movie do you want me to lookup')
        name = mic.activeListen()
        
        command = '/usr/local/bin/get_first_movie.py "'+name+'"'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        output, error = process.communicate()

        if 'sorry' in output:
            mic.say("sorry, I can't find a movie by that name")
            return

        lst = output.splitlines()
        for l in lst:
            if ('PLOT' in text or 'STORY' in text) and 'Plot' in l:
                mic.say(l)

def isValid(text):
    return bool(re.search(r'\bmovie\b', text, re.IGNORECASE))
