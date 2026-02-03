# image = [[1,1,0],[1,0,1],[0,0,0]]
# for i in image:
#     l = 0 
#     r = len(i) - 1
#     while l<=r:
#         i[l],i[r] = int(not(i[r])),int(not(i[l]))
#         l+=1
#         r-=1

# print(image)
# print(image==[[1,0,0],[0,1,0],[1,1,1]])\




def nine(digits):
    r = len(digits) - 1
    while digits[r] == 9:
        digits[r] = 0
        r-=1
    if r==-1:
        print(digits)
        digits = [1]+digits
        return digits
    else:
        print(r)
        print(digits,1)
        digits[r] +=1
        return digits
digits = [9,9,9]
r = len(digits) - 1
if digits[-1] != 9:
    digits[-1] += 1
    print(digits)
else:
    print(nine(digits))