#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Task:
#scenario1:  
credit card limit based on salary.   


# In[ ]:


1----salry < 10000
credit limit ---salary*10(salry*discount)
2----salary>=10000 and <=30000
credit limit --- salary*20
3----salary >=30000
credit limit ---salary*30


# In[ ]:


logic
if elif else


# In[12]:


def credit_card_offer(salary):
    if salary < 10000 :
        print("your salary :",salary)
        credit_limit = salary * 10
        print("your credit limit:",credit_limit)
    elif salary >=10000 and salary <=30000 :
        print("your salary: ",salary)
        credit_limit = salary * 20
        print("your credit limit :",credit_limit)
    else: 
        credit_limit = salary * 30
        print("your salary: ",salary)
        print("your credit limit :",credit_limit)  


# In[13]:


credit_card_offer(5000)


# In[14]:


credit_card_offer(27000)


# In[15]:


credit_card_offer(40000)


# In[ ]:





# In[ ]:


#scenario2:Dmart discount offer.


# In[ ]:


pamount < 20000---pamount dis 20%
pamount >=20000 to <=40000---pamount dis 30%
pamount > 50000 --pamount dis 40%


# In[ ]:


def--function
conditions---if elif elif
function call


# In[ ]:


total--- pamount --discount---final bill


# In[ ]:


input
logic
output


# In[7]:


def mart_app(mart_type,pamount):
    #mart_type="Dmart"
    #pamount=int(input("Enter your purchase amount:"))
    print("your mart is",mart_type)
    if pamount<20000:
        print("your purchase amount is ",pamount)
        dis_amt=pamount*.20
        final_dis_amount=pamount-dis_amt
        print("your final payble amount is ",final_dis_amount)
    elif (pamount>=20000 and pamount<=40000):
        print("your purchase amount is ",pamount)
        dis_amt=pamount*.30
        final_dis_amount=pamount-dis_amt
        print("your final payble amount is ",final_dis_amount)
    elif pamount>50000:
        print("your purchase amount is ",pamount)
        dis_amt=pamount*.40
        final_dis_amount=pamount-dis_amt
        print("your final payble amount is ",final_dis_amount)
            
        


# In[8]:


mart_app("Dmart",18000)


# In[9]:


mart_app("Dmart",25000)


# In[10]:


mart_app("Dmart",60000)


# In[ ]:





# In[ ]:


# scenario3:Amazon online offer. 


# In[ ]:


amozon online app
product
electoric---20%
cloth---30%
footware---40%
product dis price
total blc price


# In[ ]:


functio---amazon offer
parameters---product,price


# In[ ]:


condition-- if elif else


# In[29]:


def amazon_offer(product,price):
    #product=input("Enter product type(electroic/cloth/footware):")
    #price=float(input("Enter product price:"))
    if product == "electoric":
        print("your product type is :", product)
        print("your  discount is 20%")
        product_dis=price*.20
        final_amount=price-product_dis
        print("your final amount is :",final_amount)
    elif product == "cloth" :
        print("your product type is :", product)
        print("your  discount is 30%")
        product_dis=price*.30
        final_amount=price-product_dis
        print("your final amount is :",final_amount)
    elif product == "footware" :
        print("your product type is :", product)
        print("your  discount is 40%")
        product_dis=price*.40
        final_amount=price-product_dis
        print("your final amount is :",final_amount)
    else:
        print("no offer available")
           


# In[30]:


amazon_offer ("electoric",2000)


# In[23]:


amazon_offer("cloth",3000)


# In[24]:


amazon_offer("footware",6000)


# In[25]:


amazon_offer("shoes",5000)

