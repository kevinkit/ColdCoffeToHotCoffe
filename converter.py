# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 14:02:28 2017

@author: kevinkit


This file will convert from "old" caffe to new caffe,


supported Layers:
       
    old:           ...  new:
    
    layers         ...  layer
    
    CONVOLUTION    ... "Convolution"
    RELU           ... "Relu"
    LRN            ... "LRN"
    POOLING        ... "Pooling"
    INNER_PRODUCT  ... "InnerProduct"
    SOFTMAX        ... "Softmax"
"""


#Define the .prototxt
filename = "deploy.prototxt";


proto_file = open(filename,"r");
x = proto_file.readlines();
for i in range(0,len(x)):
    print x[i]
    if x[i] == "layers {\n": 
        x[i] = "layer {\n";

    if x != len(x)-1:
        if x[i] == "layers\n" and x[i+1] == "{\n": 
            x[i] = "layer\n";
 
    if x[i] == "  type: CONVOLUTION\n" or x[i] == "type: CONVOLUTION\n":
        x[i] = '  type: "Convolution"';

    if x[i] == "  type: RELU\n" or x[i] == "type: RELU\n":
        x[i] = '  type: "ReLU"';

    if x[i] == "  type: LRN\n" or x[i] == "type: LRN\n":
        x[i] = '  type: "LRN"';

    if x[i] == "  type: POOLING\n" or x[i] == "type: POOLING\n":
        x[i] = '  type: "Pooling"';

    if x[i] == "  type: INNER_PRODUCT\n" or x[i] == "type: INNER_PRODUCT\n":
        x[i] = '  type: "InnerProduct"';

    if x[i] == "  type: SOFTMAX\n" or x[i] == "type: SOFTMAX\n":
        x[i] = '  type: "Softmax"';


with open("new"+filename,"w") as new_file:
    for item in x:
        print item
        new_file.write("%s" % item);
    





