from sklearn.linear_model import LogisticRegression
import numpy as np
import csv

print "Reading in training file..."
with open("../data/train.csv", "rb") as train_file:
	train_reader = csv.reader(train_file)
	train_headers = train_reader.next()
	train_data = np.array(list(train_reader)).astype(np.float)

train_xs = train_data[:, 1:]
train_ys = train_data[:, 0]
print "Training file read"

print "Training with training data..."
classifier = LogisticRegression()
classifier.fit(train_xs, train_ys)
print "Training finished"

print "Reading in test data..."
with open("../data/test.csv", "rb") as test_file:
	test_reader = csv.reader(test_file)
	test_headers = test_reader.next()
	test_data = np.array(list(test_reader)).astype(np.float)
print "Test data read..."

print "Doing predictions..."
with open("../models/log1.csv", "wb") as out_file:
	out_writer = csv.writer(out_file)
	out_writer.writerow(["ImageId", "Label"])
	image_id = 1
	for features in test_data:
		prediction = classifier.predict(features)
		out_writer.writerow([str(image_id), str(prediction)])
		image_id += 1
	



