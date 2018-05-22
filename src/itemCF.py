from src.readData import *
from src.userCF import *
import operator


def item_based_rs(prefs, movie):
    itemPrefs = transformed_prefs(prefs)
    result = top_matches(itemPrefs, movie, n=10)
    for (sim, movie) in result:
        print(movie)



# The following two func is using static dataset to use item_based CF,improved ,but not used.适合于实践中对大规模数据进行
# 一次性的处理，以加速之后的查询工作
def calculateSimilarityItems(prefs, n=10):
    ''' Construct a dataset contains similar items ,this work only need one shot,
         in the following operations ,we can use the result repeatly '''
    result = {}
    # reverse the pref matrix
    itemPrefs = transformed_prefs(prefs)

    for item in itemPrefs:
        # find the most similar items
        scores = top_matches(itemPrefs, item, n=n, similarity=sim_distance)
        result[item] = scores
    return result


def getRecommendItems(prefs, itemMatch, userId):
    userRatings = prefs[userId]
    scores = {}
    totalSim = {}
    # 循环遍历当前用户评分的产品
    for (item, rating) in userRatings.items():
        # 循环遍历与当前物品相近的物品
        for (similarity, item2) in itemMatch[item]:
            # 如果用户已经对物品做过评价，则跳过
            if item2 in userRatings:
                continue
            # 评价值与相似度的加权之和
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            #全部相似度之和
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity
    #将每个合计值除以加权平均和，求出平均值
    rankings = [(score/totalSim[item], item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


def test():
    prefs = read_data()
    itemsim = calculateSimilarityItems(prefs, 10)
    print(getRecommendItems(prefs, itemsim, userId='2.0'))


# test()