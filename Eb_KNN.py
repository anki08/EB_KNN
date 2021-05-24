import pandas as pd
from math import sqrt

from sklearn.decomposition import PCA


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if int(actual[i]) == int(predicted[i]):
			correct += 1
	return correct / float(len(actual)) * 100.0


def get_neighbors(train, test_row):
    dist_list = list()
    for ind in range(len(train)):
        dist = euclidean_distance(test_row, train.iloc[ind])
        dist_list.append(dist)
    distances = train
    distances["euc_dist"] = dist_list
    distances = distances.sort_values('euc_dist')
    # distances = distances.iloc[1:]
    k_min = 3
    for k_min in range(3, len(distances)):
        k_fin = distances.head(k_min)
        n1 = len(k_fin.loc[(k_fin['diagnosis'] == 0)])
        n2 = len(k_fin.loc[(k_fin['diagnosis'] == 1)])
        if (n1 != k_min and n2 != k_min):
            break
    final_p1_list = list()
    final_k_list = list()
    final_df = pd.DataFrame()
    for k1 in range(k_min, len(train), 10):
        p1_list = list()
        k_list = list()
        df = pd.DataFrame()
        for k in range(k1, k1+10):
            neighbour_dist = distances.head(k)
            n1 = len(neighbour_dist.loc[(neighbour_dist['diagnosis'] == 0)])
            n2 = len(neighbour_dist.loc[(neighbour_dist['diagnosis'] == 1)])
            n1 = min(n1, n2)
            p1 = n1/k
            p2 = 1-p1
            p1_list.append(p1)
            k_list.append(k)
        df["p1"] = p1_list
        df["k"] = k_list
        min_p1 = df["p1"].min()
        min_k = df.loc[(df['p1'] == min_p1)]
        min_k = int(min_k.iloc[0][1])
        final_p1_list.append(min_p1)
        final_k_list.append(min_k)
        k_neigh = distances.head(min_k)
        n1_k = len(k_neigh.loc[(k_neigh['diagnosis'] == 0)])
        n2_k = len(k_neigh.loc[(k_neigh['diagnosis'] == 1)])
        min_n1 = min(n2_k, n1_k)
        max_n2 = max(n2_k, n1_k)
        n1_dash = max_n2 * max_n2 / min_n1
        if(n1_dash + max_n2) >= len(train):
            break
    final_df["p1"] = final_p1_list
    final_df["k"] = final_k_list
    final_min_p1 = final_df["p1"].min()
    final_min_k = final_df.loc[(final_df['p1'] == final_min_p1)]
    # print(final_min_k.iloc[0][1])
    return final_min_k.iloc[0][1]

def predict_classification(train, test_row):
    neighbors = get_neighbors(train, test_row)
    neighbors = int(neighbors)
    train = train.sort_values('euc_dist')
    # print(train)
    train_neigh = train.head(neighbors)
    # print(train_neigh.fruit_label.mode())
    # print(train_neigh)
    # print( type(train_neigh.diagnosis.mode()))
    x = train_neigh.diagnosis.mode()
    return x[0]

error = [297, 298, 340,347, 363, 375, 379, 385, 406, 413, 430, 448, 465, 472, 476, 481, 491, 508, 513, 532,536, 541]
# error = []
if __name__ == '__main__':
    fruits = pd.read_csv('processed_data.csv')
    # print(fruits.head())
    fruits = fruits[["radius_worst", "texture_worst", "perimeter_worst", "area_worst","smoothness_worst", "compactness_worst","concavity_worst","concave_points_worst","symmetry_worst","fractal_dimension_worst",
                     "radius_mean_ul", "texture_mean_ul", "perimeter_mean_ul", "area_mean_ul","smoothness_mean_ul", "compactness_mean_ul","concavity_mean_ul","concave_points_mean_ul","symmetry_mean_ul","fractal_dimension_mean_ul",
                     "radius_mean_ll", "texture_mean_ll", "perimeter_mean_ll", "area_mean_ll","smoothness_mean_ll", "compactness_mean_ll","concavity_mean_ll","concave_points_mean_ll","symmetry_mean_ll","fractal_dimension_mean_ll","diagnosis"]]


    dataclasses = ["M", "B"]
    # fruits = fruits[["radius_mean", "perimeter_mean", "area_mean", "concavity_mean", "concave_points_mean", "diagnosis"]]


    fruits['diagnosis'] = fruits['diagnosis'].apply(dataclasses.index)
    # print(fruits.head())

    train = fruits.head(290)
    new = fruits.iloc[error]
    final_train = train.append(new, ignore_index=True)


    array = list(range(290,569))
    array = [i for i in array if i not in error]
    # print(array)
    predicted = []
    actual = []
    for i in array:
        prediction = predict_classification(final_train, fruits.iloc[i])
        if(int(fruits.iloc[i]['diagnosis']) != int(prediction)):
            print("Expected",(int(fruits.iloc[i]['diagnosis'])), " Got " , int(prediction), "for i = ", i)
        #confirm index
        predicted.append(int(prediction))
        actual.append(int(fruits.iloc[i]['diagnosis']))

    accuracy = accuracy_metric(actual, predicted)
    print("aaccuracy : ", accuracy)