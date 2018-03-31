from src.readData import *
from src.userCF import *
import operator


def item_based_rs(prefs, userId):
    item_prefs = transformed_prefs(prefs)
    # 按照评分对字典排序
    sorted_prefs = sorted(prefs[userId].items(), key=lambda x: x[1])
    sorted_prefs = sorted_prefs[-5:]
    # sorted_prefs = sorted(prefs[userId].items(), key=operator.itemgetter(1)).reverse()
    print("您最喜欢的5部电影为:")
    print(sorted_prefs)
    print("正在基于此为您生成个性化推荐....")
    movies = []
    for movie, rating in sorted_prefs:
        movies.append(str(movie))
    # print(get_recommendations(item_prefs, 'Clueless (1995)'))
    result = []
    for item in movies:
        result.append(top_matches(item_prefs, item, n=2))
    print("为您推荐的影视为:")
    print(result)
    # #    #process the movies.csv
    # dataframe = pd.read_csv(directory+'/movies.csv')
    # # print(dataframe.dtypes)
    # movies = dataframe.set_index('movieId')['title'].to_dict()


# The following two func is using static dataset to use item_based CF,improved ,but not used.适合于实践中对大规模数据进行
# 一次性的处理，以加速之后的查询工作
def calculateSimilarityItems(prefs, n=20):
    ''' Construct a dataset contains similar items ,this work only need one shot,
         in the following operations ,we can use the result repeatly '''
    result = {}
    # reverse the pref matrix
    itemPrefs = transformed_prefs(prefs)

    for item in itemPrefs:
        # find the most similar items
        scores = top_matches(itemPrefs, item, n, sim_distance)
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
            totalSim += similarity
    #将每个合计值除以加权平均和，求出平均值
    rankings = [(scores/Decimal(totalSim[item]), item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


def test():
    prefs = read_data()
    itemsim = calculateSimilarityItems(prefs, 10)
    print(getRecommendItems(prefs, itemsim, userId='2.0'))


# test()