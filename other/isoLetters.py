import re
def isoLetters(string1):
    return re.sub('[^a-zA-Z]', '', string1).upper()
