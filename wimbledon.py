filename = "wimbledon.csv"
csv = []
win_names = []
win_country = []
name_and_number = {}
with open(filename, "r", encoding="utf-8-sig") as in_file:
    for line in in_file:
        line = line.strip().split(",")  # separate with “,”
        csv.append(line)  # add csv
for i in range(2, len(csv)):  # country ➡ number
    win_names.append(csv[i][2])  # part 3 name get
    country = str(csv[i][1])  # part 2 country and into a string
    if country not in win_country:
        win_country.append(country)  # add country and check
for name in win_names:  # get name
    name_and_number[name] = name_and_number.get(name, 0) + 1
print("Wimbledon Champions: ")
for ii in name_and_number:
    print(f"{ii} {name_and_number[ii]}")
print("These 12 countries have won Wimbledon: ")
print(", ".join(sorted(win_country)))  # ", "Split and sort
