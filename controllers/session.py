# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from session.py")

def set():
    session.name="sam"
    session.date="8/1/2015"
    session.membership="family"
    return locals()

def view():
    return locals()
