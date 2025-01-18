def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

# Example usage:
string = "radar"
print(f"Is '{string}' a palindrome? {is_palindrome(string)}")