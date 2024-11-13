import re

text = "Python is Fun. But pythons are scary !"

matches = re.findall("python", text, re.IGNORECASE)
#print(matches)

#Example 2

text_2  = """
Python, in your syntax we find delight,
Turning complex problems into something light.
python, your eloquence is truly a sight,
In the world of coding, you are knight.
"""

matches = re.findall("^python", text_2, re.IGNORECASE|re.MULTILINE)
print(matches)

# Example 3

text_3 = ""
match_3 = re.findall("light.+python", text_2, re.IGNORECASE|re.DOTALL)
print(match_3)