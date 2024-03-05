# # for loop
# list = ["Paul", "John", "Clare", "Joe", "Tim"]

# for name in list:
#     print(name)

# while loop
# n = 0

# while n < 5:
#     print("Executing while loop")
#     print(n)
#     n = n + 1

# names = ["Mollie","Sax","Amber","Samet","Tudor"]
# print(len(names)) # counts how many items are in an array

# for name in (names):
#   print("Hello, " + name)

# numbers = [4, 7, 2, 76, 54, 3, 1]
 
# for num in numbers:
#     if num > 5:
#         print(num)

# count = 1

# while count < 9:
#    print(count)
#    count += 1

# names = ["Mollie","Sax","Amber","Samet","Tudor"]
# # print(names[-1]) # prints the last item in the array, -2 second from last (Samet) etc
# # print(names[0]) # prints the first item in the array
# names.append("Paul") # add an item to the array
# names.remove("Amber") # remove an item from the list

# nums = list(range(10)) # generates a list of numbers with built-in funtions
# print(nums)
# nums = list(range(0, 100, 5)) # starts at 0 and go up to 100 in jumps of 5. Includes 0 but excludes 100

# print(nums[0:4]) # a subset from the first item to the fourth item
# print(nums[4:]) # start at the fouth item onwards
# print(nums[:6]) # up to the sixth item
# print(len(nums)) # prints the length of the array
# print(max(nums)) # prints the maximum value in the array
# print(min(nums)) # prints the minimum value in the array

paulDictionary = {
    "name": "Paul",
    "age": 30,
    "address": "BL1"
}

# print(type(paulDictionary)) # tell me the class of the list
# print(paulDictionary) # prints the entire dictionary
# print(paulDictionary["name"]) # prints the value that is assigned to name
print(paulDictionary.keys())
print(paulDictionary.values())

