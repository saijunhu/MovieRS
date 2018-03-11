import pandas as pd

directory = '/Users/Atlantis/code/Python/MovieRS/Data'
def read_data():
    #process the movies.csv
    dataframe = pd.read_csv(directory+'/movies.csv')
    # print(dataframe.dtypes)
    movies = dataframe.set_index('movieId')['title'].to_dict()
    # print(movies)

    #process the ratings/csv

    df = pd.read_csv(directory+'/ratings.csv')
    print(df.dtypes)
    prefs = {}
    for index, row in df.iterrows():
        prefs.setdefault(str(row['userId']), {})
        prefs[str(row['userId'])][str(movies[row['movieId']])] = float(row['rating'])
    # print(prefs[1])
    return prefs

def transformed_prefs(prefs):
    '''use the function to transform'''
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            result[item][person] = prefs[person][item]
    return result

