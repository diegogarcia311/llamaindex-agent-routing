import re

def validate_response(text, expected_category=None):
    required_phrases = ["category:", "reason:", "GL code:"]

    for phrase in required_phrases:
        if phrase.lower() not in text.lower():
            print(f"Missing required phrase: {phrase}")
            return False

    if expected_category and expected_category.lower() not in text.lower():
        print(f"Expected category [{expected_category}] not found in response.")
        return False

    return True

