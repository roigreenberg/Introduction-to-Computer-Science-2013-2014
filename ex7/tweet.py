#############################################################
# FILE: tweet.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex7 2013-2014
# Description: implement a new class of Tweets.
#              tweet contain text, time and position 
# coordinate(latitude and longitude)
# the method of the tweet are get.word - return a list
# containing only the words converting to lower-case char
# get_location - return the position of the tweet
# get_sentiment - return the sentiment value of the tweet
#############################################################

from doctest import run_docstring_examples
from geo import Position

class Tweet:
    def __init__(self, text, time, lat, lon):
        self.__text=text
        self.__time=time
        self.__lat=lat
        self.__lon=lon
        
    def get_words(self):
        """Return the words in a tweet, not including punctuation.
        """
        import re
        # create a list containing only the words converting to lower-case char
        word_list=re.sub("[^a-zA-Z]", " ", self.__text.lower()).split()
        return word_list

    def get_text(self):
        """Return the text of the tweet."""
        return self.__text

    def get_time(self):
        """Return the datetime that represents when the tweet was posted."""
        return self.__time

    def get_location(self):
        """Return a position (see geo.py) that represents the tweet's location."""
        return Position(self.__lat,self.__lon)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.get_text() == other.get_text() and
                    self.get_location() == other.get_location() and
                    self.get_time() == other.get_time())
        else:
            return False

    def __str__(self):
        """Return a string representing the tweet."""
        return '"{0}" @ {1} : {2}'.format(self.get_text(), 
                                          self.get_location(), 
                                          self.get_time())

    def __repr__(self):
        """Return a string representing the tweet."""
        return 'Tweet({0}, {1}, {2}, {3})'\
               .format(*map(repr,(self.get_text(),
                                  self.get_time(),
                                  self.get_location().latitude(),
                                  self.get_location().longitude())))

    def get_sentiment(self,word_sentiments):
        """ Return a sentiment representing the degree of positive or negative
        sentiment in the given tweet, averaging over all the words in the tweet
        that have a sentiment value.
        """
        # get only the words from the tweet
        words=self.get_words()
        # set the variables
        total_sentiment=0.
        count=0
        # run for every word
        for word in words:
            # if word had sentiment value raise the counter and add the
            # the sentiment value to total_sentimet
            if word in word_sentiments.keys():
                count += 1
                total_sentiment += word_sentiments[word]
                
        return None if count == 0 else total_sentiment/count

