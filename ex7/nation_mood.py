#############################################################
# FILE: nation_mood.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex7 2013-2014
# Description: implement some function that
# 1. most_talkative_state: find the most talkative state
# 2. average_sentiments: create a dictionary from state to
#    average of the tweets  sentiments
# 3. group_tweets_by_hour: create a list of lists of hours
#    so that every list contain the tweet that sent in the
#    same hour
#############################################################

from data import load_tweets
from geo_tweet_tools import group_tweets_by_state,find_closest_state,find_center
from geo import us_states, Position
from tweet import Tweet

def most_talkative_state(tweets,find_state):
    """Return the state that has the largest number of tweets containing term.
    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> tweets = load_tweets('texas')
    >>> find_state = find_closest_state(state_centers);
    >>> most_talkative_state(tweets,find_state)
    'TX'
    >>> tweets = load_tweets('sandwich')
    >>> most_talkative_state(tweets,find_state)
    'NJ'
    """
    # create a dictionary of states to tweets
    tweets_by_state=group_tweets_by_state(tweets,find_state)

    # if no tweets with sentiment value
    if not tweets_by_state:
        return None
    # create an empty list
    states=[]
    # run for every tweet
    for tweet_with_state in tweets_by_state.items():
        # ammount of tweets in the state
        ammount_tweets=len(tweet_with_state[1])
        # the state code name
        state_name=tweet_with_state[0]
        # add the ammount and name as a tuple to the list
        states.append((ammount_tweets, state_name))
    # take the name of the state with the highest ammount of tweets
    state=max(states)[1]
    
    return state

def average_sentiments(tweets_by_state,word_sentiments):
    """Calculate the average sentiment of the states by averaging over all
    the tweets from each state. Return the result as a dictionary from state
    names to average sentiment values (numbers).

    If a state has no tweets with sentiment values, leave it out of the
    dictionary entirely.  Do NOT include states with no tweets, or with tweets
    that have no sentiment, as 0.  0 represents neutral sentiment, not unknown
    sentiment.

    tweets_by_state -- A dictionary from state names to lists of tweets
    """
    # create an empty dictionary
    state_average={}

    # run for every state
    for state in tweets_by_state.items():
        # set the variables
        total_sentiment=0
        count=0
        tweet_sentiment=None
        
        # the state code name
        state_name=state[0]
        # the tweets list
        tweets=state[1]
        
        # run for every tweet
        for tweet in tweets:
            # recieve the sentiment of the tweet
            tweet_sentiment=tweet.get_sentiment(word_sentiments)
            # add the tweet sentiment to the total sentiment if
            # it not None and raise the counter
            if tweet_sentiment!=None:
                count +=1
                total_sentiment+=tweet_sentiment
        # add the state to the dictionary if any tweet had sentiment value
        if count != 0:
            state_average[state_name]=total_sentiment/count
    return state_average

    

def group_tweets_by_hour(tweets):
    """Return a list of lists of tweets that are gouped by the hour 
    they were posted.

    The indexes of the returned list represent the hour when they were posted
    - the integers 0 through 23.

    tweets_by_hour[i] is the list of all
    tweets that were posted between hour i and hour i + 1. Hour 0 refers to
    midnight, while hour 23 refers to 11:00PM.

    To get started, read the Python Library documentation for datetime 
    objects:
    http://docs.python.org/py3k/library/datetime.html#datetime.datetime

    tweets -- A list of tweets to be grouped
    """
    # create list of 24 empty lists
    HOURS=24
    hours_list=[[] for hour in range(HOURS)]

    # run for every tweet
    for tweet in tweets:
        # put the tweet in the list of hours in the 
        hours_list[tweet.get_time().hour].append(tweet)
    return hours_list

