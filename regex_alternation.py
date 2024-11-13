import re

# Example 1
text = "The cat and dog are friends."

regex = r"cat|dog"

matches = re.findall(regex, text)
#print(matches)

# Example 2

text_2 = "I will be on vacation from June 28 through July 2."
regex_2 = r"((June|July) \d{1,2})"

matches_2 = re.findall(regex_2, text_2)
#print(matches_2)

# Example 3

text_3 = "I will be on vacation from 06-28-2023 through 07/02/2023"
regex_3 = r"(\d{1,2}(-|/)\d{1,2}(-|/)\d{4})"
matches_3 =[item[0] for item in re.findall(regex_3,text_3)]
print(matches_3)