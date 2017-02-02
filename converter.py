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
    DROPOUT        ... "Dropout"
"""


#Define the .prototxt
filename = "deploy.prototxt";


proto_file = open(filename,"r");
x = proto_file.readlines();
for i in range(0,len(x)):
    buf = str(x[i]);
    uppers = [l for l in buf if l.isupper()];

    
    if x[i] == "layers {\n": 
        x[i] = "layer {\n";

    if x != len(x)-1:
        if x[i] == "layers\n" and x[i+1] == "{\n": 
            x[i] = "layer\n";
            continue;
    
    if x[i] == "  type: CONVOLUTION\n" or x[i] == "type: CONVOLUTION\n":
        x[i] = '  type: "Convolution"\n';
        continue;
    if x[i] == "  type: RELU\n" or x[i] == "type: RELU\n":
        x[i] = '  type: "ReLU"\n';
        continue;
    if x[i] == "  type: LRN\n" or x[i] == "type: LRN\n":
        x[i] = '  type: "LRN"\n';
        continue;
    if x[i] == "  type: POOLING\n" or x[i] == "type: POOLING\n":
        x[i] = '  type: "Pooling"\n';
        continue;
    if x[i] == "  type: INNER_PRODUCT\n" or x[i] == "type: INNER_PRODUCT\n":
        x[i] = '  type: "InnerProduct"\n';
        continue;
    if x[i] == "  type: SOFTMAX\n" or x[i] == "type: SOFTMAX\n":
        x[i] = '  type: "Softmax"\n';
        continue;
    if x[i] == "  type: DROPOUT\n" or x[i] == "type: DROPOUT\n":
        x[i] = '  type: "Dropout"\n';
        continue;
    
        
    if(len(uppers) > 2):
        print "did not change " + buf + " at line " + str(i) + ", if needed change manually";
        if "pool" in buf:
            print "Only pool, so do not change";
        
with open("new"+filename,"w") as new_file:
    for item in x:
        new_file.write("%s" % item);
    





