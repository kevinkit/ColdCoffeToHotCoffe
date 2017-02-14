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
filename = "VGG_CNN_M.prototxt";


proto_file = open(filename,"r");
x = proto_file.readlines();
for i in range(0,len(x)):
#    buf = str(x[i]).strip().rstrip();
    buf = x[i].strip().rstrip()
    uppers = [l for l in buf if l.isupper()];
#    x[i] =  x[i].strip().rstrip()
#    if 'input_dim' in x[i]:
#     	number = x[i].find(":") +1;
#	buf = x[i];
#	x[i] = 'dim:' + str(buf[number:len(buf)])    

    
    if buf == "layers {\n" or buf == "layers {":
        x[i] = "layer {\n";
    if x != len(x)-1:
        if buf == "layers\n" and x[i+1] == "{\n": 
            x[i] = "layer\n";
            continue;
    #no longer supported
    if 'blobs_lr' in x[i] or 'weight_decay' in x[i]:
	x[i] = ''    
    if buf == "type: CONVOLUTION\n" or buf == "type: CONVOLUTION":
        x[i] = '  type: "Convolution"\n';
        continue;
    if  buf == "type: RELU\n" or buf == "type: RELU" : 
        x[i] = '  type: "ReLU"\n';
        continue;
    if buf == "type: LRN\n" or buf == "type: LRN":
        x[i] = '  type: "LRN"\n';
        continue;
    if  buf  == "type: POOLING\n" or buf  == "type: POOLING":
        x[i] = '  type: "Pooling"\n';
        continue;
    if buf == "type: INNER_PRODUCT\n" or buf == "type: INNER_PRODUCT":
        x[i] = '  type: "InnerProduct"\n';
        continue;
    if buf  == "type: SOFTMAX\n" or buf == "type: SOFTMAX":
        x[i] = '  type: "Softmax"\n';
        continue;
    if buf == "type: DROPOUT\n" or buf == "type: DROPOUT":
        x[i] = '  type: "Dropout"\n';
        continue;
    
        
    if(len(uppers) > 2):
        print "did not change " + buf + " at line " + str(i) + ", if needed change manually";
        if "pool" in buf:
            print "Only pool, so do not change";
        
with open("new"+filename,"w") as new_file:
    for item in x:
        new_file.write("%s" % item);
    
