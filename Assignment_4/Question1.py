import csv
file= [["Name", "   Address", "   Mobile", "E-Mail"],
    ["Garvit", "Jaipur, Rajasthan", "9745342345", "garvit@gmail.com"],
    ["Gauri", "Delhi, Delhi", "8745242341", "gauri@gmail.com"],
    ["Harsh", "Kota, Rajasthan", "7745222345", "harsh@gmail.com"],
    ["Lakshay", "Kota, Rajasthan", "9645442321", "lkr@gmail.com"]
    ]
with open("file.csv", "w", newline="")as f:
    writer = csv.writer(f)
    for row in file:
        writer.writerow(row)
with open("file.csv", "r", newline="")as f:
   reader = csv.reader(f)
   for l in reader:
        print(l)
