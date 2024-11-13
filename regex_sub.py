import re

# Example 1:
# imagine we have a list of user adresse and we want to replace the names by something else.

text: str = "Contact us at info@example.com or support@mywebsite.come"

regex = r"\w+@"

try:
    matches = re.findall(regex, text)
    anonymous = re.sub(regex, "user@", text)
    print(anonymous)
except:
    print("No match found")


# Example 2:
# imagine we have a piece of text containng dates in the format month-day-year and we want to convert them 
# to the format year-month-day.

dates_to_convert: str = "the event will take place on 02/14/2024. Please purchase tickets by 01/01/2024."
pattern: str= r"(\d{2})/(\d{2})/(\d{4})" # wraping in () to access those groups when substituting



try:
    formatted_text = re.sub(pattern, r"\3-\1-\2", dates_to_convert) # this what we mean by backreferenced !!!
    print(formatted_text)
except:
    print("No match found")