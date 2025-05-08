# import re
#
# def remove_tags(text):
#     newText = re.sub('((<\/\w+>|<\w+>))', '', text)
#     return newText

import re

def remove_tags(text):
    newText = re.sub(r'((<\/\w+>|<\w+>))', '', text)
    return newText

 