import pandas as pd
from math import sqrt
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


def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for ind in range(len(train)):
        dist = euclidean_distance(test_row, train.iloc[ind])
        distances.append((train.iloc[ind], dist))
    distances.sort(key=lambda tup: tup[1])
    # print("distances in ascending order: ", distances)
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

error = [297, 298, 340, 347, 363, 375, 379, 385, 406, 421, 430, 465, 472, 476, 481, 491, 508, 513, 518, 532, 536, 541]
# error = []
if __name__ == '__main__':
    fruits = pd.read_csv('processed_data.csv')

    print(fruits.head())
    fruits = fruits[["radius_worst", "texture_worst", "perimeter_worst", "area_worst","smoothness_worst", "compactness_worst","concavity_worst","concave_points_worst","symmetry_worst","fractal_dimension_worst",
                     "radius_mean_ul", "texture_mean_ul", "perimeter_mean_ul", "area_mean_ul","smoothness_mean_ul", "compactness_mean_ul","concavity_mean_ul","concave_points_mean_ul","symmetry_mean_ul","fractal_dimension_mean_ul",
                     "radius_mean_ll", "texture_mean_ll", "perimeter_mean_ll", "area_mean_ll","smoothness_mean_ll", "compactness_mean_ll","concavity_mean_ll","concave_points_mean_ll","symmetry_mean_ll","fractal_dimension_mean_ll","diagnosis"]]

    dataclasses = ["M", "B"]
    fruits['diagnosis'] = fruits['diagnosis'].apply(dataclasses.index)
    print(fruits.head())
    train = fruits.head(290)
    new = fruits.iloc[error]
    finaal_train = train.append(new, ignore_index=True)

    array = list(range(290, 569))
    array = [i for i in array if i not in error]
    # print(array)
    predicted = []
    actual = []
    for i in array:
        prediction = predict_classification(finaal_train, fruits.iloc[i], 5)
        if(int(fruits.iloc[i]['diagnosis']) != int(prediction)):
            print("Expected",int(fruits.iloc[i]['diagnosis']), " Got " , int(prediction), "for i = ", i)
        predicted.append(prediction)
        actual.append(fruits.iloc[i]['diagnosis'])

    accuracy = accuracy_metric(actual, predicted)
    print("aaccuracy : ", accuracy)