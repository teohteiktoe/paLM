#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import google.generativeai as palm 

palm.configure(api_key="AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4")
model = {"model":"models/chat-bison-001"}

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("question")
        r = palm.chat(
            **model,
            messages=q
        )
        return(render_template("index.html",result=r.last))
    else:
        return(render_template("index.html",result="waiting.........."))

if __name__ == "__main__":
    app.run()


# In[ ]:




