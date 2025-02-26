#!/usr/bin/env python
# coding: utf-8

# In[8]:


def tanh_activation(x):
    return (2 / (1+ (2.71828 ** (-2 * x))))  




b1, b2 = 0.5, 0.7
x1, x2 = 0.2, -0.3




w1, w2, w3, w4, w5, w6 = [simple_random(seed + i) for i in range(6)]




h1, h2 = tanh(x1 * w1 + x2 * w2 + b1), tanh(x1 * w3 + x2 * w4 + b1)
output = tanh(h1 * w5 + h2 * w6 + b2)




print(output)


# In[ ]:




