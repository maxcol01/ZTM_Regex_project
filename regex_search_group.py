import re

# string = "I remixed a remix, it was back to normal"
# search_pattern = "remix"

# try:
#     match = re.search(search_pattern, string)
#     print("We found a match")
#     print(f"The pattern is: {match.group()}")
# except:
#     print("No pattern found")

# codes = "123abc xyz789 gh12ij"

# # found a code that starts with a number and is followed by any alphanumeric characters
# regex_pattern = r"\d\w+" # use of raw string to say Python to interpret the string as a whole and not escape sequence


# try:
#     matches = re.search(regex_pattern,codes)
#     print(f"The pattern found is: {matches.group()}")
# except:
#     print("Could not find")

test_string = "the macguffin will arrive on June 21, 2023."
# we want to extract month, day and year all as seperate elements
patterns  = r"(\w+) (\d{1,2}), (\d{4})"

try:
    matches = re.search(patterns, test_string)
    print(f"The pattern found is: {matches.group(1)}")
    print(f"The pattern found is: {matches.group(2)}")
    print(f"The pattern found is: {matches.group(3)}")
except:
    print("Could not find")