from mad.data import STORIES

def getKeys(number):
    """
    Make set of keys to show to user as hints
    :param number: number of story to select from 
    """

    formatString = STORIES[str(number)]
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1  # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start: end]
        keyList.append(key)  # may add duplicates

    return set(keyList)  # removes duplicates: no duplicates in a set

def tellStory(postData):
    """
    Take the data from as key: userChoice dictionary and 
    format it to story
    :param postData
    """
    dic = {}
    for x in postData:
        dic[x] = postData[x]
    story = STORIES[dic['numberOfStory']].format(**dic)
    return story
    
