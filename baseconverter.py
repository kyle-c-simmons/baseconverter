#!/usr/bin/env python

# Python 3
# Created by: Kyle Simmons
# Github: github.com/kyle-c-simmons

import argparse
import hashlib

parser = argparse.ArgumentParser(description="Base converter - Converts a VALUE to different bases")

# Setup the arguments
def handleArguments():
    parser.add_argument("value", help="Input a value to convert")
    parser.add_argument("-d", "--decimal", action="store_true", help="Convert inputted VALUE into decimal")
    parser.add_argument("-b", "--binary", action="store_true", help="Convert inputted VALUE into binary")
    parser.add_argument("-o", "--octal", action="store_true", help="Convert inputted VALUE into octal")
    parser.add_argument("-hex", "--hexadecimal", action="store_true", help="Convert inputted VALUE into hexadecimal")
    parser.add_argument("-m", "--md5", action="store_true", help="Returns a MD5 hash of the VALUE inputted")
    parser.add_argument("-s", "--sha1", action="store_true", help="Returns a SHA1 hash of the VALUE inputted")
    parser.add_argument("-a", "--all", action="store_true", help="Returns a MD5 / SHA1 hash and all converts to all numeric values.")

handleArguments()    
args = parser.parse_args()

# Converters
def converter(convert):
    converted = bytes(args.value, "ascii")
    print(' '.join([convert.format(x) for x in converted]),)

def displayArguments():
    
    print("\n========BASE CONVERTER========\n")

    # Numeric
    if args.decimal:
        print("\n---Converted to decimal...")
        print("Old value: " + args.value)
        print("New value: ")
        converter("{0:d}")

    if args.binary:
        print("\n---Converted to binary...")
        print("Old value: " + args.value)
        print("New value: ") 
        converter("{0:b}")

    if args.octal:
        print("\n---Converted to octal...")
        print("Old value: " + args.value)
        print("New value: ") 
        converter("{0:o}")

    if args.hexadecimal:
        print("\n---Converted to hexadecimal...")
        print("Old value: " + args.value)
        print("New value: ")
        converter("{0:X}")
        print("")
 
    # Hasing
    if args.md5:
        hashedmd5 = hashlib.md5(args.value.encode())
        print("\n---Converted to MD5...")
        print("Old value: " + args.value)
        print("New value: " + hashedmd5.hexdigest() + "\n")

    if args.sha1:
        hashedsha1 = hashlib.sha1(args.value.encode())
        print("\n---Converted to SHA1...")
        print("Old value: " + args.value)
        print("New value: " + hashedsha1.hexdigest() + "\n")

    # ALL
    if args.all:
        print("\n---Converted to decimal...")
        print("Old value: " + args.value)
        print("New value: ")
        converter("{0:d}")

        print("\n---Converted to binary...")
        print("Old value: " + args.value)
        print("New value: ") 
        converter("{0:b}")

        print("\n---Converted to octal...")
        print("Old value: " + args.value)
        print("New value: ") 
        converter("{0:o}")

        print("\n---Converted to hexadecimal...")
        print("Old value: " + args.value)
        print("New value: ")
        converter("{0:X}")
 
        hashedmd5 = hashlib.md5(args.value.encode())
        print("\n---Converted to MD5...")
        print("Old value: " + args.value)
        print("New value: " + hashedmd5.hexdigest() + "\n")

        hashedsha1 = hashlib.sha1(args.value.encode())
        print("\n---Converted to SHA1...")
        print("Old value: " + args.value)
        print("New value: " + hashedsha1.hexdigest() + "\n")

displayArguments()
