
import doctest
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.polynomial import roots
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
    en1()
    min = -1
    max = 1
    num = 0.1
    np.random.seed(0)
    x = (max-min)*np.random.rand(int(((max-min)/num)))-1
    y = true_function(x)
    df = pd.DataFrame(data=x,columns=["観測点"])
    df["真値"] = y
    plt.scatter(x=df["観測点"],y=df["真値"],c="red")
    return df


def en3():
    df = en2()
    min = -1
    max = 1
    num = 0.1
    np.random.seed(0)
    x = (max-min)*np.random.rand(int(((max-min)/num)))-1
    #平均値を0.0、分散を2.0
    y = np.random.normal(0,np.sqrt(2),20) / 2 #分散2.0が怪しい？ np.random.normalの値かそのものがおかしいのかな？ or 仕様
    df["観測値"] = y
    plt.scatter(x=x,y=y,c="green")
    print(df)


def en4():
    en3()
    pass
    
def main():
    en3()
    plt.show()
if __name__ == "__main__":
    main()
    doctest.testmod()
