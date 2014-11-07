import sys
import json
import re

def calculatefrequency(tweets_file):
    frequencies = {}
    total_word_count = 0.0
    for line in tweets_file:
        parsed = json.loads(line)
        keys = parsed.keys()
        text = "text"
        if(text in keys ) and parsed['lang']=='en':
            words =  parsed[text].encode("UTF-8").split()
            for word in words:
                if not re.match("^[A-Za-z0-9]+",word):
                    continue
                total_word_count += 1
                if frequencies.has_key(word):
                    frequencies[word] += frequencies.get(word)
                else:
                    frequencies[word] = 1.0
    for i in frequencies.keys():
        print i,frequencies.get(i)/total_word_count
        
def main():
    tweets_file = open(sys.argv[1])
    calculatefrequency(tweets_file)
    
if __name__ == '__main__':
    main()
