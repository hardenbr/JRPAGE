import os
import math
import ROOT as rt
from  optparse  import OptionParser
import sys, os

#script options

parser.add_option("-f", "--file", dest="file",
                                      help="name of file consisting of pixel data",
                                      action="store",type="string",default="test.txt")

parser.add_option("-o", "--output", dest="output",
                                      help="name of file to output",
                                      action="store",type="string",default="test_out.txt")

(options, args) = parser.parse_args()


#Takes in a line of digits, returns representative TH2D 
def line_to_th2d(line):
    

