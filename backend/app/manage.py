#!/usr/bin/env python3

import argparse
from utils import process_file

#Create a parser object, prog= name of program, description=gives useser help
parser = argparse.ArgumentParser(prog="Training data Tools",description="Input the file path to the folder you want to organize.")

#adds argument-- if you need more then one args all multiple lines
parser.add_argument('file_path',type=str,help="Write the file path")

#parsers the arguments
args = parser.parse_args()

#once the args are parsered args.(the argument will bring the input into the script)
file_path = args.file_path
process_file(file_path)

