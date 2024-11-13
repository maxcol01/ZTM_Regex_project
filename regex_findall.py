import re

target_string: str = "the 1998 Football world cup was hosted by France. The next on in 2002 by Japan and South Korea. The most recent one by Quatar in 2022."
# extract all the years fro this sting:

regex: str = r"\d{4}"

try:
    matches = re.findall(regex, target_string)
    print(matches)
except:
    print("Not match found")


# Example 2:

text = "The cat goes meow, meoooow, meooow, meowwww, while the dog goes woof."

# finds the cat's sound

regex_cat = r"me+o+w+"
try:
    matches_cat = re.findall(regex_cat, text)
    print(matches_cat)
except:
    print("Not match found")