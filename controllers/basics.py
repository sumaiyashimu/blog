# -*- coding: utf-8 -*-
# try something like

def helloworld():
    msg = "Hello, This is my first page "
    return locals()


def request_args():
    arg1=float(request.args(0))
    arg2=float(request.args(1))
    total = arg1 + arg2
    return locals()




def request_vars():
    num1=()
    num2=()
    total=()
    if request.post_vars:
        num1 = float (request.post_vars.num1)
        num2 = float (request.post_vars.num2)
        total = num1+num2
        response.flash=T("The total is"+str(total))
        return locals()
  


def request_object():
    app=request.application
    cntr=request.controller
    fx=request.function
    extn=request.extension
    folder=request.folder
    now=request.now
    client=request.client
    http=request.is_https
    return locals()
    
def index(): return dict(message="hello from basics.py")
