import argparse
import pandas as pd
import numpy as np
import os,sys, re
sys.path.append(os.getcwd())
from funtaxacount import merge_orf_and_funtax, get_function_counts

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate function counts')
    parser.add_argument( 'orf', nargs='?',
                         type=argparse.FileType('r'))
    parser.add_argument( 'funtax', nargs='?',
                         type=argparse.FileType('r'))
    parser.add_argument( 'read_counts', nargs='?',
                         type=argparse.FileType('r'))

    parser.add_argument( '--function', choices=['ec','KO', 'COG'], default='ec') 
    parser.add_argument( '--out', nargs='?',
                        type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    function_counts = get_function_counts( args.function, args.orf.name, args.funtax.name, args.read_counts )
    function_counts.to_csv(args.out, sep='\t')
        
    
