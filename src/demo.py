from src.itemCF import item_based_rs
from src.readData import *
from src.userCF import *

def main():
    print("-----------------欢迎来到智能影视推荐系统------------------")
    print("正在读入训练集数据，请稍后.....")
    prefs = read_data()
    print("读入完毕")
    # 注意userid为1.0型
    user_id = input("请输入您的用户名（以回车键结束）:")
    while True:

        print('''主菜单：
            1.演示基于用户的协同过滤算法
            2.演示基于内容的协同过滤算法''')
        choice  = input("请输入选项：")
        if choice == '1':
            print("您的观看历史及评分为：")
            print("|  影视名称  |  您的评分  |")

            for movie, rating in prefs[user_id].items():
                text = "| " + movie + '  |  ' + str(rating) + ' |'
                print(text)
            print("正在基于此您生成个性化推荐影视清单...请稍后")
            print("推荐给您的影视Top10为:")
            for (sim, movie) in get_recommendations(prefs,user_id)[:10]:
                print(movie)

        if choice == '2':
            item_based_rs(prefs,user_id)
main()