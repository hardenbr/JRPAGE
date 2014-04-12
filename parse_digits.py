import os
import math
import ROOT as rt
from  optparse  import OptionParser
import sys, os

#hard coded parameters
PIXEL_X = 28
PIXEL_Y = 28

parser = OptionParser()

#script options
parser.add_option("-f", "--file", dest="file",
                                      help="name of file consisting of pixel data",
                                      action="store",type="string",default="test.txt")

parser.add_option("-o", "--output", dest="output",
                                      help="name of file to output",
                                      action="store",type="string",default="test_out.txt")

parser.add_option("-v", "--verbos", dest="verbose",
                                      help="print more information",
                                      action="store",type="string",default="test_out.txt")

(options, args) = parser.parse_args()


#takes in a line of digits, returns a 2d list 
def line_to_matrix(line): 
    split = line.split(",")
    
    #remove the first elemnt it is just the label
    label = split[0]
    split = split[1:]

    matrix = []  #[x][y] coordinates

    #test that the line has the correct number of elements
    if len(split) != PIXEL_X * PIXEL_Y:
        print "ERROR: LINE DOES NOT SPLIT CORRECTLY"
        print "LEN SPLIT:", len(split)
        print split 
        exit(1)

    #append the line values to the matrix
    for yy in range(PIXEL_Y):
        matrix.append([])
        for xx in range(PIXEL_X):
            index = PIXEL_X * yy + xx
            matrix[yy].append(int(split[index]))

    return (label,matrix)

#builds a th2d from the pixel matrix
def matrix_to_th2d(matrix, name): 
    hist = rt.TH2D(name,name,PIXEL_X,0,PIXEL_X-1,PIXEL_Y,0,PIXEL_Y-1)
    for xx in range(PIXEL_X):
        for yy in range(PIXEL_Y):
            hist.Fill(yy,(PIXEL_X-xx),matrix[xx][yy])

    return hist

def draw_line(line): pass
    
#read in the pixels lines
in_file = open(options.file,"r")
in_file_lines = map(lambda x: x.rstrip("\r\n"),in_file.readlines())

out_file = rt.TFile("test.root","RECREATE")

#loop over lines
for line in in_file_lines[:10]:
    index = in_file_lines.index(line)

    if index % 100 == 0:
        print "analyzing index", index


    (label,matrix) = line_to_matrix(line)
    name = "hist_%i_label_%s" % (index,label)
    hist = matrix_to_th2d(matrix, name)
    print label

    hist.Write()

out_file.Close()

#pause to draw
#raw_input("RAW INPUT")
