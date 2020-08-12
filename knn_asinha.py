import pandas as pd
from math import sqrt

def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for ind in range(len(train)):
        dist = euclidean_distance(test_row, train.iloc[ind])
        distances.append((train.iloc[ind], dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

if __name__ == '__main__':
    fruits = pd.read_csv('knn_fruit.csv')
    print(fruits.head())
    fruits = fruits[["mass", "width", "height", "color_score", "fruit_label"]]
    prediction = predict_classification(fruits, fruits.iloc[34], 3)
    print('Expected %d, Got %d.' % (fruits.iloc[34][4], prediction))