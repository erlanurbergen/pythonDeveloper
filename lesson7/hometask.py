# task 1
# def disemvowel(string_):
#     for i in "euioaEUIOA":
#         string_ = string_.replace(i, "")
#     return string_
#
# print(disemvowel("This website is for losers LOL!"))

# task 3
# def validate_pin(pin):
#     if pin.isdigit():
#         return len(pin) == 4 or len(pin) == 6
#     return False
#
# print(validate_pin("-1234"))

# task 4
def to_jaden_case(string):
    l1 = string.split(" ")
    text = ""
    for i in l1:
        text += i.capitalize() + " "

    return text.strip()

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))