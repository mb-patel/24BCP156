def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  # Check if uppercase
            result += chr(ord(char) + 32)  # Convert to lowercase
        else:
            result += char  # Keep as is
    return result

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  # Check if lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Keep as is
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result += chr(ord(char) - 32)
        else:
            result += char  # Keep as is
    return result

# Example Usage
s = input("enter a string:")
print("Lowercase:", to_lowercase(s)) 
print("Uppercase:", to_uppercase(s))  
print("Toggle Case:", toggle_case(s))  
