# quick sort
def partition(arr,s,e):
    pivot=arr[s]
    pi=s
    x=s+1
    while(x<=e):
        if arr[x]<pivot:
            pi+=1
        x+=1
    arr[pi],arr[s]=arr[s],arr[pi]
    while(s<pi and pi<e):
        while arr[s]<pivot:
            s+=1
        while arr[e]>pivot:
            e-=1
        if s<pi and pi<e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1


    return pi
def quicksort(arr,s,e):
    if e<=s:
        return
    p=partition(arr,s,e)
    quicksort(arr,s,p-1)
    quicksort(arr,p+1,e)
arr= [6,5,4,3,2,1,9,8,7]
quicksort(arr,0,8)
print(arr)
