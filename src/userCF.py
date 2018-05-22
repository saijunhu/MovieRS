from math import sqrt

# user te pearson param to evaluate the similarity of people
from src.readData import *


# Choice1: use the Euclidean Distance Score as the similarity index
def sim_distance(prefs, user1Id, user2Id):
    # get the commmon list
    common = {}
    for item in prefs[user1Id]:
        if item in prefs[user2Id]:
            common[item] = 1
    if len(common) ==0 : return 0
    # When you writing the list generator, Do not forget write the brace
    sum_of_squares=sum([pow(prefs[user1Id][item]-prefs[user2Id][item],2)
                       for item in common])
    return (1/(1+sqrt(sum_of_squares)))


# Choice2: use the Pearson Correlation Score as the similarity index
def sim_pearson(prefs, user1Id, user2Id):
    # get the common list
    common = {}
    for item in prefs[user1Id]:
        if item in prefs[user2Id]:
            common[item] = 1

    # if two people no common rated movie,then return
    n = len(common)
    if n == 0:
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

# The other alternative similarity index is feasible , such as Jaccard 系数，曼哈顿距离

def top_matches(prefs, userId, n=5, similarity=sim_pearson):
    '''该函数得到与目标用户喜好程度最为相同的n个用户。'''
    scores = [(similarity(prefs, userId, other), other) for other in prefs if other != userId]
    scores.sort()
    scores.reverse()
    return scores[0:n]


# Calculate the person similarity advanced, one execute, one shot, improve the efficiency，该函数未使用
def calculateSimilarityUser(prefs, n=10):
    result={}
    for user in prefs:
        scores = top_matches(prefs, user, n, sim_distance)
        result[user] = scores
    return result


def get_recommendations(prefs, userId, similarity=sim_pearson):
    """该函数得到推荐的电影列表。"""
    totals = {}
    simSum = {}
    for other in prefs:
        # Do not compare with yourself
        if other == userId:
            continue
        sim = similarity(prefs, userId, other)

        # ignore the sum value no larger than 0
        if sim <= 0:
            continue
        for item in prefs[other]:
            # only rate those movies that you haven't watched
            if item not in prefs[userId] or prefs[userId][item] == 0:
                totals.setdefault(item, 0)
                # for every person calculate the ratings * sim
                # the '+=' is for higher 'for' loop setting, means all other people's score on this item
                totals[item] += prefs[other][item] * sim
                # for every item,calculate the sim sum,'+=' is for higher 'for'loop setting ,
                # means all other people similarity sum,which rated this item
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
    # result = get_recommendations(prefs, '2.0',sim_pearson)

    result1 = sim_pearson(prefs,'1.0', '6.0')
    result2 = sim_distance(prefs,'1.0', '6.0')
    print("'浮点数")

# main()
