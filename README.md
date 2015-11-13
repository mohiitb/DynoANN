# DynoANN
Part of the Bachelor Thesis Project, covers both serial and parallel implementation of ANN along with UI. So far only serial implementation is included with following tunable parameters:
1) Upload file format: Univariate output is taken into consideration. CSV file format should be: out of N columns, last one is the output value.
2) Train:Test Data ratio can be set
3) Number of Hidden Layers/Neurons can also be set.
4) Other parameters inlclude Transfer Functions(so far 3), normalization of data, bias value, maximum allowed error(not yet completed) and maximum iteration numbers. 

Implementation:

Used Pybrain python library. Refer: http://pybrain.org/
