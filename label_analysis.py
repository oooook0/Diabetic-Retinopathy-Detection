import pandas as pd


data = pd.read_csv("trainLabels.csv")

def split(dataset, match):
	dataset['left'] = 0
	dataset.loc[dataset[match].str.contains("left"), "left"] = 1
	return dataset

df = split(data, "image")

print("Number of images with no DR: {}".format(df[ (df["left"] == 1) & (df["level"] == 0) ].sum()[-1]))
print("Number of images with Mild DR: {}".format(df[ (df["left"] == 1) & (df["level"] == 1) ].sum()[-1]))
print("Number of images with Moderate DR: {}".format(df[ (df["left"] == 1) & (df["level"] == 2) ].sum()[-1]))
print("Number of images with Severe DR: {}".format(df[ (df["left"] == 1) & (df["level"] == 3) ].sum()[-1]))
print("Number of images with Proliferative DR: {}".format(df[ (df["left"] == 1) & (df["level"] == 4) ].sum()[-1]))