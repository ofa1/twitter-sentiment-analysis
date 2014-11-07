import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

scores = {} # initialize an empty dictionary
inv_states = {v:k for k, v in states.items()}
def getscores(scoringfile):
    for line in scoringfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
#     print scores.items() # Print every (term, score) pair in the dictionary

state_scores = {}
def scoretweets(tweet_file):
    for line in tweet_file:
        score = 0
        parsed = json.loads(line)
        
        keys = parsed.keys()
        if "text" not in keys or "place" not in keys or parsed["place"] == None or parsed["place"]["country_code"] != "US" or parsed["place"]["full_name"] == None:
            continue
        location = parsed["place"]["full_name"].split()
        state = location[len(location)-1]
        
        if state == "USA":
            state = location[0] if "," in location[0] else location[0]+" "+location[1]
            state = state[:len(state) - 1]
            state = inv_states[state]
        
        words =  parsed["text"].split()
        for word in words:
            if word.encode("utf-8") in scores.keys():
                score += scores[word]
        state_scores[state] = score if state not in state_scores.keys() else state_scores[state] + score 
        
    max_sentiment = max(state_scores.itervalues())
    for state, score in state_scores.items():
        if score == max_sentiment:
            print state
            break
        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    getscores(sent_file)
    scoretweets(tweet_file)
    

if __name__ == '__main__':
    main()
