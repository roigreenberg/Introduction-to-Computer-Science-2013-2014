#####################################################################
# FILE: geo_tweet_tools.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex7 2013-2014
# Description: implement some function about polygon and tweets:
#     1. find_centroid: calculate the centeroid and area of polygon
#     2. find_center:  calculate the center of several polygons
#     3. find_closest_state: find the closest state to the tweet
#     4. find_containing_state: find the state containing the tweet
#     5. group_tweets_by_state: create a dictionary that group
#        tweets by  their state as key
######################################################################

from geo import us_states, Position
from tweet import Tweet
    
def find_centroid(polygon):
    """Find the centroid of a polygon.

    http://en.wikipedia.org/wiki/Centroid #Centroid_of_polygon

    polygon -- A list of positions, in which the first and last are the same

    Returns: 3 numbers; centroid latitude, centroid longitude, and polygon area

    Hint: If a polygon has 0 area, return its first position as its centroid

    >>> p1, p2, p3 = Position(1, 2), Position(3, 4), Position(5, 0)
    >>> triangle = [p1, p2, p3, p1]  # First vertex is also the last vertex
    >>> find_centroid(triangle)
    (Position(3.0, 2.0), 6.0)
    >>> find_centroid([p1, p3, p2, p1])
    (Position(3.0, 2.0), 6.0)
    >>> find_centroid([p1, p2, p1])
    (Position(1.0, 2.0), 0)
    """
    # calculate the area
    area=0.5 * (sum(polygon[i].latitude() * polygon[i+1].longitude()\
              - polygon[i + 1].latitude() * polygon[i].longitude() \
                  for i in range(len(polygon) - 1)))
    # return the first position if area is 0
    if not area:
        return Position(polygon[0].latitude(), polygon[0].longitude()),0

    # calclate the centroid latitude
    latitude=(1 / (6 * area)) * sum((polygon[i].latitude() + \
                               polygon[i + 1].latitude()) * \
              (polygon[i].latitude() * polygon[i+1].longitude() - \
               polygon[i + 1].latitude() * polygon[i].longitude())\
                  for i in range(len(polygon)-1))
    # calclate the centroid logitude
    longitude=(1 / (6 * area)) * sum((polygon[i].longitude() + \
                                polygon[i + 1].longitude()) * \
              (polygon[i].latitude() * polygon[i + 1].longitude() - \
               polygon[i + 1].latitude() * polygon[i].longitude())\
                  for i in range(len(polygon)-1))
    
    return Position(latitude,longitude),abs(area)

def find_center(polygons):
    """Compute the geographic center of a state, averaged over its polygons.

    The center is the average position of centroids of the polygons in polygons,
    weighted by the area of those polygons.

    Arguments:
    polygons -- a list of polygons

    >>> ca = find_center(us_states['CA'])  # California
    >>> round(ca.latitude(), 5)
    37.25389
    >>> round(ca.longitude(), 5)
    -119.61439

    >>> hi = find_center(us_states['HI'])  # Hawaii
    >>> round(hi.latitude(), 5)
    20.1489
    >>> round(hi.longitude(), 5)
    -156.21763
    """

    # calclate the latitude
    latitude=sum(find_centroid(polygon)[0].latitude() * \
                 find_centroid(polygon)[1] for polygon in polygons)\
           /(sum(find_centroid(polygon)[1] for polygon in polygons))
    # calclate the longitude
    longitude=sum(find_centroid(polygon)[0].longitude() * \
                  find_centroid(polygon)[1] for polygon in polygons) / \
                  sum(find_centroid(polygon)[1] for polygon in polygons)
    
    return Position(latitude,longitude)


def find_closest_state(state_centers):
    import geo
    """Returns a function that takes a tweet and returns the name of the state 
    closest to the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    state_centers -- a dictionary from state names to positions.

    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> nj = Tweet("Welcome to New Jersey", None, 41.1, -74)
    >>> find_state = find_closest_state(state_centers)
    >>> find_state(sf)
    'CA'
    >>> find_state(nj)
    'NJ'
    """
    
    def find_state(tweet):
        """the function takes a tweet and returns the name of the state 
        closest to the given tweet's location.

        Argumente:
        tweet- a tweet abstract data type"""
        # calculate the distances between the tweet position and the states
        # centers and take the shortest distance
        closest_state=min([(geo.geo_distance(tweet.get_location(),\
                                 state_centers[state]),state)\
               for state in state_centers])
        # return the name of tShe state
        return closest_state[1]
  
    return find_state



def find_containing_state(states):
    """Returns a function that takes a tweet and returns the name of the state 
    containing the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    us_states -- a dictionary from state names to positions.

    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> ny = Tweet("Welcome to New York", None, 41.1, -74)
    >>> find_state = find_containing_state(us_states)
    >>> find_state(sf)
    'CA'
    >>> find_state(ny)
    'NY'
    """
    def find_state(tweet):
        """the function takes a tweet and returns the name of the state 
        contain the given tweet's location.

        Argumente:
        tweet- a tweet abstract data type"""

        # get latitude and longitude of the tweet
        t_lat=tweet.get_location().latitude()
        t_lon=tweet.get_location().longitude()

        # run for every state
        for state in states:
            # set inside to False
            inside=False
            # set polygon as the list of state positions
            polygon=states[state][0]
            # number of positions in state
            num=len(polygon)
            # take the first position
            lat_1,lon_1=polygon[0].latitude(),polygon[0].longitude()
            # run for every position
            for pol in range(num):
                # set the next position
                lat_2=polygon[pol].latitude()
                lon_2=polygon[pol].longitude()
                # check if the tweet position cross the line between
                # the positions we check 
                if min(lon_1,lon_2) < t_lon <= max(lon_1,lon_2):

                    if t_lat <= max(lat_1,lat_2):
                        if lon_1 != lon_2:
                            lat_in_pol = (t_lon-lon_1) * (lat_2-lat_1) / \
                                    (lon_2-lon_1) + lat_1
                        # if cross, change the state of inside
                        if lat_1 == lat_2 or t_lat <= lat_in_pol:
                            inside = not inside
                # set the first position as the next one
                lat_1,lon_1 = lat_2,lon_2
            # if tweet inside state return the state name
            if inside == True:
                return state

    return find_state

def group_tweets_by_state(tweets,find_state):
    """Return a dictionary that aggregates tweets by their nearest state center.

    The keys of the returned dictionary are state names, and the values are
    lists of tweets that appear closer to that state center than any other.

    tweets -- a sequence of tweet abstract data types

    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> find_state = find_closest_state(state_centers);
    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> ny = Tweet("Welcome to New York", None, 41, -74)
    >>> ca_tweets = group_tweets_by_state([sf, ny],find_state)['CA']
    >>> ca_tweets
    [Tweet('Welcome to San Francisco', None, 38, -122)]
    """
    # create an empty dictionary
    tweets_by_state={}
    # run for every tweet
    for tweet in tweets:
        # recieve the tweet state
        state=find_state(tweet)
        # add new state to dictionary if not exist
        if state not in tweets_by_state.keys():
            # set the value as the tweet
            tweets_by_state[state]=[tweet]
        # add the tweet to the state key if alredy exist
        else:
            tweets_by_state[state].append(tweet)
        
    return tweets_by_state
