ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using `encode` is considered cheating.

## Solution:

```python
import string

def rot13(message):
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    encoded = ""
        
    for letter in message:
        if letter in alpha_lower:
            encoded += alpha_lower[(alpha_lower.index(letter) + 13) % 26]
        elif letter in alpha_upper:
            encoded += alpha_upper[(alpha_upper.index(letter) + 13) % 26]
        else:
            encoded += letter
    return encoded
```

## Soltuion 2:

```python

```