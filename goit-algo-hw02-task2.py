from collections import deque

def is_palindrome(input_string):
    # Prepare the input string: lower case, no spaces
    prepare_string = ''.join(input_string.lower().split())

    # Create a two-way queue (deque). Add all characters
    char_deque = deque(prepare_string)

    while len(char_deque) > 1:
        # Compare characters at both ends
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Test
test_strings = [
    "The antique shop offers a treasure",
    "Visitors can browse through shelves",
    "No lemon no melon",
    "madam",
    "nureses nur"
]

for test in test_strings:
    print(f"'{test}' is a palindrome: {is_palindrome(test)}")