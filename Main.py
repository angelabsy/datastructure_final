from Node import Node
from Tree import RBT

import os

def inputData():
    data = []
    
    f = open('test01.txt', 'r')
    lines = f.readlines()
    for line in lines:
        inputNumber = int(line.strip())
        data.append(inputNumber)
    f.close()
    return data

def searchData():
    data = []
    f= open('search01.txt', 'r')
    lines = f.readlines()
    for line in lines:
        inputNumber = int(line.strip())
        data.append(inputNumber)
    f.close()
    return data

def main():

    iData = inputData()
    sData = searchData()
    print(iData,'\n',sData)
    rbt = RBT()

    for i in iData:
        if i > 0 :
            rbt.insert(i)
        elif i < 0:
            rbt.delete(-i)
        else:
            break

    f = open("output.txt", 'w')
    for i in sData:
        data = rbt.inorder(rbt.root)
               
        if i in data:
            data.append('NIL')
            a= str(data[data.index(i)-1]) +' '+ str(i) + ' '+ str(data[data.index(i)+1]) +'\n'
            f.write(a)
            print(data[data.index(i)-1], i, data[data.index(i)+1])
        else:
            data.append(i)
            data.sort()
            
            data.append('NIL')
            
            a = str(data[data.index(i)-1]) +' NIL '+ str(data[data.index(i)+1]) + '\n'
            f.write(a)
            print(data[data.index(i)-1], 'NIL', data[data.index(i)+1])

    f.close()
            
   

    

main()
