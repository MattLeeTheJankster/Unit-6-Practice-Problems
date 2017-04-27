def sumlist(num):
   if len(num) == 1:
        return num[0]
   else:
        return num[0] + sumlist(num[1:])
			
######## Main Program #########
print(sumlist([1,3,5,7,9]))
