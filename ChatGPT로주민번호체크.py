# ChatGPT로주민번호체크
#파이썬으로 한국의 주민번호를 체크하는 코드를 작성해줘
#총 14자리로 구성되어있고
#앞에서부터 6자리숫자, 그다음은 - 그다음은 7자리숫자로 구성되어있는데 
#앞에 6자리는 연도월일(yymmdd)로 구성되어있고 뒤쪽 7자리의 1번자리는 (1,2,3,4) 4개중 1개로 구성되어야해
import re

import re

def check_korean_ssn(ssn):
    # Regular expression pattern for matching Korean social security numbers
    ssn_pattern = r'^\d{6}-?[1-4]\d{6}$'

    # Check if the provided ssn matches the pattern
    if re.match(ssn_pattern, ssn):
        return True
    else:
        return False

# Test cases
test_ssns = [
    "951015-1234567",  # Valid
    "870201-1234567",  # Valid
    "920212-5678910",  # Invalid (first 6 digits don't represent a valid date)
    "990101-5678910",  # Invalid (invalid first digit of last 7 digits)
    "880123-8234567",  # Invalid (invalid first digit of last 7 digits)
    "123456-1234567",  # Invalid (invalid first digit of last 7 digits)
    "88012345678910",  # Invalid (missing hyphen)
    "880123-9234567",  # Invalid (invalid first digit of last 7 digits)
]

for ssn in test_ssns:
    if check_korean_ssn(ssn):
        print(f"{ssn} is a valid Korean social security number.")
    else:
        print(f"{ssn} is not a valid Korean social security number.")
