#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib


# In[4]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        INCOME = request.form.get("INCOME")
        AGE = request.form.get("AGE")
        LOAN = request.form.get("LOAN")
        INCOME = float(INCOME)
        AGE = float(AGE)
        LOAN = float(LOAN)
        print(INCOME, AGE, LOAN)
        model1 = joblib.load("CART")
        pred1 = model1.predict([[INCOME, AGE, LOAN]])
        model2 = joblib.load("RF")
        pred2 = model2.predict([[INCOME, AGE, LOAN]])
        model3 = joblib.load("GB")
        pred3 = model3.predict([[INCOME, AGE, LOAN]])
        model4 = joblib.load("LM")
        pred4 = model4.predict([[INCOME, AGE, LOAN]])
        
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3, result4=pred4))
    else:
        return(render_template("index.html", result1="NA", result2="NA", result3="NA", result4="NA"))


# In[5]:


if __name__=="__main__":
    app.run()


