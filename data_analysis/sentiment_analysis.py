from nrclex import NRCLex
import numpy as np
import csv

# if file type csv
text = ""
with open("INCEPTION_ARIADNE.csv") as file:
    lines = csv.reader(file)
    for line in lines:
        text += line[1]

# change scripts
text_object = NRCLex("""""")

labels = np.array(["joy", "sadness", "anger", "disgust", "fear"])
stats = np.array([text_object.raw_emotion_scores[i] for i in labels])
stats = np.array([int(round(i / stats.sum() * 100)) for i in stats])
print(labels)
print(stats)
