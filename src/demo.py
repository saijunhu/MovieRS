from src.itemCF import *
from src.readData import *
from src.userCF import *
from src.hybridRS import *
import pickle
def main():
    print("^_^---------------欢迎来到智能影视推荐系统------------------")
    print("正在读入用户及影视数据，请稍后.....")
    prefs = read_data()
    print("读入完毕")
    print("正在读入预计算数据，请稍后.....")
    f = open('simItem.txt', 'rb')
    simItem = pickle.load(f)
    f.close()
    print("读入完毕")
    # 注意userid为1.0型
    user_id = input("请输入您的用户名（以回车键结束）:")
    sorted_prefs = sorted(prefs[user_id].items(), key=lambda x: x[1])
    # sorted_prefs = sorted(prefs[userId].items(), key=operator.itemgetter(1)).reverse()
    print("已读取到您的历史记录及评分(按照评分从高到低）:")
    print("|  影视名称  |  您的评分  |")
    for (movie, rating) in sorted_prefs:
        text = "| " + movie + '  |  ' + str(rating) + ' |'
        print(text)
    print("接下来将依据此记录为您做出个性化的推荐...^_^....")

    userCFResult = []
    itemCFResult = []

    while True:
        print('''主菜单：
            1.演示基于用户的协同过滤算法
            2.基于内容的协同过滤算法（根据某一电影推荐）
            3.基于内容的协同过滤算法(改进预计算版）
            4.组合推荐算法''')
        choice  = input("请输入选项：")
        if choice == '1':
            print("正在基于此您生成个性化推荐影视清单...请稍后")
            print("推荐给您的影视Top10为:")
            temp = get_recommendations(prefs, user_id)[:50]
            userCFResult = temp
            for (ratings, movie) in temp[:10]:
                print(ratings, movie)

        if choice == '2':
            movie = input("请输入电影名称: ")
            print("给您推荐的影视为: ")
            # Tom and Huck (1995)
            item_based_rs(prefs, movie)

        if choice == '3':
            result = getRecommendItems(prefs, simItem, user_id)
            itemCFResult = result
            print("给您推荐的Top10影视为: ")
            for (ratings, movie) in result[:10]:
                print(ratings, movie)


        if choice == '4':
            userMovie = [movie for (r,movie) in userCFResult]
            itemMovie = [movie for (r,movie) in itemCFResult]
            result = [m for m in userMovie if m in itemMovie]
            print("给您推荐的影视为: ")
            for m in result:
                print(m)

main()
