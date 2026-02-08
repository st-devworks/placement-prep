# DAY 8 – Dictionaries & Sets

student = {
    "name": "Shikhar",
    "age": 21,
    "branch": "AIML"
}

print(student)
print(student["name"])

#Adding & updating values
student["college"] = "RGPV"
student["age"] = 22

print(student)

#Looping through dictionary
for key in student:
    print(key, ":", student[key])

#Topic 2: Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

#Safe access
print(student.get("name"))
print(student.get("marks", "Not available"))

#Sets
numbers = {1, 2, 3, 4, 4, 5}
print(numbers)   # duplicates removed

#Creating a set
a = {1, 2, 3}
b = {3, 4, 5}

#Set operations
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# Set methods
numbers.add(6)
numbers.remove(3)
print(numbers)

#Count frequency using dictionary
text = "banana"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

#Remove duplicates
lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print(unique)

student = {
    "name": "Shikhar",
    "age": 21
}

student["age"] = 22        # update
student["college"] = "RGPV" # add
del student["name"]        # delete

print(student)
