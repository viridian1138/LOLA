# -*- coding: utf-8 -*-

#$$strtCprt
#
# Lightweight OSGi-Like Activation for Python (LOLA)
# 
# Copyright (C) 2019 Thornton Green
# 
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, 
# see <http://www.gnu.org/licenses>.
# Additional permission under GNU GPL version 3 section 7
#
#
#$$endCprt


#
# Test code execution script using GUI.
#


import datetime;

import context;
import ibodypart;
import components;

from tkinter import *
from tkinter import ttk



components.start();




ws = Tk()
ws.title('LOLA Test GUI')
ws.geometry('700x500')



top_frame = Frame(ws)
top_frame.pack(fill=BOTH,expand=1)



scroll_frame = Frame(top_frame)
scroll_frame.pack(fill=BOTH,expand=1)



scroll_bar = Scrollbar(scroll_frame,orient='vertical')
scroll_bar.pack(side=RIGHT,fill=Y)



scroll_bar = Scrollbar(scroll_frame,orient='horizontal')
scroll_bar.pack(side=BOTTOM,fill=X)




treeview=ttk.Treeview(scroll_frame,yscrollcommand=scroll_bar.set,xscrollcommand=scroll_bar.set)



treeview.pack(fill=BOTH,expand=1)





scroll_bar.config(command=treeview.yview)
scroll_bar.config(command=treeview.xview)



treeview['columns']=('ID','Name','Percentage','Date')

treeview.column("#0", width=0, stretch=NO)
treeview.column("ID", anchor=CENTER, width=80)
treeview.column("Name", anchor=CENTER, width=80)
treeview.column("Percentage", anchor=CENTER, width=80)
treeview.column("Date", anchor=CENTER, width=80)




treeview.heading("#0", text="", anchor=CENTER)
treeview.heading("ID", text="ID", anchor=CENTER)
treeview.heading("Name", text="Name", anchor=CENTER)
treeview.heading("Percentage", text="Percentage", anchor=CENTER)
treeview.heading("Date", text="Date", anchor=CENTER)




lst = [];


def init():
            global lst

            for x in context.get():
                        if not isinstance(x, ibodypart.IBodyPart ): raise Exception('Bad interface');
                        lst.append( x );
            
            
            
            def sortFunc(x):
                        if not isinstance(x, ibodypart.IBodyPart ): raise Exception('Bad interface');
                        ddel = ( datetime.date.today() - x.getDate() ).days;
                        percentage = 100.0 * ddel / x.numDays()
                        return -percentage


            lst.sort(key=sortFunc)


            cnt = int( 0 );
            for x in lst:
                        if not isinstance(x, ibodypart.IBodyPart ): raise Exception('Bad interface');
                        name = x.name()
                        ddel = ( datetime.date.today() - x.getDate() ).days;
                        percentage = str( 100.0 * ddel / x.numDays() ) + "%"
                        if not isinstance(x.getDate(), datetime.date ): raise Exception('Bad interface');
                        date = str( x.getDate() )
                        id = str( cnt )
                        treeview.insert( parent='', index='end', iid=cnt , text='', values=( id , name , percentage , date ) )
                        cnt = cnt + 1;

init()



def button_press():

            global lst
            
            sels = treeview.focus()
            for index in sels:
                        sel = int( index )
                        lst[ sel ].setDate( datetime.date.today() );
                        children = treeview.get_children()
                        for child in children:
                                    treeview.delete(child)
                        lst = [];
                        init()



button = Button(top_frame, text="Set A Time To The Current Date", command=button_press)

button.pack(side=BOTTOM)




ws.mainloop()


print( "" );
print( "" );
components.stop();



