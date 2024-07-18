import re
import unicodedata

def camel_to_snake(text):
    text = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()

def normalize(text):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')

def replace_last(string1, new_string):
    return string1[:-len(new_string)] + new_string