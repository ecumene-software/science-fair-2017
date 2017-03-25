import numpy as np
from articles import *

class YTVideo():
    def __init__(self, creator, person, projshares, monthsage):
        self.creator = creator
        self.person = person
        self.projshares = projshares
        self.monthsage  = monthsage
    def to_arr(self):
        return  np.array([self.creator.subs, self.creator.views,
            self.person.dayinterest30, self.person.dayinterestyear,
            self.projshares, self.monthsage], np.int64)

class YTResponse():
    def __init__(self, views, subboost):
        self.views = views
        self.subboost = subboost
    def to_arr(self):
        return np.array([self.views, self.subboost], np.int64)

yt_namedrop = {
    # 0 DAYS
    YTVideo(FANTANO, KENYE, 1426, 9):YTResponse(1549940, 3752), # Fantanos old video on kenye, MAX VIEWS.
    YTVideo(ST,      KENYE, 1069, 1):YTResponse(373776,  8),    # Small youtuber gets huge subboost
    YTVideo(JACOB,   KENYE, 5,    0):YTResponse(5756,    2),    # BAM, small youtuber gets REKT in DAYS
    YTVideo(FANTANO, KENYE, 314,  0):YTResponse(1004304, 4480), # Shows how a simple name drop can BANG up a view count
    YTVideo(TMZ,     KENYE, 656,  0):YTResponse(175099,  25),   # TMZ sees a nice turnout in days
    YTVideo(BERNIESHILL, BERNIE, 30141, 18):YTResponse(2824686, 8259), # Videos popular because of bernie supporters
    YTVideo(VOX,         BERNIE, 1426,  17):YTResponse(752849,  1024),  # Vox name drops bernie
    YTVideo(CNN,         BERNIE, 786,    5):YTResponse(142432,  13),
    YTVideo(CNN,         BERNIE, 2854,   1):YTResponse(643600,  129),
    YTVideo(CNN,         BERNIE, 596,   11):YTResponse(305800,  45),
    YTVideo(BERNIESHILL, BERNIE, 605,    1):YTResponse(95214,   145), # Video somewhat popular during course of few days
    YTVideo(TRUMPSHILL,  TRUMP, 455,    5):YTResponse(101515,  284),  # Odd subboost, nice growth
    YTVideo(TRUMPSHILL,  TRUMP, 962,    2):YTResponse(105592,  300),  # Pretty weird growth, lots of shares v views ..
    YTVideo(ABC,         TRUMP, 635,    1):YTResponse(357403,  85),   # Anouther big namedrop
    YTVideo(ABC,         TRUMP, 14297,  1):YTResponse(3744539, 1058), # Pretty big video from very large chanel, extreme namedrop!
    YTVideo(ABNN,        TRUMP, 87,     1):YTResponse(40531,   29),   # Early namedrop, not huge growth over time
    YTVideo(LWT,         TRUMP, 9561,   1):YTResponse(3195672, 1570),
    YTVideo(WILLVEVO,      WILLSMITH, 140352,68):YTResponse(23432073, 203),  # Old, huge video
    YTVideo(MOVIETRAILERS, WILLSMITH, 43362,  3):YTResponse(4292085,  1116), # Giant movie reveal
    YTVideo(SEEKER, ALEPPO, 941,  6):YTResponse(176086, 126),
    YTVideo(CNN,    ALEPPO, 1709, 5):YTResponse(174141, 19),
    YTVideo(CNN,    ALEPPO, 1476, 5):YTResponse(163185, 46),
    YTVideo(CNN,    ALEPPO, 2769, 5):YTResponse(390825, 87),
    YTVideo(VOX,    ALEPPO, 1221, 3):YTResponse(269775, 903),
    YTVideo(ST,     SYRIA,  1605, 3):YTResponse(316425,  1181),
    YTVideo(VOX,    SYRIA,  4203, 12):YTResponse(3393615, 2050),
    YTVideo(VOX,    ISIS,   2010, 8):YTResponse(955747, 208),
    YTVideo(VOX,    ISIS,   3203,12):YTResponse(3682656,603),
    YTVideo(SEEKER, ISIS,   303,  3):YTResponse(213375, 58),
    YTVideo(CNN,    ISIS,   417,  2):YTResponse(187616, 95),
    YTVideo(CNN,    ISIS,   60,   2):YTResponse(96254,  60),
    YTVideo(CNN,    ISIS,   1927, 1):YTResponse(505643, 308),
}
