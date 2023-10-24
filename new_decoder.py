import argparse
import sys
import base64

parser=argparse.ArgumentParser(description="Python script to decode base64 and base32"
                               ,usage="%(prog)s --b64/b32 cipher"
                               , epilog="Example: %(prog)s --b64 aGVsbG8=")
parser.add_argument("--b64",help="decode base64 encoding"
                    ,metavar="base64"
                    ,dest="b64"
                    ,nargs="+")
parser.add_argument("--b32",help="decode base32 encoding"
                    ,metavar="base32"  #metavar means full form 
                    ,dest="b32"
                    ,nargs="+")

parser.add_argument("-v"
                    ,help="version"   #metavar will not work in case of v 
                    ,action="version"
                    ,version="%(prog)s 1.0")

args=parser.parse_args()

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)


b64=args.b64
b32=args.b32



if b64:
    for i in b64:
        print((base64.b64decode(i)).decode())


if b32:
    for i in b32:
        print((base64.b32decode(i)).decode())
