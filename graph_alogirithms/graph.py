"""
nodes are ordered alphabetically:
    BOS, BWI, DFW, JFK, LAX, MIA, ORD, PVD, SFO
BOS, -------------------------------------------
BWI,
DFW,
JFK,
LAX,
MIA,
ORD,
PVD,
SFO
"""

from enum import Enum


class AP(Enum):
    BOS, BWI, DFW, JFK, LAX, MIA, ORD, PVD, SFO = 0, 1, 2, 3, 4, 5, 6, 7, 8

lv = float('inf')

adj_mtx = [
    [0, lv, lv, 187, lv, 1258, 867, lv, 2704],
    [lv, 0, lv, 184, lv, 946, 621, lv, lv],
    [lv, lv, 0, 1391, 1235, 1121, 802, lv, 1464],
    [187, 184, 1391, 0, lv, 1090, 740, 144, lv],
    [lv, lv, 1235, lv, 0, 2342, lv, lv, 337],
    [1258, 946, 1121, 1090, 2342, 0, lv, lv, lv],
    [867, 621, 802, 740, lv, lv, 0, 849, 1846],
    [lv, lv, lv, 144, lv, lv, 849, 0, lv],
    [2704, lv, 1464, lv, 337, lv, 1846, lv, 0]
]

