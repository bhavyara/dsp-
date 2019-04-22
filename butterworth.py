
# coding: utf-8

# In[78]:


import numpy as np
import matplotlib.pyplot as plt
#dp=np.float(input('enter the gain of pass band:'))#give input=0.8
#ds=np.float(input('enter the gain of stop band:'))#give input=0.2
#wp=np.float(input('enter pass band cutoff frequency:'))#give input=2*np.pi*4000
#ws=np.float(input('enter stop band cutoff frequency:'))#give input=2*np.pi*5000 for better result
dp=0.8
ds=0.2
wp=2*np.pi*4000
ws=2*np.pi*5000
def butter (dp,ds,ws,wp):
    #n=0.5*(np.log(((1/np.square(dp)-1))/((1/np.square(ds))-1))/(np.log(wp/ws)))
    #N=np.ceil(n)
    #wc=wp/(((1/np.square(dp)-1)**(1/2*N)))
    #return float(N),float(wc);
    a=(1/(dp**2))-1
    b=(1/(ds**2))-1
    N=int(np.ceil(0.5*np.log10(a/b)/np.log10(wp/ws)))
    wc=wp/(a**(1/(2*N)))
    return float(N),float(wc)
           
    

N,wc=butter (dp,ds,ws,wp)
print (N,wc)
w=np.arange(0,np.pi*2*10000,10)
b=np.abs(1/((1+(w/wc)**(2*N))**0.5))
plt.plot(w,b)
plt.show()


