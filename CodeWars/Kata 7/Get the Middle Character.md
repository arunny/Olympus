You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

```python
("test") should return "es"

("testing") should return "t"

("middle") should return "dd"

("A") should return "A"
```

#Output

The middle character(s) of the word represented as a string.

## Solution:

```python
def get_middle(s):

	if not len(s) % 2 == 0:
		return s[len(s) // 2]
	else:
		return s[len(s) // 2 - 1] + s[len(s) // 2]
```
