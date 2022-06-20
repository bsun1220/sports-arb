from draftkingsscrape import draftking
from caesarscrape import caesar
from fandualscrape import fandual
from pointsbetscrape import pointsbet
from match import match_source
from sort import sort_data
from statistics import stat
import copy
import requests


def find():
    data1 = caesar()
    data2 = draftking()
    data3 = fandual()
    data4 = pointsbet()
    matched = match_source(copy.deepcopy(data1),copy.deepcopy(data2),copy.deepcopy(data3),copy.deepcopy(data4))
    sort = sort_data(matched)
    return sort
    