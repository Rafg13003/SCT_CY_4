import re

def assess_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))  # Matches any special character

    # Count the number of fulfilled criteria
    criteria_count = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Determine the strength based on the number of criteria met
    if criteria_count == 5:
        strength = "Very Strong"
    elif criteria_count == 4:
        strength = "Strong"
    elif criteria_count == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Return a dictionary with the details of the assessment
    return {
        "length": length_criteria,
        "uppercase": uppercase_criteria,
        "lowercase": lowercase_criteria,
        "digit": digit_criteria,
        "special_character": special_char_criteria,
        "strength": strength
    }

# Example usage
password = "P@ssw0rd123"
assessment = assess_password_strength(password)

print(f"Password Strength: {assessment['strength']}")
print("Criteria met:")
print(f"Length: {assessment['length']}")
print(f"Uppercase Letter: {assessment['uppercase']}")
print(f"Lowercase Letter: {assessment['lowercase']}")
print(f"Digit: {assessment['digit']}")
print(f"Special Character: {assessment['special_character']}")
