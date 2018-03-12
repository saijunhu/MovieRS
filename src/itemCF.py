from src.readData import *
from src.userCF import *
import operator


def item_based_rs(prefs, userId):
    item_prefs = transformed_prefs(prefs)
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
        result.append(top_matches(item_prefs, item,n=2))
    print("为您推荐的影视为:")
    print(result)
    # #    #process the movies.csv
    # dataframe = pd.read_csv(directory+'/movies.csv')
    # # print(dataframe.dtypes)
    # movies = dataframe.set_index('movieId')['title'].to_dict()