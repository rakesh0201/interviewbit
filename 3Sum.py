def threeSum(N):
    input_arr = []
    for i in range(0,N):
        x = int(input())
        input_arr.append(x)
                
    T = int(input("Enter target value :"))

    input_arr.sort()
    dist = 99999999
    first = second = third = 0
            
    for i in range(0,N-2):
        #x = input_arr[i]
        remaining = T - input_arr[i]
        j = i+1
        k = N-1
        while(j<k):
            sums = input_arr[j] + input_arr[k]
            dist1 = remaining - sums
            if(abs(dist1) < dist):
                dist = abs(dist1)
                first = i
                second = j
                third = k
            if(sums > remaining):
                k -= 1
            else :
                j += 1
                
    print(input_arr[first] , input_arr[second] ,input_arr[third])
    print(input_arr[first] + input_arr[second] +input_arr[third])

N = int(input("enter size of array:- "))
print("Enter {one} values".format(one = N))
threeSum(N)

    
    