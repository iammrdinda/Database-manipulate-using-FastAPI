from fastapi import FastAPI,Body,Depends
from jose import jwt
import json
from app.model import PostSchema,UserLoginSchema,UserSchema
from app.auth.jwt_handler import signJWT
import imaplib
import email
from email.header import decode_header
from app.auth.jwt_bearer import jwtBearer
from db import *
from fastapi import Request,HTTPException

app=FastAPI()

def get_posts():
    data=all()
    return{"data":data}

@app.post("/create",dependencies=[Depends(jwtBearer())])
#def add_post(post: PostSchema):
def add_post(data: PostSchema):
    id =create(data)
    return {"inserted": True}

@app.get("/get/{item_id}")
def get_one_post(item_id:int):
    data=get_one(item_id)
    return {"data":data}
    
       
@app.post("/user/signup")
def user_signup(user : UserSchema=Body):
    id =create_for_userdetails_db(user)
    #return signJWT(user.email)

def check_user(credentials: UserLoginSchema):
    user = collection2.find_one({"email": credentials.email, "password": credentials.password})
    return user is not None
    
@app.post("/user/login")
def user_login(user: UserLoginSchema):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{ "error":"Invalid login details!"}