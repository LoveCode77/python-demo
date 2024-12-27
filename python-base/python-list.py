import operator




if __name__ == "__main__":
    print("111")
    list1=['GooGle','Runood',19997,2000];
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]
    list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list2[-1])
    print(list4[0:-3])
    list4[0]="redddddd"
    print(list4[0])
    list4.append('gray')
    print(list4)
    print("删除list3-----------------------")
    del list3[2]
    print(list3)
    length=len(list4)
    print(length)
    list5=[1,2,3]+[4,5,6]
    print(list5)
    list6=["Hello"]*10
    print(list6)
    b="Hello1" in list6
    print(b)
    print(list6[1:])
    print(list6[:-2])
    print(list6[:])

    b2=operator.eq(list6,list5)
    print(b2)
    print(max(list5))
    print(min(list5))
    list5.clear()
    print(list5)
    list5=list6.copy()
    print(list5)
