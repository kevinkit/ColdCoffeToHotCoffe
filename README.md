# ColdCoffeToHotCoffe
Converts the old caffe format used in prototxt to describe the nets to the newer version. 


# Supported Layers:
The following layers are supported at the moment, more will follow. Feel free to contribute.


  old:           ...  new:

  layers         ...  layer

  CONVOLUTION    ... "Convolution"
  
  RELU           ... "Relu"
  
  LRN            ... "LRN"
  
  POOLING        ... "Pooling"
  
  INNER_PRODUCT  ... "InnerProduct"
  
  SOFTMAX        ... "Softmax"
  
An overview of all layers can be found at: http://caffe.berkeleyvision.org/tutorial/layers.html 
