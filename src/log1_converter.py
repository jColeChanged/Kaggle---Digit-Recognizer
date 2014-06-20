# Messed up on the output formatting of my first attempt at logistic regression.
# I had expected the logistic classifier to output labels as intergers, but instead
# I got a list containing a float. Rather than re-run the script, which actually
# takes a long time to train, I'm going to coerce the output file into something
# more readable.

import csv

in_file_path = r"../models/log1.csv"
out_file_path = r"../models/log1v2.csv"
with open(in_file_path, "rb") as in_file:
    csv_in = csv.reader(in_file)
    with open(out_file_path, "wb") as out_file:
        csv_out = csv.writer(out_file)
        headers = csv_in.next()
        csv_out.writerow(headers)
        for row in csv_in:
            prediction = int(eval(row[1])[0])
            csv_out.writerow([row[0], prediction])
