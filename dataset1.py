
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
    min = -1
    max = 1
    num = 0.1
    x = num*np.arange(int(((max-min)/num))+1)-1
    y = true_function(x)
    plt.plot(x,y)

def en2():
    min = -1
    max = 1
    num = 0.1
    np.random.seed(0)
    x = (max-min)*np.random.rand(int(((max-min)/num)))-1
    y = true_function(x)
    df = pd.DataFrame(data=x,columns=["観測点"])
    df["真値"] = y
    plt.scatter(x=df["観測点"],y=df["真値"],c="red")
    en1()

def main():
    en2()
    plt.show()
if __name__ == "__main__":
    main()
    doctest.testmod()
