#kadan's algo
def kadane(arr,n):
  mx=arr[0]
  s=0
  for i in arr:
    s=s+i
    mx=max(s,mx)
    if s<0:
      s=0
  return mx

arr=[-1,-1,-1,2,8,-1,-2,-1]
s=kadane(arr,len(arr))
print(s)
print("changes are made")
print("hello")