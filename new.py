def bs(arr,l,n,t):
    if n>=l:
        mid=(n+l)//2
        if mid==t:
            print(arr[mid])
            return mid
        elif arr[mid]>t:
            return bs(arr,l,mid-1,t)
        else:
            return bs(arr,mid+1,n,t)
    else:
        return -1
n,t=map(int,input().split())
arr=list(map(int,input().split()))
print(arr)
print(n,t)
r=bs(arr,0,n-1,t)
print(r)