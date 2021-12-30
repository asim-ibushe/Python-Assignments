import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def slop(X,X_mean,Y,y_mean):
    numarator=0
    denominator=0

    for i in range(len(X)):
        numarator+=(X[i]-X_mean)*(Y[i]-y_mean)
        denominator+=(X[i]-X_mean)**2

    m=numarator/denominator
    return(m)

def main():
    name=pd.read_csv("Advertising.csv")

    X1=name["TV"].values
    X2=name["radio"].values
    X3=name["newspaper"].values
    Y=name["sales"]
    #print(X)
    #print(y)

    #finding mean
    x1_mean=np.mean(X1)
    x2_mean = np.mean(X2)
    x3_mean = np.mean(X3)
    y_mean=np.mean(Y)
    print("X1b:",x1_mean,"X2b:", x2_mean,"X3b:", x3_mean)

    #calling def slop to fine slop or finding m
    m1=slop(X1,x1_mean,Y,y_mean)
    m2=slop(X2,x2_mean,Y,y_mean)
    m3=slop(X3,x3_mean,Y,y_mean)
    print("M1",m1,"M2",m2,"M3",m3)

    #formula of multiline reg :y=c+m1x1 + m2x2 ,m3x3
    c=y_mean-(m1*x1_mean)+(m2*x2_mean)+(m3*x3_mean)

    print("C:",c)
    Numerator=0
    Denomenator=0
    Y_predicted=[]
    for i in range(len(X1)):
    	y_pred=c+m1*X1[i]+m2*X2[i]+m3*X3[i]
    	Y_predicted.append(y_pred)
    	Numerator=Numerator+(Y[i]-y_pred)**2
    	Denomenator=Denomenator+(Y[i]-y_mean)**2
    print('Goodness of fit(R square method=)',Numerator/Denomenator)	




if __name__ == '__main__':
    main()		
