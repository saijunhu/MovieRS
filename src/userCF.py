from math import sqrt

# user te pearson param to evaulate the simarilty of people
from src.readData import *


def sim_pearson(prefs, user1Id, user2Id):
    # get the common list
    common = {}
    for item in prefs[user1Id]:
        if item in prefs[user2Id]:
            common[item] = 1

    # if two people no common rated movie,then return
    if len(common) == 0:
        return 0

    # sum the all prefs
    sum1 = sum([prefs[user1Id][item] for item in common])
    sum2 = sum([prefs[user2Id][item] for item in common])

    # 求平方和
    sum1Sq = sum([pow(prefs[user1Id][item], 2) for item in common])
    sum2Sq = sum([pow(prefs[user2Id][item], 2) for item in common])

    # 求乘积之和
    pSum = sum([prefs[user1Id][item] * prefs[user2Id][item] for item in common])

    # 计算皮尔逊评价值
    n = len(common)
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


def top_matches(prefs, userId, n=5, similarity=sim_pearson):
    '''该函数得到与目标用户喜好程度最为相同的n个用户。'''
    scores = [(similarity(prefs, userId, other), other) for other in prefs if other != userId]
    scores.sort()
    scores.reverse()
    return scores[0:n]


def get_recommendations(prefs, userId, similarity=sim_pearson):
    """该函数得到推荐的电影列表。"""
    totals = {}
    simSum = {}
    for other in prefs:
        if other == userId:
            continue
        sim = similarity(prefs, userId, other)
        # ignore the sum value less than 0
        if sim <= 0:
            continue
        for item in prefs[other]:
            if item not in prefs[userId] or prefs[userId][item] == 0:
                totals.setdefault(item, 0)
                # for every item calculate the sim*rating
                totals[item] += prefs[other][item] * sim
                # calculate the sim sum
                simSum.setdefault(item, 0)
                simSum[item] += sim
    # create the normalized list
    rankings = [(total / simSum[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


def main():
    prefs = read_data()
    # print("the pearson score is: ", end=' ')
    # print(sim_pearson(prefs, 2, 4))
    # print(top_matches(prefs, 2))
    print(get_recommendations(prefs, '2.0'))

# main()
