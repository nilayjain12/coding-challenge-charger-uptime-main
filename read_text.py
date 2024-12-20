
# Read the text from input file, using the in-built readlines method, to get the whole line in the form of list
with open("input_2.txt", "r") as input_file:
    content = input_file.readlines()

print("Original Content:\n", content)
# Removing \n from each element to make it simpler
for i in range(len(content)):
    content[i] = content[i].rstrip()
print(r"After removing \n:", "\n", content)
# Remove empty strings from content
content = [x for x in content if x]
print("After removing empty strings:\n", content)

# Initialize station dictionary that will hold the list of charger id's
station_ids = dict()

# Parse the elements till we find the string "[Charger Availability Reports]"
k, i = 1, 1
while content[k] != "[Charger Availability Reports]":
    element = content[i].split()    # element is the list of strings
    temp_list = []
    for j in range(1, len(element)):
        temp_list.append(int(element[j]))
    station_ids[int(element[0])] = temp_list
    # update the while increment parameters
    k += 1
    i += 1
print("Printing station dictionary:\n", station_ids)

# Initialize a list that will store lists of charger details
charger_details = []

for l in range(k+1, len(content)):      # 4 -> 7
    element = content[l].split()       # [1001, 0, 50000, true]
    temp_list_element = []
    for item in element:
        if item.isdigit():
            temp_list_element.append(int(item))
        else:
            temp_list_element.append(item)
    charger_details.append(temp_list_element)
print("After extracting charging details:\n", charger_details)

