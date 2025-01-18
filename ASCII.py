def ascii(s):
    values = []

    for char in s:
        ascii_value = 0
        for i in range(256):  
            if chr(i) == char: 
                ascii_value = i
                break
        values.append(ascii_value)

    return values

# Test the function
input_string = "Hello"
values = ascii(input_string)
print(f"ASCII values of '{input_string}': {values}")


#The ascii function takes a string as input and returns a list of ASCII values corresponding to each character in the string. It iterates through each character in the string and uses a loop to find the ASCII value by comparing the character to each possible ASCII value (from 0 to 255). Once a match is found, the ASCII value is added to the list 