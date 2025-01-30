def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

string = "radar"
print("Is '{string}' a palindrome? {is_palindrome(string)}")

#This Python Code checks if a given string is a palindrome.The Code works by iterating through the first half of the string, comparing each character with its corresponding character from the end of the string by using negative indexing which starts from the back of the string. If any pair of characters do not match then the function immediately returns False. If all pairs match, the function returns True, indicating that the string is a palindrome. 
#A palindrome is a word, phrase, or sequence that reads the same forwards and backwards, ignoring spaces and punctuation.
