import customtkinter as Ctk
import requests
import json

Ctk.set_default_color_theme("dark-blue") 
app = Ctk.CTk()
app.geometry("900x800")
app.title("Sender.py")
def getRequest():
    url = targetGet.get()
    if not url.startswith("http"):
        url = "http://" + url
    r = requests.get(url)
    
    textbox.insert("0.0", f"Status: {r.status_code}\n\n{r.text}")
    textbox.pack()

textbox = Ctk.CTkTextbox(app, width=800, height=300)

## Get Frame
get = Ctk.CTkFrame(app)
getText = Ctk.CTkLabel(get, font=("Monsserat", 30), text=r"""
 Get
 """)
getText.pack()
text = Ctk.CTkLabel(get, font=("Monsserat", 30), text=r"""
 Target:
 """)
text.pack()
targetGet = Ctk.CTkEntry(get)
targetGet.pack()
sendGet = Ctk.CTkButton(get, fg_color="red", text="Send", command=getRequest)
sendGet.pack()

def getFrame():
    clear()
    get.pack(pady=20)

def postRequest():
    url = targetPost.get()
    if not url.startswith("http"):
        url = "http://" + url
    r = requests.post(url, json=json.loads(jsonPost.get()))
    
    textbox.insert("0.0", r.status_code)  
    textbox.pack()
## Post Frame
post = Ctk.CTkFrame(app)
postText = Ctk.CTkLabel(post, font=("Monsserat", 30), text=r"""
 Post
 """)
postText.pack()
text = Ctk.CTkLabel(post, font=("Monsserat", 30), text=r"""
 Target:
 """)
text.pack()
targetPost = Ctk.CTkEntry(post)
targetPost.pack()
text = Ctk.CTkLabel(post, font=("Monsserat", 30), text=r"""
 JSON:
 """)
text.pack()
jsonPost = Ctk.CTkEntry(post)
jsonPost.pack()
sendPost = Ctk.CTkButton(post, fg_color="red", text="Send", command=postRequest)
sendPost.pack()

def postFrame():
    clear()
    post.pack(pady=20)

def deleteRequest():
    url = targetDel.get()
    if not url.startswith("http"):
        url = "http://" + url
    r = requests.delete(url)
    textbox.insert("0.0", r.status_code)  
    textbox.pack()
## Delete Frame
delete = Ctk.CTkFrame(app)
deleteText = Ctk.CTkLabel(delete, font=("Monsserat", 30), text=r"""
 Delete
 """)
deleteText.pack()
text = Ctk.CTkLabel(delete, font=("Monsserat", 30), text=r"""
 Target:
 """)
text.pack()
targetDel = Ctk.CTkEntry(delete)
targetDel.pack()
sendDel = Ctk.CTkButton(delete, fg_color="red", text="Send", command=deleteRequest)
sendDel.pack()

def deleteFrame():
    clear()
    delete.pack(pady=20)

def putRequest():
    url = targetPut.get()
    if not url.startswith("http"):
        url = "http://" + url
    r = requests.put(url, json=json.loads(jsonPut.get()))
    
    textbox.insert("0.0", r.status_code)  
    textbox.pack()
## Put Frame
put = Ctk.CTkFrame(app)
putText = Ctk.CTkLabel(put, font=("Monsserat", 30), text=r"""
 Put
 """)
putText.pack()
text = Ctk.CTkLabel(put, font=("Monsserat", 30), text=r"""
 Target:
 """)
text.pack()
targetPut = Ctk.CTkEntry(put)
targetPut.pack()
text = Ctk.CTkLabel(put, font=("Monsserat", 30), text=r"""
 JSON:
 """)
text.pack()
jsonPut = Ctk.CTkEntry(put)
jsonPut.pack()
sendPut = Ctk.CTkButton(put, fg_color="red", text="Send", command=putRequest)
sendPut.pack()

def putFrame():
    clear()
    put.pack(pady=20)

def getBearerRequest():
    url = targetBearerGet.get()
    if not url.startswith("http"):
        url = "http://" + url
    r = requests.get(url, headers={
        "Authorization": BearerTokenGet.get()
    })
    
    textbox.insert("0.0", f"Status: {r.status_code}\n\n{r.text}")
    textbox.pack()


## Get With Bearer Frame
getBearer = Ctk.CTkFrame(app)
getBearerText = Ctk.CTkLabel(getBearer, font=("Monsserat", 30), text=r"""
 Get With Bearer
 """)
getBearerText.pack()
text = Ctk.CTkLabel(getBearer, font=("Monsserat", 30), text=r"""
 Target:
 """)
text.pack()
targetBearerGet = Ctk.CTkEntry(getBearer)
targetBearerGet.pack()
BearerText = Ctk.CTkLabel(getBearer, font=("Monsserat", 30), text=r"""
 Bearer Token:
 """)
BearerText.pack()
BearerTokenGet = Ctk.CTkEntry(getBearer)
BearerTokenGet.pack()
sendGet = Ctk.CTkButton(getBearer, fg_color="red", text="Send", command=getBearerRequest)
sendGet.pack()

def getBearerFrame():
    clear()
    getBearer.pack(pady=20)
## DELETE WITH BEARER
def deleteBearerRequest():
    url = targetBearerDelete.get()
    if not url.startswith("http"):
        url = "http://" + url
    r = requests.delete(url, headers={
        "Authorization": BearerTokenDelete.get()
    })
    
    textbox.insert("0.0", f"Status: {r.status_code}\n\n{r.text}")
    textbox.pack()


## Delete With Bearer Frame
deleteBearer = Ctk.CTkFrame(app)
deleteBearerText = Ctk.CTkLabel(deleteBearer, font=("Monsserat", 30), text=r"""
 Delete With Bearer
 """)
deleteBearerText.pack()
text = Ctk.CTkLabel(deleteBearer, font=("Monsserat", 30), text=r"""
 Target:
 """)
text.pack()
targetBearerDelete = Ctk.CTkEntry(deleteBearer)
targetBearerDelete.pack()
BearerText = Ctk.CTkLabel(deleteBearer, font=("Monsserat", 30), text=r"""
 Bearer Token:
 """)
BearerText.pack()
BearerTokenDelete = Ctk.CTkEntry(deleteBearer)
BearerTokenDelete.pack()
sendDelete = Ctk.CTkButton(deleteBearer, fg_color="red", text="Send", command=deleteBearerRequest)
sendDelete.pack()

def deleteBearerFrame():
    clear()
    deleteBearer.pack(pady=20)




def postBearerRequest():
    url = targetBearerPost.get()
    if not url.startswith("http"):
        url = "http://" + url
    r = requests.post(url, json=json.loads(jsonBearerPost.get()), headers={
        "Authorization": BearerTokenPost.get()
    })
    textbox.insert("0.0", f"Status: {r.status_code}\n\n{r.text}")
    textbox.pack()
## Post With Bearer Frame
postBearer = Ctk.CTkFrame(app)
postText = Ctk.CTkLabel(postBearer, font=("Monsserat", 30), text=r"""
 Post With Bearer
 """)
postText.pack()
text = Ctk.CTkLabel(postBearer, font=("Monsserat", 30), text=r"""
 Target:
 """)
text.pack()
targetPost = Ctk.CTkEntry(postBearer)
targetPost.pack()
text = Ctk.CTkLabel(postBearer, font=("Monsserat", 30), text=r"""
 JSON:
 """)
text.pack()
jsonBearerPost = Ctk.CTkEntry(postBearer)
jsonBearerPost.pack()
BearerText = Ctk.CTkLabel(postBearer, font=("Monsserat", 30), text=r"""
 Bearer Token:
 """)
BearerText.pack()
BearerTokenPost = Ctk.CTkEntry(postBearer)
BearerTokenPost.pack()
sendPost = Ctk.CTkButton(postBearer, fg_color="red", text="Send", command=postBearerRequest)
sendPost.pack()

def postBearerFrame():
    clear()
    postBearer.pack(pady=20)

def putBearerRequest():
    url = targetBearerPut.get()
    if not url.startswith("http"):
        url = "http://" + url
    r = requests.put(url, json=json.loads(jsonBearerPut.get()), headers={
        "Authorization": BearerTokenPut.get()
    })
    textbox.insert("0.0", f"Status: {r.status_code}\n\n{r.text}")
    textbox.pack()
## Put With Bearer Frame
putBearer = Ctk.CTkFrame(app)
putText = Ctk.CTkLabel(putBearer, font=("Monsserat", 30), text=r"""
 Put With Bearer
 """)
putText.pack()
text = Ctk.CTkLabel(putBearer, font=("Monsserat", 30), text=r"""
 Target:
 """)
text.pack()
targetBearerPut = Ctk.CTkEntry(putBearer)
targetBearerPut.pack()
text = Ctk.CTkLabel(putBearer, font=("Monsserat", 30), text=r"""
 JSON:
 """)
text.pack()
jsonBearerPut = Ctk.CTkEntry(putBearer)
jsonBearerPut.pack()
BearerText = Ctk.CTkLabel(putBearer, font=("Monsserat", 30), text=r"""
 Bearer Token:
 """)
BearerText.pack()
BearerTokenPut = Ctk.CTkEntry(putBearer)
BearerTokenPut.pack()
sendPut = Ctk.CTkButton(putBearer, fg_color="red", text="Send", command=putBearerRequest)
sendPut.pack()

def putBearerFrame():
    clear()
    putBearer.pack(pady=20)




def clear():
    get.pack_forget()
    post.pack_forget()
    delete.pack_forget()
    put.pack_forget()
    getBearer.pack_forget()
    postBearer.pack_forget()
    deleteBearer.pack_forget()
    putBearer.pack_forget()
    textbox.pack_forget()
senderText = Ctk.CTkLabel(app, font=("Monsserat", 30), text=r"""
Sender.py
""")
senderText.pack()
getBtn = Ctk.CTkButton(app, fg_color="red", text="Get", command=getFrame)
getBtn.pack(pady=5)
postBtn = Ctk.CTkButton(app, fg_color="red", text="Post", command=postFrame)
postBtn.pack(pady=5)
deleteBtn = Ctk.CTkButton(app, fg_color="red", text="Delete", command=deleteFrame)
deleteBtn.pack(pady=5)
putBtn = Ctk.CTkButton(app, fg_color="red", text="Put", command=putFrame)
putBtn.pack(pady=5)
getBtn = Ctk.CTkButton(app, fg_color="red", text="Get With Bearer Token", command=getBearerFrame)
getBtn.pack(pady=5)
postBtn = Ctk.CTkButton(app, fg_color="red", text="Post With Bearer Token", command=postBearerFrame)
postBtn.pack(pady=5)
deleteBtn = Ctk.CTkButton(app, fg_color="red", text="Delete With Bearer Token", command=deleteBearerFrame)
deleteBtn.pack(pady=5)
putBtn = Ctk.CTkButton(app, fg_color="red", text="Put With Bearer Token", command=putBearerFrame)
putBtn.pack(pady=5)





app.mainloop()