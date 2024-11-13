import re

def anonymize_snn(input_string: str) ->  str:
    """
    Exit a anonymize SNN
    """
    # check first if the SNN is correct
    regex_check = r"\d{3}-\d{2}-\d{3}"

    matches = re.search(regex_check, input_string)

    if  matches:
        changed_char = "***-**"
        sequence_to_change = r"\d{3}-\d{2}"
        return f"You anonymized SNN is: {re.sub(sequence_to_change, changed_char, input_string)}"
            
    else:
        return "Not a valid SNN ! Please check the input"


print(anonymize_snn(input_string=input("Please enter you social security number (SNN): ")))