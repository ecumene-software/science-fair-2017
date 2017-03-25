class Creator():
    def __init__(self, subs, views):
        self.subs = subs
        self.views = views

class Topic():
    def __init__(self, dayinterest30, dayinterestyear):
        self.dayinterest30 = dayinterest30
        self.dayinterestyear = dayinterestyear

FANTANO       = Creator(814574, 172114491)
JACOB         = Creator(497757,  33398107)
TMZ           = Creator(2283837, 1947391120)
ST            = Creator(1000, 1000000)         # Small random youtuber
VOX           = Creator(1498998, 288520295)
VICE          = Creator(7394068, 1214109215)
BERNIESHILL   = Creator(36362,  5549211)
ABC           = Creator(2210939,  2277256814)
CNN           = Creator(1699122,  1569673854)
ABNN          = Creator(19904,  24028430)
TRUMPSHILL    = Creator(79051, 22324720)
MOVIETRAILERS = Creator(10328663, 7351979537)
WILLVEVO      = Creator(273793, 144532621)
SEEKER        = Creator(1350426, 276320563)
LWT           = Creator(4405676, 967885659)

KENYE     = Topic(30, 50)
BERNIE    = Topic(20, 60)
TRUMP     = Topic(14, 20)
WILLSMITH = Topic(75, 35)
ALEPPO    = Topic(80, 45)
SYRIA     = Topic(90, 75)
ISIS      = Topic(80, 60)
