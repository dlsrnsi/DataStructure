'''
Created on 2015. 2. 16.

@author: Ingoo
'''
'''
A Lower Bound for Comparison-Based Sorting
n numbers : each 1...n occuring once each
    How many orders can they be in?
    Answer : n! = 1*2*3*...*(n-2)*(n-1)*n
Each order is PERMUTATION of the numbers
    n! is possible permutation
n! = 1*2*..(n-1)*n <= n*n*...*n*n = n^n : upperbound
n! >= n/2*(n/2+1)*...*(n-1)*n >= (n/2)*(n/2)*...(n/2) = (n/2)^(n/2) : lower bound
log((n/2)^(n/2)) = (n/2)log(n/2) in theta(nlog(n)), log(n^n) = nlog(n)
so log(n!) = in theta(nlog(n))

Comparison-based sort : all decision based on comparing key
A correct sorting algorithm must generate a different sequence of true/false answer for
each permutation of 1..n
If algorithm asks <= d true/false questions, it generate <= 2^d different sequences of true/false answer
    so n! <= 2^d
       log2(n!) <= d
       -> d in omega(nlog(n))
Algorithm spends theta(d) time asking d questions
Every comparison-based sorting algorithm takes omega(nlog(n)) worst-case time
Fast algorithms make q-way decisions for large q
'''
# QuickSort
def quickSort(list):
    if len(list) <= 1 :
        return list
    v = list.pop(int(len(list)/2))
    l1 = []
    l2 = []
    for x in list :
        if x <= v :
            l1.append(x)
        else :
            l2.append(x)
    return quickSort(l1) + [v] + quickSort(l2)


def quickSortArray(array,left,right):
    index = partition(array, left, right)
    if left < index -1 :
        quickSortArray(array, left, index-1)
    if index < right :
        quickSortArray(array, index, right)
    return array

def partition(array,left,right):
    i = left
    j = right
    pivot = array[int((left+right)/2)]
    print(i,j,pivot, array)
    while(i<=j) :
        while(array[i]<pivot) :
            i +=1
        while(array[j]>pivot) :
            j -=1
        if(i<=j) :
            print("swap :", array[i], " with ", array[j])
            a = array[i]
            b = array[j]
            array[j] = a
            array[i] = b
            i +=1
            j -=1
            print("swap result : ",array)
    print(i)
    return i

list = [11,9,88,50,80,33, 6, 15, 18, 3,4,37, 35]
print(quickSort(list))
list = [3,8,0,9,4,7,5]
print(quickSortArray(list,0,len(list)-1))    