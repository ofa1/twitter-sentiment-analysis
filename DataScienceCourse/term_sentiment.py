import sys
import json

scores = {} # initialize an empty dictionary

def getscores(scoringfile):
    for line in scoringfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
#     print scores.items() # Print every (term, score) pair in the dictionary

newwords = {}
def scoretweets(tweet_file):
    for line in tweet_file:
        score = 0
        parsed = json.loads(line)
        
        keys = parsed.keys()
        text = "text"
        
        positive_count = 0.0
        negative_count = 0.0
        
        if(text in keys):
            words =  parsed[text].split()
            for word in words:
                if word.encode("utf-8") in scores.keys():
                    if scores[word] > 0:
                        positive_count += 1
                    else:
                        negative_count += 1
            score = positive_count / (negative_count if negative_count > 0 else 1)
            for word in words:
                if word.encode("utf-8") not in scores.keys():
                    print word.encode("utf-8"), " ",score
        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    getscores(sent_file)
    scoretweets(tweet_file)
    

if __name__ == '__main__':
    main()
