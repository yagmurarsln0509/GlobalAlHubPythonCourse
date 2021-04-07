#homeworkpart1
my_list = [2,3,5,7,6,1,4,9,0,3]
def swapHalf(my_list):
    l = int(len(my_list)/2)
    my_list[:l], my_list[l:] = my_list[l:], my_list[:l] 
    print(my_list) 
swapHalf(my_list)

#homeworkpart2
def evenNumbers(): 
    while  True :
        n = int(input('Bir tek basamaklı sayı giriniz: '))
        if n <10 and n>0 :
            break
    for i in range (0, n):
        if i %2 == 0:
            print(i)
evenNumbers()
