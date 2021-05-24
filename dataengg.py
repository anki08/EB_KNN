import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_csv('UCI.csv')
print(data.head())
data['radius_mean_ul'] = data['radius_mean'] + data['radius_se']
data['texture_mean_ul'] = data['texture_mean'] + data['texture_se']
data['perimeter_mean_ul'] = data['perimeter_mean'] +data['perimeter_se']
data['area_mean_ul'] = data['area_mean'] + data['area_se']
data['smoothness_mean_ul'] = data['smoothness_mean'] +data['smoothness_se']
data['compactness_mean_ul'] = data['compactness_mean'] +data['compactness_se']
data['concavity_mean_ul'] = data['concavity_mean'] +data['concavity_se']
data['concave_points_mean_ul'] = data['concave_points_mean'] +data['concave_points_se']
data['symmetry_mean_ul'] = data['symmetry_se'] +data['symmetry_mean']
data['fractal_dimension_mean_ul'] = data['fractal_dimension_mean'] +data['fractal_dimension_se']
data['radius_mean_ll'] = data['radius_mean'] - data['radius_se']
data['texture_mean_ll'] = data['texture_mean'] - data['texture_se']
data['perimeter_mean_ll'] = data['perimeter_mean'] -data['perimeter_se']
data['area_mean_ll'] = data['area_mean'] - data['area_se']
data['smoothness_mean_ll'] = data['smoothness_mean'] -data['smoothness_se']
data['compactness_mean_ll'] = data['compactness_mean'] -data['compactness_se']
data['concavity_mean_ll'] = data['concavity_mean'] -data['concavity_se']
data['concave_points_mean_ll'] = data['concave_points_mean'] -data['concave_points_se']
data['symmetry_mean_ll'] = data['symmetry_se'] -data['symmetry_mean']
data['fractal_dimension_mean_ll'] = data['fractal_dimension_mean'] -data['fractal_dimension_se']
data.to_csv('processed_data.csv')