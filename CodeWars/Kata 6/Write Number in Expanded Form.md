
You will be given a number and you will need to return it as a string in [Expanded Form](https://www.mathsisfun.com/definitions/expanded-notation.html). For example:

```python
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```

NOTE: All numbers will be whole numbers greater than 0.


## Solution:

```python
def expanded_form(num):
	exform = []
    
    for idx, digit in enumerate(str(num)):
        if int(digit) > 0:
            addnum = digit + ("0" * (len(str(num)) - (idx + 1)))
            exform.append(addnum)
    return " + ".join(exf
```
