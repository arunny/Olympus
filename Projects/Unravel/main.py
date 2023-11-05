#!/usr/bin/env python
import argparse
import sys

def encipher(msg: str, n: int):
    newMsg = ""

    for char in msg:
        if char.isalpha():
            if char.isupper():
                newMsg += chr((ord(char) - ord("A") + n) % 26 + ord("A"))
            else:
                newMsg += chr((ord(char) - ord("a") + n) % 26 + ord("a"))
        else:
            newMsg += char
    return newMsg

def decipher(msg: str, n: int): 
    newMsg = ""

    for char in msg:
        if char.isalpha():
            if char.isupper():
                newMsg += chr((ord(char) - ord("A") - n) % 26 + ord("A"))
            else:
                newMsg += chr((ord(char) - ord("a") - n) % 26 + ord("a"))
        else:
            newMsg += char
    return newMsg

def main():
    parser = argparse.ArgumentParser(
                        prog        = "./Unravel.py", 
                        description = "(De)cipher string n times")
    group  = parser.add_mutually_exclusive_group(required = True)
    group.add_argument("-e","--encipher",
                        dest   = "action",
                        action = "store_const",
                        const  = encipher,
                        help   = "encipher string n times forwards.")

    group.add_argument("-d", "--decipher",
                        dest   = "action", 
                        action = "store_const",
                        const  = decipher,
                        help   = "decipher string n times backwards.")

    parser.add_argument("-n",
                        metavar = "number",
                        type    = int,
                        default = 0,
                        help    = "shift string n times.")
    
    parser.add_argument("s", 
                        type    = str,
                        metavar = "string",
                        help    = "string to (de)cipher.")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    print(args.action(args.s, args.n))

if __name__ == "__main__":
    main()


