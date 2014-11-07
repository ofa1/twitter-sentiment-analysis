import sys
import json
import re
import collections

def top_ten(tweets_file):
    frequencies = collections.defaultdict(int)
    total_word_count = 0.0
    for line in tweets_file:
        parsed = json.loads(line)
        keys = parsed.keys()
        if "text" not in keys or "entities" not in keys or "hashtags" not in parsed["entities"] or parsed["entities"]["hashtags"] == []:
            continue
        hashtags = parsed["entities"]["hashtags"]
        for hashtag in hashtags:
            text = hashtag["text"]
            frequencies[text] += 1 
    count = 0
    for w in sorted(frequencies, key=frequencies.get, reverse=True):
        print w.encode("utf-8"), frequencies[w]
        count += 1
        if count is 10 : break

def main():
    tweets_file = open(sys.argv[1])
    top_ten(tweets_file)
    
if __name__ == '__main__':
    main()
