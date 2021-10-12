
import doctest
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def true_function(x):

    '''
    >>> true_function(0) 
    0.0
    '''

    y = np.sin(np.pi * x * 0.8) * 10

    return y

def en1():
    x = np.arange(-1,1,0.1)
    y = true_function(x)
    plt.plot(x,y)
    plt.show()

def main():
    en1()

if __name__ == "__main__":
    main()
    doctest.testmod()
