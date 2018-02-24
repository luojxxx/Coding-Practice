# https://www.hackerrank.com/challenges/ctci-bubble-sort
def bubblesort(arr):
    totalSwaps = 0
    runSwap = 1
    while runSwap != 0:
        
        runSwap = 0
        for idx in range(0,len(arr)-1):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                runSwap +=1

        totalSwaps += runSwap

    print('Array is sorted in %s swaps.' % totalSwaps)
    print('First Element: %s' % arr[0])
    print('Last Element: %s' % arr[-1])