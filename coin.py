import random
total_flips = 0 #số lần búng đồng xu
num_tails = 0 #số lần mặt sau xuất hiện
num_heads = 0 #số lần mặt trước xuất hiện
for _ in range (1000):
    #sinh số ngẫu nhiên nằm trong khoảng [0,1)
   n = random.random()
   if n < 0.5:
       num_tails = num_tails +1 
   else: 
       num_heads = num_heads +1
       
total_flips = total_flips +1 #không thuộc khối else  
