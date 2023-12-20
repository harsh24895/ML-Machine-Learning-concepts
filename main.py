import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('./deeplearning.mplstyle')


def main():
# X would be for input variable( the size of 1000 sqf)
#y is the target price in 1000s dollor
    x = np.array([1.0,2.0])
    y = np.array([200.0,500.0])
    print(f"x = {x}")
    print(f"y = {y}")

#m is a number of training examples
# .shape parameter uses in the numpy
    print(f"x:{x.shape}")
    m = x.shape[0]
    print(f"number of training examples is: {m}")


    i = 0 #change this to 1 to see [x^1, y^1], it will display the values for position 1 in values
    x_i = x[i]
    y_i = y[i]
    print(f"(x^({i}),y^{i})) = ({x_i},{y_i}")


    #ploting the data using the matplotlib library

    #plot the data points
    plt.scatter(x,y,marker='x',c='r')
    #set the title
    plt.title("housing prices")
    #set the y-axis label
    plt.ylabel("price in 1000s of dollors")
    #set the x-axis label
    plt.ylabel('size(1000 sqft')
    plt.show()

    w=100
    b=200
    print(f"w:{w}")
    print(f"b:{b}")





if __name__ == '__main__':
    main()



































































































































































































































