import numpy as np
rep = 10
between_t=np.zeros([rep])
enter_t=np.zeros([rep])
start_t=np.zeros([rep])
end_t=np.zeros([rep])
service_t=np.zeros([rep])
wiat_t=np.zeros([rep])
for i in range(rep):
   #hassanzadeh
   p1,p2,p3=0.2,0.5,0.3
   r1=np.random.rand(1,1)
   if r1<p1:
      between_t[i]=5
   elif r1<p1+p2:
      between_t[i]=3
   else:
      between_t[i]=6
   r2=np.random.rand(1,1)
   if r2<0.1:
      service_t[i]=7
   elif r2<0.1+.02+0.4:
      service_t[i]=4
   else:
      service_t[i]=3
   if i==0:
      enter_t[i]=0
   else:
      end_t[i]=enter_t[i - 1] +between_t[i]
   if end_t[i - 1] < enter_t[i]:
      start_t[i]=end_t[i]
   else:
      start_t[i]=end_t[i - 1]
      
   end_t[i]=start_t[i]+service_t[i]
   wiat_t[i]=start_t[i]-enter_t[i]
   print(wiat_t[i])            