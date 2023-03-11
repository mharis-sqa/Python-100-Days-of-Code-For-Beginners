# Day_ 22 Dictionaries in Python .........................................................................................

# customer = {
#     "name": "Haris",
#     "age": 30,
#     "is_verified": True
# }

# print(customer["name"])
# print(customer["age"])
# print(customer["is_verified"])
# print(customer.get("birthdate")) # if key is ot present we get none
# print(customer.get("birthday", "01 oct 2001")) # getting values or initiating values

## EXERCISE: converting numers into spellings

# phone = input("Enter The Number: ")

# digits = {
#     "1": 'one',
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }

# output = ""
# for ch in phone:
#     output += digits.get(ch, "!") + " "
# print(output)
