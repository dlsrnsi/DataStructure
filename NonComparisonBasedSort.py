__author__ = 'Ingoo'

'''
Bucket sort
work when keys are in small ranges
1. Make array of q queues, numbered from 0 to q-1
2. Enqueue each item key i goes in queue i
3. Concatenate queues in order : Theta(q+n) times
Theta(q)time initialize & concatenate bucket
Theta(n)time to put items in queue
If q in O(n) total is O(n) time
'''
def bucketSort(array) :
    for x in range(max(array)+1) :
        exec("queue%d = []" % x)
    for x in array :
        exec("queue%d.append(x)"% x)
    result = []
    for x in range(max(array)+1) :
        exec("if queue%d : result.append(queue%d)" % (x,x))
    print(result)

array = [55,33,43,1,35,5,7]
bucketSort(array)


'''
Counting Sort with Complete Items
input : Key + Associated value
1. Let x be input array of object with keys.
2. Count keys in x, make counts array
3. Do a scan, So counts[i] contain number of keys less than i
4. Let y be output array, counts[i] tells us first index of y to put items
5. When putting item with key i to y, add 1 to counts[i]
'''

def countingSort(array) :
    counts = [0] * (max([x[0] for x in array])+1)
    output = [0] * len(array)
    total = 0
    for x in range(len(counts)) :
        numberOfKey = 0
        for y in array :
            if y[0] == x :
                numberOfKey += 1
        counts[x] = total
        total += numberOfKey
    print(counts)
    for x in array :
        output[counts[x[0]]] = x[0]
        counts[x[0]] += 1
    print(output)

entryList = [(6,'hi'),(7,'everyone'),(3,'hello'),(0,'there?'),(3,'five'),(1,'night'),(5,'at'),
    (0,'the'),(3,'freddy'),(7, 'thanks')]
countingSort(entryList)

'''
Bucket sort & Counting sort take O(q+n) times
If q in O(n), they O(n) time.
Array : counting sort takes less memory
Linked list : bucket sort more natural
'''

'''
Radix Sort
sort 1,000 items in range 0,...,9999999999
provide q = 10 buckets.
1. Sort on first digit only
2. we could queue recursively on second digit, then on third digit, etc
Smaller subsets will be sorted inefficiently.
clever idea : keep numbers in one pile throughout sort,
              sort on last digit first, then next-to-last, up to most significant digit
Work because bucket&counting sort are STABLE
Faster if we sort on 2 digits at a time or 3
On computers, more natural to choose power-of-two radix like radix q = 256
q = # of buckets = radix of digit we use as sort key.
Each pass inspects log2(q) bits of each key
If all key represented in b bits, # of passes is b/log2(q)
Running time of radix sort is O((n+q)*(b/log2(q)))
Choose q in O(n), so each pass takes linear time
make q large enough, it will make # of passes small
choose q similar with n. Radix sort takes )(n + n*b/log(n)) time
int b is a constant radix sort takes linear time
Practical choice : make q be n rounded down to power of two
To keep memory use low : q is similar with sqt(n) to nearest power of two
'''