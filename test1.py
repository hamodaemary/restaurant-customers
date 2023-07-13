from ttkbootstrap.constants import *
import ttkbootstrap
from ttkbootstrap import *
import sqlite3
#sqlite3
db = sqlite3.connect('customers.db')
cur = db.cursor()
cur.execute('CREATE TABLE if not exists mers(name text,phone integer,lo text,lp integer)')
#functions
def submiting():
        c = ent.get()
        v = ent1.get()
        b = ent2.get()
        n = ent3.get()
        cur.execute(f'insert into mers(name,phone,lo,lp) values("{c}",{v},"{b}",{n})')
        db.commit()
def fetching():
    for record in tree.get_children():
        tree.delete(record)
    count = 0
    y = cur.execute('SELECT name ,phone , lo , lp from mers ')
    for i in range(100000):
        o= y.fetchone()
        if o != None:
            tree.insert(parent='', index=END, iid=count, text='parent', values=o)
        count += 1
    db.commit()
def delete():
    p = ent.get()
    cur.execute(f'delete from mers where name="{p}"')
    db.commit()
def update():
    j = ent2.get()
    f = ent.get()
    q = ent3.get()
    cur.execute(f"update mers set lo='{j}',lp={q} where name='{f}' ")
def search():
    for record in tree.get_children():
        tree.delete(record)
    cv = search_entry.get()
    ll = cur.execute(f'SELECT name,phone,lo,lp from mers where name LIKE "{cv}"')
    xc=ll.fetchone()
    tree.insert(parent='',index=END,iid=1,text='parent',values=xc)
    db.commit()
#--------------
x = ttkbootstrap.Window(themename='solar')
x.title('customers')
x.geometry('1000x500')
cus = Label(text='customers',bootstyle='cyborg',font=('Impact',12))
cus.pack()
search_entry = Entry(bootstyle='cyborg')
search_entry.pack()
sb = Button(text='search',command=search,bootstyle='cyborg-outline')
sb.pack()
#frame
frm = Labelframe(bootstyle='solar',text='Control-Panel',width=100,height=450)
frm.place(x=1,y=1)
#labels-frame
lvl1 = Label(frm,text='name:',bootstyle='solar')
lvl1.place(x=1,y=20)
lvl2 = Label(frm,text='Phone:',bootstyle='solar')
lvl2.place(x=1,y=70)
lvl3 = Label(frm,text='Last-Order:',bootstyle='solar')
lvl3.place(x=1,y=120)
lvl4 = Label(frm,text='last-purchase:',bootstyle='solar')
lvl4.place(x=1,y=170)
#entries of frame
ent = Entry(frm,bootstyle='solar',width=13)
ent.place(x=1,y=40)
ent1 = Entry(frm,bootstyle='solar',width=13)
ent1.place(x=1,y=90)
ent2 = Entry(frm,bootstyle='solar',width=13)
ent2.place(x=1,y=140)
ent3 = Entry(frm,bootstyle='solar',width=13)
ent3.place(x=1,y=190)
#button
but = Button(frm,text='submit',bootstyle='success-outline',command=submiting)
but.place(x=15,y=240)
but1 = Button(frm,text='fetching',bootstyle='success-outline',command=fetching)
but1.place(x=15,y=280)
#con : button
dele =  Button(frm,text='delete',bootstyle='success-outline',command=delete)
dele.place(x=15,y=319)

#TreeView
tree = Treeview(bootstyle='solar')
tree['columns'] = ('name','phone','last-order','last-purchase')
#columns
tree.column('#0',width=1)
tree.column('name',width=120,anchor=CENTER,minwidth=25)
tree.column('phone',width=120,anchor=CENTER,minwidth=25)
tree.column('last-order',width=120,anchor=CENTER,minwidth=25)
tree.column('last-purchase',width=120,anchor=CENTER,minwidth=25)
#headings
tree.heading('name',text='name')
tree.heading('phone',text='phone',anchor=CENTER)
tree.heading('last-order',text='last-order',anchor=CENTER)
tree.heading('last-purchase',text='quantity',anchor=CENTER)
#---------------
tree.place(x=230,y=90)
x.mainloop()