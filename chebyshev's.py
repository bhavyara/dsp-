
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
dp=np.float(input('enter the gain of pass band:'))#give input=0.8
ds=np.float(input('enter the gain of stop band:'))#give input=0.2
wp=np.float(input('enter stop band cutoff frequency:'))#give input=6183
ws=np.float(input('enter pass band cutoff frequency:'))#give input=31415 for better result
def che (dp,ds,ws,wp):
    n=0.5*(np.log(((1/np.square(dp)-1))/((1/np.square(ds))-1))/(np.log(wp/ws)))
    N=np.ceil(n)
    wc=wp/(((1/np.square(dp)-1)**(1/2*N)))
    return N,wc;










2


































































