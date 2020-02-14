#Long short term memory 

import numpy as np
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from collections import Counter
import os
import clean2
import matplotlib.pyplot as plt
import scikitplot.plotters as skplt


top_words = 5000
epoch_num = 5
batch_size = 64