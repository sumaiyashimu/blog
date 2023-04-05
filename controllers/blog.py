# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from blog.py")

def post():
    form=SQLFORM(db.blog)
    if form.process().accepted:
        session.flash='form accepted'
        redirect(URL('Thanks'))
    elif form.errors:
        response.flash='form has error'
    else:
        response.flash='please fill out the form'
    return locals()

def view():
    rows=db(db.blog).select(db.blog.ALL)
    return locals()

def update():
    record=db.blog(request.args(0)) or redirect(URL('post'))
    form=SQLFORM(db.blog,record)
    if form.process().accepted:
        response.flash=T('Record updated')
    else:
        response.flash=T('Record complete the form')  
    return locals()


          
        
        
        