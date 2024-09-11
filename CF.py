import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

result_tracks=set()

# Сгенерируем матрицу users-items
users_size=100
items_size=100
mat_users_items=np.random.random((users_size,items_size))

for i in range(users_size):
    for j in range(items_size):
        mat_users_items[i][j]=np.around(mat_users_items[i][j])


# Найдём "близких" пользователей через косинусное сходство
user=np.array([np.around(x) for x in np.random.random((items_size))])
print(user)
treshhold=5
alpha=1
result_users=set()

while len(result_users)<10:
    for i in range(users_size):
        if i not in result_users and sum(mat_users_items[i])>treshhold:
            cos_dst=cosine_similarity([user],[mat_users_items[i]])[0][0]
            if cos_dst>alpha:
                for j in range(items_size):
                    if mat_users_items[i][j]==1:
                        result_tracks.add(j)
                        result_users.add((i,cos_dst))
    alpha-=0.01


# Добавим треки, которые есть у похожих пользователей, но нет у user
for id in range(items_size):
    if user[id] and id in result_tracks:
        result_tracks.remove(id)

print(result_tracks, len(result_tracks))
print(result_users, len(result_users))


# Для примера используем пользователей, полученных в результате фильтрацииы
# [(10, 0.6371930928643099), (12, 0.6089028755593185), (35, 0.6240896334821995), (64, 0.6089028755593184), (67, 0.6174969805662238), (14, 0.6240896334821996), (7, 0.61088283865697), (50, 0.6819385906727176), (82, 0.600099198148979), (89, 0.6057340560268407), (81, 0.6017934765940705), (51, 0.6141296055506468), (57, 0.6071428571428572), (31, 0.6371930928643099)]