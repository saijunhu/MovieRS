from src.readData import *
from src.userCF import *
item_prefs = transformed_prefs(read_data())
# print(top_matches(item_prefs, 'Clueless (1995)'))

print(get_recommendations(item_prefs, 'Clueless (1995)'))