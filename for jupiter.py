from csv import reader
opened_file_2 = open("googleplay.csv", "r", encoding = "utf8")
str_data_2 = opened_file_2.read()
new_str_data_2 = str_data_2.replace('\n\n', "")

new_file = open("new.csv", "w", encoding= "utf_8")
new_file.write(new_str_data_2)
new_file.close()

new_file = open("new.csv", "r", encoding="utf8")
read_new_file  = reader(new_file )
data_2 = list(read_new_file )
print(data_2[0])


def explore(data, start, end):
    print("The rows of is: {}".format(len(data)))
    print("The columns of is: {}".format(len(data[0])))
    print(data[start:end])
    return "Good luck!"



duplicate_apps = [] # check out if we have duplicate data=> yes we have
unique_apps = []
for app in data_2:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)


review_max = {}  #make a dictionary that have perfekt user review
for lst in data_2:
    app_name = lst[0]
    if app_name not in review_max:
        review_max[app_name] = lst[3]
    else:
        if review_max[app_name] < lst[3]:
            review_max[app_name] = lst[3]


android_clean = []   # add data to the list we need. 
already_added = []
for lst in data_2[1:]:
    if review_max[lst[0]] == lst[3] and lst[0] not in already_added:
        android_clean.append(lst)
        already_added.append(lst[0])



android_clean_eng = []
for app in android_clean:
    i = 0
    for char in app[0]:
        if ord(char) > 127:
            i += 1
    if i < 3:
        android_clean_eng.append(app)
#print(explore(android_clean_eng, 0, 0))
#print(explore(android_clean, 0,0))


android_final = []
android_final.append(android_clean[0])
for app in android_clean_eng:
    if app[7] == "0":
        android_final.append(app)

csv_file = open("android_final.csv", "w", encoding = "utf8")
for app in android_final:
    csv_file.write(str(app))
    csv_file.write("\n")
csv_file.close()