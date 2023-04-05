# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from contacts.py")

def data():
    rows=db(db.contacts).select()
    return locals()

def filter():
    row1_count=db(db.contacts).count()

def add():
    form=SQLFORM(db.contacts).process()
    return locals()

def view():
    if request.args(0) is None:
        rows=db(db.contacts).select(orderby=db.contacts.last_name | db.contacts.first_name)
        return locals()
    else:
        letter=request.args(0)
        rows=db(db.contacts.last_name.startswitch(letter)).select(orderby=db.contacts.last_name | db.contacts.first_name)
        return locals()

def update():
    record=db.contacts(request.args(0)) or redirect(URL('view'))
    form = SQLFORM(db.contacts,record)
    if form.process.accepted():
        response.flash=T('record updated')
        
    else:
        response.flash=T('please fill up the form')    
        
        return locals()
