Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

```
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
```

## Solution:
```python
def solution(s):
    newlist = []
    text = ""
    
    for char in s:
        text += char
        if len(text) == 2:
            newlist.append(text)
            text = ""
    if text:
        newlist.append(text + "_")
    return newlist
```
