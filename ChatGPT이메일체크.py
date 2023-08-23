# ChatGPT이메일체크

import re

# Regular expression pattern for matching email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Test strings containing email addresses
test_strings = [
    "john.doe@example.com",
    "jane_smith123@gmail.com",
    "contact@mywebsite.net",
    "invalid-email",
    "user@domain.invalid",
]

# Search for email addresses in test strings
for test_string in test_strings:
    match = re.search(email_pattern, test_string)
    if match:
        print(f"Found email address: {match.group()}")
    else:
        print(f"No email address found in: {test_string}")
