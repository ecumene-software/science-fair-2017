from articles import *
import numpy as np

class Tweet():
    def __init__(self, creator, person, projretweets, monthsage):
        self.creator = creator
        self.person = person
        self.projretweets = projretweets
        self.monthsage  = monthsage
    def to_arr(self):
        return  np.array([self.creator.subs, self.creator.views,
            self.person.dayinterest30, self.person.dayinterestyear,
            self.projretweets, self.monthsage], np.int64)

class TweetResponse():
    def __init__(self, likes, replies):
        self.likes = likes
        self.replies = replies
    def to_arr(self):
        return np.array([self.likes, self.replies], np.int64)

tw_namedrop = {
    Tweet(FANTANO,    KENYE,     10,11):TweetResponse(68, 3),
    Tweet(TMZ,        KENYE,   2119, 1):TweetResponse(2800, 395),
    Tweet(TMZ,        TRUMP,   2119, 1):TweetResponse(2800, 395),
    Tweet(CNN,        TRUMP,   1076, 2):TweetResponse(1112, 1300),
    Tweet(TRUMPSHILL, TRUMP,   4447, 3):TweetResponse(26999, 1700),
    Tweet(TRUMPSHILL, ISIS,   34000, 4):TweetResponse(107485, 7800),
    Tweet(CNN,        ALEPPO,   993, 3):TweetResponse(589, 47),
    Tweet(VOX,        SYRIA,     52, 7):TweetResponse(70, 2)
}
