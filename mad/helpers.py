from django.http import request
from mad.data import A

def getKeys(number):
    '''formatString is a format string with embedded dictionary keys.
    Return a set containing all the keys from the format string.'''

    formatString = A[str(number)]
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1  # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start: end]
        keyList.append(key)  # may add duplicates

    return set(keyList)  # removes duplicates: no duplicates in a set


def addPick(cue, dictionary):  # from madlib.py
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    promptFormat = "Enter a specific example for {name}: "
    # hint = cue.split('::')
    # hint = '('.join([hint[0], a[hint[1]]]) + ')'

    prompt = promptFormat.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response


def getUserPicks(cues):
    '''Loop through the collection of cue keys and get user choices.
    Return the resulting dictionary.
    '''
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks


def tellStory(postdata):
    '''storyFormat is a string with Python dictionary references embedded,
    in the form {cue}.  Prompt the user for the mad lib substitutions
    and then print the resulting story with the substitutions.
    '''
    dic = {}
    for x in postdata:
        dic[x] = postdata[x]
    story = A[dic['numberOfStory']].format(**dic)
    return story
    
