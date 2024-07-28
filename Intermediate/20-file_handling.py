### File Handling ###

# .txt file
txt_file = open("Intermediate/my_file.txt", "r+")
##print(txt_file.read())
##print(txt_file.read(10))
#print(txt_file.readline())
print(txt_file.readlines())
txt_file.write("\nEsta es una nueva línea")


import json

json_file = open("Intermediate/my_file.json", "w+")
json_text = {
    "name": "Maximiliano",
    "surname": "Cerra",
    "age": 40
}

json.dump(json_text, json_file, indent= 1)


import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age"])
csv_writer.writerow(["name", "surname", "age"])
csv_writer.writerow(["name", "surname", "age"])



