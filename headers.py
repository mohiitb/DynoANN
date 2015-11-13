# import headers here
from sklearn import preprocessing
from pybrain.structure import FeedForwardNetwork, FullConnection
from pybrain.structure.modules   import LinearLayer, SigmoidLayer, SoftmaxLayer, TanhLayer, BiasUnit
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

import numpy as np
import csv
import wx
import os
import sys
import time