# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:50:30 2019

@author: MR
"""

from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox as box
import numpy as np
from random import random

#gui
class Gui1:
    
    def __init__(self,win,ops):
        self.win=win
        self.win.title('Wh AoS')
        self.frame=Frame(win)
        self.widgits()
        self.pos()
        self.commands()
        
    def widgits(self):        
        self.title=Label(self.win,text='Warhammer Age of Sigmar',font=('',12))
        self.btnSingle=Button(self.frame,text='Single')
        self.btnCompare=Button(self.frame,text='Compare')
        
    def pos(self):
        self.title.pack()
        self.frame.pack()
        self.btnSingle.pack(side=LEFT)
        self.btnCompare.pack(side=RIGHT)
        
    def commands(self):
        self.btnSingle.configure(command=lambda:self.setSingle())
        self.btnCompare.configure(command=lambda:self.setMulti())
        self.ops=Mode()
    
    def setSingle(self):
        ops.mode=1
        self.win.destroy()
        
    def setMulti(self):
        ops.mode=2
        self.win.destroy()
    
class Mode:
    mode=0
   
class Gui2:
    runnum=0
    
    def __init__(self,win):
        self.lines=1
        self.win=win
        self.win.title('Wh AoS')
        #self.frame=Frame(win)
        self.totframe=Frame(win)
        self.btnFrame=Frame(self.totframe)
        self.widgits()
        self.pos()
        self.addLine()
        self.commands()
        
    def widgits(self):
        self.canvas=Canvas(self.totframe)
        self.frame=Frame(self.canvas)
        self.scrollbar=Scrollbar(self.totframe,orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set,bg='blue')
        self.title=Label(self.totframe,text='Single unit ability',font=('',12))
        self.btnAdd=Button(self.btnFrame,text='Add line')
        self.btnDel=Button(self.btnFrame,text='Remove line')
        self.btnCal=Button(self.btnFrame,text='Calculate')
        self.txtotal=Label(self.btnFrame,text='Total')
        self.total=Label(self.btnFrame,text=0.0)
        self.totalmw=Label(self.btnFrame,text=0.0)
        self.txsize=Label(self.frame,text='Unit Size')
        self.txatk=Label(self.frame,text='Attacks')
        self.txth=Label(self.frame,text='To Hit')
        self.txtw=Label(self.frame,text='To Wound')
        self.txrend=Label(self.frame,text='Rend')
        self.txdam=Label(self.frame,text='Damage')
        self.txoutch=Label(self.frame,text='Chance')
        self.txoutuch=Label(self.frame,text='Unit Chance')
        self.txoutd=Label(self.frame,text='Damage Output')
        self.txouttd=Label(self.frame,text='Unit Damage')
        self.txoutmw=Label(self.frame,text='Mortal wounds')
        self.txoutumw=Label(self.frame,text='Unit Mortal Wounds')
        self.widgitset=[]
        self.widgitset2=[]
        
    def pos(self):
        self.totframe.pack()
        self.title.pack()
        self.btnFrame.pack()
        self.btnAdd.pack(side='left')
        self.btnDel.pack(side='left')
        self.btnCal.pack(side='left')
        self.totalmw.pack(side='right')
        self.total.pack(side='right')
        self.txtotal.pack(side='right')
        
        self.scrollbar.pack(side='right',fill=Y)
        self.canvas.pack(fill="both",expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>",self.onFrameConfigure)
        
        
        #self.frame.pack()
        self.txsize.grid(row=0,column=0)
        self.txatk.grid(row=0,column=1)
        self.txth.grid(row=0,column=2,columnspan=2)
        self.txtw.grid(row=0,column=4,columnspan=2)
        self.txrend.grid(row=0,column=6)
        self.txdam.grid(row=0,column=7)
        self.txoutch.grid(row=0,column=8)
        self.txoutuch.grid(row=0,column=9)
        self.txoutd.grid(row=0,column=10)
        self.txouttd.grid(row=0,column=11)
        self.txoutmw.grid(row=0,column=12)
        self.txoutumw.grid(row=0,column=13)
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def addLine(self):
        #alFrame=Frame(self.win)
        size=Combobox(self.frame,width=2)
        i=1
        value=[]
        while i<=50:
            value.append(i)
            i+=1
        size.configure(values=value)
        size.set(1)
        atk=Combobox(self.frame,width=4)
        i=1
        value=['D3','D6','2D3','2D6']
        while i<=12:
            value.append(i)
            i+=1
        atk.configure(values=value)
        atk.set(1)
        th=Combobox(self.frame,values=[2,3,4,5,6],width=1)
        th.set(4)
        pth=Label(self.frame,text='+')
        tw=Combobox(self.frame,values=[2,3,4,5,6],width=1)
        tw.set(4)
        ptw=Label(self.frame,text='+')
        rend=Combobox(self.frame,values=[0,-1,-2,-3],width=2)
        rend.set(0)
        dam=Combobox(self.frame,values=['D3','D6','2D3',1,2,3,4,5,6],width=4)
        dam.set(1)
        outch=Label(self.frame,text=0.0)#,width=6)
        outuch=Label(self.frame,text=0.0)#,width=12)
        outd=Label(self.frame,text=0.0)#,width=9)
        outtd=Label(self.frame,text=0.0)#,width=10)
        outmw=Label(self.frame,text=0.0)
        outumw=Label(self.frame,text=0.0)
        widgitline=[size,atk,th,pth,tw,ptw,rend,dam,outch,outuch,outd,outtd,outmw,outumw]
        self.widgitset.append(widgitline)
        
        #alFrame.pack()
        size.grid(row=self.lines,column=0)
        atk.grid(row=self.lines,column=1)
        th.grid(row=self.lines,column=2,sticky=E)
        pth.grid(row=self.lines,column=3,sticky=W)
        tw.grid(row=self.lines,column=4,sticky=E)
        ptw.grid(row=self.lines,column=5,sticky=W)
        rend.grid(row=self.lines,column=6)
        dam.grid(row=self.lines,column=7)
        outch.grid(row=self.lines,column=8)
        outuch.grid(row=self.lines,column=9)
        outd.grid(row=self.lines,column=10)
        outtd.grid(row=self.lines,column=11)
        outmw.grid(row=self.lines,column=12)
        outumw.grid(row=self.lines,column=13)
        
        #ops: re-roll 1s, re-roll 6s, re-roll all (hit+wound+attacks+damage), modifiers (all), 6s (hit+wound), multiply (hit+wound), mortal (hit+wound), rend mod (hit+wound), (6s dam x2 +1) add (6/6+ extra atk)
        opsFrame=Frame(self.frame)
        atkFrame=Frame(opsFrame)
        hitFrame=Frame(opsFrame)
        hit2Frame=Frame(opsFrame)
        woundFrame=Frame(opsFrame)
        wound2Frame=Frame(opsFrame)
        #rendFrame=Frame(opsFrame)
        #damageFrame=Frame(opsFrame)
        
        txatkop=Label(atkFrame,text='Attack options:')
        atkrrop=IntVar()
        cbatkrrop=Checkbutton(atkFrame,text='Re-roll',onvalue=1,offvalue=0,variable=atkrrop)
        cbatkmod=Combobox(atkFrame,values=[-3,-2,-1,0,1,2,3],width=2)
        cbatkmod.set(0)
        txatkmod=Label(atkFrame,text='Modifier')
        
        txrendop=Label(atkFrame,text='Rend options:')
        cbrendmod=Combobox(atkFrame,values=[-3,-2,-1,0],width=2)
        cbrendmod.set(0)
        txrendmod=Label(atkFrame,text='Modifier to')
        
        txdamop=Label(atkFrame,text='Damage options:')
        cbdammod=Combobox(atkFrame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'x2','x3'],width=4)
        cbdammod.set(0)
        txdammod=Label(atkFrame,text='Modifier to +')
        cbdammod2=Combobox(atkFrame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'-D3','-D6','-2D3','-2D6',-1,-2,-3,-4,-5,-6],width=5)
        cbdammod2.set(0)
        txdammod2=Label(atkFrame,text='Modifier')
        
        txsvop=Label(atkFrame,text='Save options:')
        cvop=IntVar()
        cbcvop=Checkbutton(atkFrame,text='Cover',onvalue=1,offvalue=0,variable=cvop)
        cbsvmod=Combobox(atkFrame,values=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6],width=5)
        cbsvmod.set(0)
        txsvmod=Label(atkFrame,text='Modifier')
        
        txhitop=Label(hitFrame,text='To hit options:')
        hitrrop=IntVar()
        cbhitrrop=Checkbutton(hitFrame,text='Re-roll',onvalue=1,offvalue=0,variable=hitrrop)
        hitrr1op=IntVar()
        cbhitrr1op=Checkbutton(hitFrame,text='Re-roll 1s',onvalue=1,offvalue=0,variable=hitrr1op)
        hitrr6op=IntVar()
        cbhitrr6op=Checkbutton(hitFrame,text='Re-roll 6s',onvalue=1,offvalue=0,variable=hitrr6op)
        cbhitmod=Combobox(hitFrame,values=[-3,-2,-1,0,1,2,3],width=2)
        cbhitmod.set(0)
        txhitmod=Label(hitFrame,text='Modifier')
        
        cbhit6op=Combobox(hitFrame,values=[0,2,3,'D3','D6','2D3','2D6'],width=4)
        cbhit6op.set(0)
        txhit6op=Label(hitFrame,text='6s x hits')
        cbhit6pop=Combobox(hitFrame,values=[0,2,3,'D3','D6','2D3','2D6'],width=4)
        cbhit6pop.set(0)
        txhit6pop=Label(hitFrame,text='6+ x hits')
        cbhitxop=Combobox(hitFrame,values=[0,2,3,'D3','D6','2D3','2D6'],width=4)
        cbhitxop.set(0)
        txhitxop=Label(hitFrame,text='hit x hits')
        
#        hit62op=IntVar()
#        cbhit62op=Checkbutton(hitFrame,text='6s 2 hits',onvalue=1,offvalue=0,variable=hit62op)
#        hit63op=IntVar()
#        cbhit63op=Checkbutton(hitFrame,text='6s 3 hits',onvalue=1,offvalue=0,variable=hit63op)
#        hit6p2op=IntVar()
#        cbhit6p2op=Checkbutton(hitFrame,text='6+ 2 hits',onvalue=1,offvalue=0,variable=hit6p2op)
#        hit6p3op=IntVar()
#        cbhit6p3op=Checkbutton(hitFrame,text='6+ 3 hits',onvalue=1,offvalue=0,variable=hit6p3op)
#        hitd3op=IntVar()
#        cbhitd3op=Checkbutton(hitFrame,text='hit D3 hits',onvalue=1,offvalue=0,variable=hitd3op)
#        hitd6op=IntVar()
#        cbhitd6op=Checkbutton(hitFrame,text='hit D6 hits',onvalue=1,offvalue=0,variable=hitd6op)
        
        hit6aop=IntVar()
        cbhit6aop=Checkbutton(hitFrame,text='6s +1a',onvalue=1,offvalue=0,variable=hit6aop)
        hit6paop=IntVar()
        cbhit6paop=Checkbutton(hitFrame,text='6+ +1a',onvalue=1,offvalue=0,variable=hit6paop)
        cbhit6rend=Combobox(hitFrame,values=[-3,-2,-1,0],width=2)
        cbhit6rend.set(0)
        txhit6rend=Label(hitFrame,text='6s Rend')
        cbhit6prend=Combobox(hitFrame,values=[-3,-2,-1,0],width=2)
        cbhit6prend.set(0)
        txhit6prend=Label(hitFrame,text='6+ Rend')
        cbhit6dam=Combobox(hit2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'x2','x3'],width=5)
        cbhit6dam.set(0)
        txhit6dam=Label(hit2Frame,text='6s Damage  modifier to +')
        cbhit6dam2=Combobox(hit2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6],width=5)
        cbhit6dam2.set(0)
        txhit6dam2=Label(hit2Frame,text='6s Damage  modifier')
        cbhit6pdam=Combobox(hit2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'x2','x3'],width=5)
        cbhit6pdam.set(0)
        txhit6pdam=Label(hit2Frame,text='6+ Damage  modifier to +')
        cbhit6pdam2=Combobox(hit2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6],width=5)
        cbhit6pdam2.set(0)
        txhit6pdam2=Label(hit2Frame,text='6+ Damage  modifier')
        cbhit6mw=Combobox(hit2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'D3 atk end','D6 atk end','2D3 atk end','2D6 atk end','1 atk end','2 atk end','3 atk end','4 atk end','5 atk end','6 atk end'],width=10)
        cbhit6mw.set(0)
        txhit6mw=Label(hit2Frame,text='6s mortal wound')
        cbhit6pmw=Combobox(hit2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'D3 atk end','D6 atk end','2D3 atk end','2D6 atk end','1 atk end','2 atk end','3 atk end','4 atk end','5 atk end','6 atk end'],width=10)
        cbhit6pmw.set(0)
        txhit6pmw=Label(hit2Frame,text='6+ mortal wound')
        cbhitmw=Combobox(hit2Frame,values=[0,'D3 atk end','D6 atk end','2D3 atk end','2D6 atk end','1 atk end','2 atk end','3 atk end','4 atk end','5 atk end','6 atk end'],width=10)
        cbhitmw.set(0)
        txhitmw=Label(hit2Frame,text='mortal wound hit')
        
        txwoundop=Label(woundFrame,text='To wound options:')
        woundrrop=IntVar()
        cbwoundrrop=Checkbutton(woundFrame,text='Re-roll',onvalue=1,offvalue=0,variable=woundrrop)
        woundrr1op=IntVar()
        cbwoundrr1op=Checkbutton(woundFrame,text='Re-roll 1s',onvalue=1,offvalue=0,variable=woundrr1op)
        woundrr6op=IntVar()
        cbwoundrr6op=Checkbutton(woundFrame,text='Re-roll 6s',onvalue=1,offvalue=0,variable=woundrr6op)
        
        cbwoundmod=Combobox(woundFrame,values=[-3,-2,-1,0,1,2,3],width=2)
        cbwoundmod.set(0)
        txwoundmod=Label(woundFrame,text='Modifier')
        
        cbwound6op=Combobox(woundFrame,values=[0,2,3,'D3','D6','2D3','2D6'],width=4)
        cbwound6op.set(0)
        txwound6op=Label(woundFrame,text='6s x wounds')
        cbwound6pop=Combobox(woundFrame,values=[0,2,3,'D3','D6','2D3','2D6'],width=4)
        cbwound6pop.set(0)
        txwound6pop=Label(woundFrame,text='6+ x wounds')
        cbwoundxop=Combobox(woundFrame,values=[0,2,3,'D3','D6','2D3','2D6'],width=4)
        cbwoundxop.set(0)
        txwoundxop=Label(woundFrame,text='wound x wounds')
        
#        wound62op=IntVar()
#        cbwound62op=Checkbutton(woundFrame,text='6s 2 wounds',onvalue=1,offvalue=0,variable=wound62op)
#        wound63op=IntVar()
#        cbwound63op=Checkbutton(woundFrame,text='6s 3 wounds',onvalue=1,offvalue=0,variable=wound63op)
#        wound6p2op=IntVar()
#        cbwound6p2op=Checkbutton(woundFrame,text='6+ 2 wound',onvalue=1,offvalue=0,variable=wound6p2op)
#        wound6p3op=IntVar()
#        cbwound6p3op=Checkbutton(woundFrame,text='6+ 3 wound',onvalue=1,offvalue=0,variable=wound6p3op)
#        woundd3op=IntVar()
#        cbwoundd3op=Checkbutton(woundFrame,text='wound D3 wounds',onvalue=1,offvalue=0,variable=woundd3op)
#        woundd6op=IntVar()
#        cbwoundd6op=Checkbutton(woundFrame,text='wound D6 wounds',onvalue=1,offvalue=0,variable=woundd6op)
        
        wound6aop=IntVar()
        cbwound6aop=Checkbutton(woundFrame,text='6s +1a',onvalue=1,offvalue=0,variable=wound6aop)
        wound6paop=IntVar()
        cbwound6paop=Checkbutton(woundFrame,text='6+ +1a',onvalue=1,offvalue=0,variable=wound6paop)
        cbwound6rend=Combobox(woundFrame,values=[-3,-2,-1,0],width=2)
        cbwound6rend.set(0)
        txwound6rend=Label(woundFrame,text='6s Rend')
        cbwound6prend=Combobox(woundFrame,values=[-3,-2,-1,0],width=2)
        cbwound6prend.set(0)
        txwound6prend=Label(woundFrame,text='6+ Rend')
        cbwound6dam=Combobox(wound2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'x2','x3'],width=5)
        cbwound6dam.set(0)
        txwound6dam=Label(wound2Frame,text='6s Damage  modifier to +')
        cbwound6dam2=Combobox(wound2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6],width=5)
        cbwound6dam2.set(0)
        txwound6dam2=Label(wound2Frame,text='6s Damage  modifier')
        cbwound6pdam=Combobox(wound2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'x2','x3'],width=5)
        cbwound6pdam.set(0)
        txwound6pdam=Label(wound2Frame,text='6+ Damage  modifier to +')
        cbwound6pdam2=Combobox(wound2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6],width=5)
        cbwound6pdam2.set(0)
        txwound6pdam2=Label(wound2Frame,text='6+ Damage  modifier')
        cbwound6mw=Combobox(wound2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'D3 atk end','D6 atk end','2D3 atk end','2D6 atk end','1 atk end','2 atk end','3 atk end','4 atk end','5 atk end','6 atk end'],width=10)
        cbwound6mw.set(0)
        txwound6mw=Label(wound2Frame,text='6s mortal wound')
        cbwound6pmw=Combobox(wound2Frame,values=['D3','D6','2D3','2D6',0,1,2,3,4,5,6,'D3 atk end','D6 atk end','2D3 atk end','2D6 atk end','1 atk end','2 atk end','3 atk end','4 atk end','5 atk end','6 atk end'],width=10)
        cbwound6pmw.set(0)
        txwound6pmw=Label(wound2Frame,text='6+ mortal wound')
        cbwoundmw=Combobox(wound2Frame,values=[0,'D3 atk end','D6 atk end','2D3 atk end','2D6 atk end','1 atk end','2 atk end','3 atk end','4 atk end','5 atk end','6 atk end'],width=10)
        cbwoundmw.set(0)
        txwoundmw=Label(wound2Frame,text='mortal wound wound')
        
        widgitline2={'txatkop':txatkop,'cbatkrrop':cbatkrrop,'atkrrop':atkrrop,'cbatkmod':cbatkmod,'txatkmod':txatkmod,'txrendop':txrendop,'cbrendmod':cbrendmod,'txrendmod':txrendmod,'txdamop':txdamop,'cbdammod':cbdammod,'txdammod':txdammod,'cbdammod2':cbdammod2,'txdammod2':txdammod2,'txsvop':txsvop,'cvop':cvop,'cbcvop':cbcvop,'cbsvmod':cbsvmod,'txsvmod':txsvmod,
                     'txhitop':txhitop,'cbhitrrop':cbhitrrop,'hitrrop':hitrrop,'cbhitrr1op':cbhitrr1op,'hitrr1op':hitrr1op,'cbhitrr6op':cbhitrr6op,'hitrr6op':hitrr6op,'cbhitmod':cbhitmod,'txhitmod':txhitmod,'cbhit6op':cbhit6op,'txhit6op':txhit6op,'cbhit6pop':cbhit6pop,'txhit6pop':txhit6pop,'cbhitxop':cbhitxop,'txhitxop':txhitxop,'cbhit6aop':cbhit6aop,'hit6aop':hit6aop,'cbhit6paop':cbhit6paop,'hit6paop':hit6paop,'cbhit6rend':cbhit6rend,'txhit6rend':txhit6rend,'cbhit6prend':cbhit6prend,'txhit6prend':txhit6prend,'cbhit6dam':cbhit6dam,'txhit6dam':txhit6dam,'cbhit6dam2':cbhit6dam2,'txhit6dam2':txhit6dam2,'cbhit6pdam':cbhit6pdam,'txhit6pdam':txhit6pdam,'cbhit6pdam2':cbhit6pdam2,'txhit6pdam2':txhit6pdam2,'cbhit6mw':cbhit6mw,'txhit6mw':txhit6mw,'cbhit6pmw':cbhit6pmw,'txhit6pmw':txhit6pmw,'cbhitmw':cbhitmw,'txhitmw':txhitmw,
                     'txwoundop':txwoundop,'cbwoundrrop':cbwoundrrop,'woundrrop':woundrrop,'cbwoundrr1op':cbwoundrr1op,'woundrr1op':woundrr1op,'cbwoundrr6op':cbwoundrr6op,'woundrr6op':woundrr6op,'cbwoundmod':cbwoundmod,'txwoundmod':txwoundmod,'cbwound6op':cbwound6op,'txwound6op':txwound6op,'cbwound6pop':cbwound6pop,'txwound6pop':txwound6pop,'cbwoundxop':cbwoundxop,'txwoundxop':txwoundxop,'cbwound6aop':cbwound6aop,'wound6aop':wound6aop,'cbwoun6paop':cbwound6paop,'wound6paop':wound6paop,'cbwound6rend':cbwound6rend,'txwound6rend':txwound6rend,'cbwound6prend':cbwound6prend,'txwound6prend':txwound6prend,'cbwound6dam':cbwound6dam,'txwound6dam':txwound6dam,'cbwound6dam2':cbwound6dam2,'txwound6dam2':txwound6dam2,'cbwound6pdam':cbwound6pdam,'txwound6pdam':txwound6pdam,'cbwound6pdam2':cbwound6pdam2,'txwound6pdam2':txwound6pdam2,'cbwound6mw':cbwound6mw,'txwound6mw':txwound6mw,'cbwound6pmw':cbwound6pmw,'txwound6pmw':txwound6pmw,'cbwoundmw':cbwoundmw,'txwoundmw':txwoundmw,
                     'opsFrame':opsFrame,'atkFrame':atkFrame,'hitFrame':hitFrame,'hit2Frame':hit2Frame,'woundFrame':woundFrame,'wound2Frame':wound2Frame}
        
        self.widgitset2.append(widgitline2)
        
        opsFrame.grid(row=self.lines+1,column=0,columnspan=14)
        
        atkFrame.pack()
        txatkop.pack(side='left')
        cbatkrrop.pack(side='left')
        cbatkmod.pack(side='left')
        txatkmod.pack(side='left')
        txrendop.pack(side='left')
        cbrendmod.pack(side='left')
        txrendmod.pack(side='left')
        txdamop.pack(side='left')
        cbdammod.pack(side='left')
        txdammod.pack(side='left')
        cbdammod2.pack(side='left')
        txdammod2.pack(side='left')
        txsvop.pack(side='left')
        cbcvop.pack(side='left')
        cbsvmod.pack(side='left')
        txsvmod.pack(side='left')

        hitFrame.pack()
        hit2Frame.pack()
        txhitop.pack(side='left')
        cbhitrrop.pack(side='left')
        cbhitrr1op.pack(side='left')
        cbhitrr6op.pack(side='left')
        #cbhit62op.pack(side='left')
        #cbhit63op.pack(side='left')
        cbhitmod.pack(side='left')
        txhitmod.pack(side='left')
        cbhit6op.pack(side='left')
        txhit6op.pack(side='left')
        cbhit6pop.pack(side='left')
        txhit6pop.pack(side='left')
        cbhitxop.pack(side='left')
        txhitxop.pack(side='left')
        #cbhit6p2op.pack(side='left')
        #cbhit6p3op.pack(side='left')
        #cbhitd3op.pack(side='left')
        #cbhitd6op.pack(side='left')
        cbhit6aop.pack(side='left')
        cbhit6paop.pack(side='left')
        cbhit6rend.pack(side='left')
        txhit6rend.pack(side='left')
        cbhit6prend.pack(side='left')
        txhit6prend.pack(side='left')
        cbhit6dam.pack(side='left')
        txhit6dam.pack(side='left')
        cbhit6dam2.pack(side='left')
        txhit6dam2.pack(side='left')
        cbhit6pdam.pack(side='left')
        txhit6pdam.pack(side='left')
        cbhit6pdam2.pack(side='left')
        txhit6pdam2.pack(side='left')
        cbhit6mw.pack(side='left')
        txhit6mw.pack(side='left')
        cbhit6pmw.pack(side='left')
        txhit6pmw.pack(side='left')
        cbhitmw.pack(side='left')
        txhitmw.pack(side='left')
        
        woundFrame.pack()
        wound2Frame.pack()
        txwoundop.pack(side='left')
        cbwoundrrop.pack(side='left')
        cbwoundrr1op.pack(side='left')
        cbwoundrr6op.pack(side='left')
        #cbwound62op.pack(side='left')
        #cbwound63op.pack(side='left')
        cbwoundmod.pack(side='left')
        txwoundmod.pack(side='left')
        cbwound6op.pack(side='left')
        txwound6op.pack(side='left')
        cbwound6pop.pack(side='left')
        txwound6pop.pack(side='left')
        cbwoundxop.pack(side='left')
        txwoundxop.pack(side='left')
        #cbwound6p2op.pack(side='left')
        #cbwound6p3op.pack(side='left')
        #cbwoundd3op.pack(side='left')
        #cbwoundd6op.pack(side='left')
        cbwound6aop.pack(side='left')
        cbwound6paop.pack(side='left')
        cbwound6rend.pack(side='left')
        txwound6rend.pack(side='left')
        cbwound6prend.pack(side='left')
        txwound6prend.pack(side='left')
        cbwound6dam.pack(side='left')
        txwound6dam.pack(side='left')
        cbwound6dam2.pack(side='left')
        txwound6dam2.pack(side='left')
        cbwound6pdam.pack(side='left')
        txwound6pdam.pack(side='left')
        cbwound6pdam2.pack(side='left')
        txwound6pdam2.pack(side='left')
        cbwound6mw.pack(side='left')
        txwound6mw.pack(side='left')
        cbwound6pmw.pack(side='left')
        txwound6pmw.pack(side='left')
        cbwoundmw.pack(side='left')
        txwoundmw.pack(side='left')
        
        self.lines+=2
        self.btnDel.configure(state=NORMAL)
        
        self.sizerest()
        
    def sizerest(self):
        self.frame.update()
        h=self.frame.winfo_height()
        w=self.frame.winfo_width()
        self.canvas.configure(width=w,height=h)
        #print(h,w)
        
    def removeLine(self):
        for x in self.widgitset[-1]:
            x.destroy()
        for y in self.widgitset2[-1].copy():
            try:
                self.widgitset2[-1][y].destroy()
            except Exception:
                del self.widgitset2[-1][y]
        self.widgitset.pop()
        self.widgitset2.pop()
        self.lines-=2
        if self.lines==3:
            self.btnDel.configure(state=DISABLED)
        self.sizerest()
    
    def roll(self,values,rolls,results):
        i=0
        while i<rolls:
                a=int(random()*6+1)
                #results[a-1]+=1
                values[i]=a
                #effects.append(0)
                i+=1
                
        j=0
        while j<6:
            results[j]=values.count(j+1)
            j+=1
        b=max(results)
        c=min(results)
        diff=np.round((b-c)/rolls*100,3)
        print('rolls 1-6',results,'total',rolls,'variance',diff,'%')
        return values
    
    def calculate(self):
        Gui2.runnum+=1
        print('\nrun number',Gui2.runnum)
        total=0
        totalmw=0
        ii=0
        while ii<len(self.widgitset):
            print('weapon',ii+1,'total',len(self.widgitset))
            line=self.widgitset[ii]
            line2=self.widgitset2[ii]
        #for line in self.widgitset:
            #get roll
            rolls=6**7
            results=[0,0,0,0,0,0]
            values=[0]*rolls
            effects=[0]*rolls
            mw=[0,0] #instances,total
            
#            for x in values:
#                effects.append(0)
            
            #hit
            values,effects,mw=self.tohit(line,line2,values,effects,mw,results,rolls)
            print('start',rolls,'end',len(values))
            h=len(values)/rolls
            print('hit',len(values)/rolls,h,'mortal wounds',mw[1])#review
            #multi hits
            values,effects=self.multi6s(values,effects,line2,'hit')
            w=s=1
            #wound
            if len(values)!=0:
                a=len(values)
                values,effects,mw=self.towound(line,line2,values,effects,mw,results)
                print('start',rolls,'end',len(values))
                w=len(values)/a
                print('wound',len(values)/rolls,w,'mortal wounds',mw[1])
                #multi wounds
                values,effects=self.multi6s(values,effects,line2,'wound')
            #saves
            if len(values)!=0:
                a=len(values)
                values,effects=self.tosave(values,effects,results,line,line2)
                s=len(values)/a
                print('save fails',len(values)/rolls,s)#mw[0]
            
            print('sucess chance',len(values)/rolls,h*w*s,'mortal wounds',mw[1])
            model=len(values)/rolls*int(line[1].get())
            modelmw=(mw[1]*int(line[1].get()))/rolls
            print('model chance',model,'mortal wounds',modelmw)
            unit=model*int(line[0].get())
            unitmw=modelmw*int(line[0].get())
            print('unit chance',unit,'mortal wounds',unitmw)
            line[8].configure(text='%.5f'%model)
            line[9].configure(text='%.5f'%unit)
            line[12].configure(text='%.5f'%modelmw)
            line[13].configure(text='%.5f'%unitmw)
            
            #damage
            if len(values)!=0:
                dam=self.todamage(values,effects,line,line2)/len(values)
                print('damage',dam)
                damagemodel=dam*model
                damageunit=unit*dam
                print('model damage',damagemodel)
                print('unit damage',damageunit)
                line[10].configure(text='%.5f'%damagemodel)
                line[11].configure(text='%.5f'%damageunit)
            
                total+=damageunit
            totalmw+=unitmw
            
            ii+=1
            #widgitline[size,atk,th,pth,tw,ptw,rend,dam,outch,outuch,outd,outtd]
        self.total.configure(text='%.5f'%total)
        self.totalmw.configure(text='%.5f'%totalmw)
            
    def tohit(self,line,line2,values,effects,mw,results,rolls):
        #hit
        values=self.roll(values,rolls,results)
        hittarget=int(line[2].get())
        mod=int(line2['cbhitmod'].get())
        rerolled=[]
        effectsr=[]
        #re-rolls: yours then oppoenents
        #re-roll 1s
        if line2['hitrr1op'].get()==1:
            values,rerolled,effects,effectsr=self.reroll1s(values,rerolled,effects,effectsr)
        #re-roll failed (before mod)
        if line2['hitrrop'].get()==1:
            values,rerolled,effects,effectsr=self.rerollfail(values,rerolled,hittarget,mod,effects,effectsr)
        #re-roll 6s
        if line2['hitrr6op'].get()==1:
            values,rerolled,effects,effectsr=self.reroll6s(values,rerolled,effects,effectsr)
        #extra atks 
        if (line2['hit6aop'].get()==1 or line2['hit6paop'].get()==1):
            values,effects,mw=self.ex6s1a(values,rerolled,line,line2,mod,hittarget,effects,effectsr,'hit',mw)
        #put together all values
        for x in rerolled:
            values.append(x)
        for y in effectsr:
            effects.append(y)
        #unmod effects
        #remove all 1s
        values,effects=self.fail1s(values,effects)
        #mw ending roll
        if line2['cbhitmw'].get()!='0':
            j=0
            while j<len(values):
                if values[j]>=hittarget:
                    x=self.dxconvert(line2['cbhitmw'].get())
                    mw[0]+=1
                    mw[1]+=x
                j+=1
            #end fn
            #do
            #print(values,effects)
            print('mod',mod,'rr',len(rerolled),'values',len(values),'effects',len(effects),'mw',mw)
            return [],[],mw
        #mw 6
        if (line2['cbhit6mw'].get()!='0' or line2['cbhit6pmw'].get()!='0'):
            values,mw=self.mw6s(values,line2,mod,mw,'hit')
        #rend and damage on 6
        if (line2['cbhit6rend'].get()!='0' or line2['cbhit6prend'].get()!='0' or line2['cbhit6dam'].get()!='0' or line2['cbhit6dam2'].get()!='0' or line2['cbhit6pdam'].get()!='0' or line2['cbhit6pdam2'].get()!='0'):
            effects=self.renddameffects(values,effects,mod,1)
        #hit or missed
        values,effects=self.rollpass(values,effects,hittarget,mod,'hit')
#        #multi hits
#        values,effects=self.multi6s(values,effects,hittarget,mod,line2,'hit')

        #print(values,effects)
        print('mod',mod,'rr',len(rerolled),'values',len(values),'effects',len(effects),'mw',mw)
        
        return values,effects,mw
    
    def towound(self,line,line2,values,effects,mw,results):
        #wound
        values=self.roll(values,len(values),results)
        woundtarget=int(line[4].get())
        mod=int(line2['cbwoundmod'].get())
        rerolled=[]
        effectsr=[]
        #re-rolls: yours then oppoenents
        #re-roll 1s
        if line2['woundrr1op'].get()==1:
            values,rerolled,effects,effectsr=self.reroll1s(values,rerolled,effects,effectsr)
        #re-roll failed (before mod)
        if line2['woundrrop'].get()==1:
            values,rerolled,effects,effectsr=self.rerollfail(values,rerolled,woundtarget,mod,effects,effectsr)
        #re-roll 6s
        if line2['woundrr6op'].get()==1:
            values,rerolled,effects,effectsr=self.reroll6s(values,rerolled,effects,effectsr)
        #extra atks 
        if (line2['wound6aop'].get()==1 or line2['wound6paop'].get()==1):
            values,effects,mw=self.ex6s1a(values,rerolled,line,line2,mod,woundtarget,effects,effectsr,'wound',mw)
        #put together all values
        for x in rerolled:
            values.append(x)
        for y in effectsr:
            effects.append(y)
        #unmod effects
        #remove all 1s
        values,effects=self.fail1s(values,effects)
        #mw ending roll
        if line2['cbwoundmw'].get()!='0':
            j=0
            while j<len(values):
                if values[j]>=woundtarget:
                    x=self.dxconvert(line2['cbwoundmw'].get())
                    mw[0]+=1
                    mw[1]+=x
                j+=1
            #end fn
            #do
            #print(values,effects)
            print('mod',mod,'rr',len(rerolled),'values',len(values),'effects',len(effects),'mw',mw)
            return [],[],mw
        #mw 6
        if (line2['cbwound6mw'].get()!='0' or line2['cbwound6pmw'].get()!='0'):
            values,mw=self.mw6s(values,line2,mod,mw,'wound')
        #rend and damage on 6
        if (line2['cbwound6rend'].get()!='0' or line2['cbwound6prend'].get()!='0' or line2['cbwound6dam'].get()!='0' or line2['cbwound6dam2'].get()!='0' or line2['cbwound6pdam'].get()!='0' or line2['cbwound6pdam2'].get()!='0'):
            effects=self.renddameffects(values,effects,mod,3)
        #wound or not
        values,effects=self.rollpass(values,effects,woundtarget,mod,'wound')
#        #multi wounds
#        values,effects=self.multi6s(values,effects,woundtarget,mod,line2,'wound')
        
        #print(values,effects)
        print('mod',mod,'rr',len(rerolled),'values',len(values),'effects',len(effects),'mw',mw)
        
        return values,effects,mw
            
    def tosave(self,values,effects,results,line,line2):
        values=self.roll(values,len(values),results)
        mod=0
        mod+=(int(line2['cvop'].get())+int(line2['cbsvmod'].get()))
        mod2=[int(line2['cbhit6rend'].get()),int(line2['cbhit6prend'].get()),int(line2['cbwound6rend'].get()),int(line2['cbwound6prend'].get()),int(line[6].get()),int(line2['cbrendmod'].get())]
        values,effects=self.rollpass(values,effects,mod,mod2,'save')
        
        #print(values,effects)
        print('mod',mod,'values',len(values),'effects',len(effects))
        
        return values,effects
    
    def todamage(self,values,effects,line,line2):
        base=line[7].get()
        #base mod for all values
        modtobase=line2['cbdammod'].get()
        modaddbase=self.dxconvert(line2['cbdammod2'].get())
        multiply=1
        if modtobase!='0':
            #x2x3
            if (modtobase=='x2' or modtobase=='x3'):
                if modtobase=='x2':
                    multiply=2
                else:
                    multiply=3
                base=base
            else:
                base=modtobase
        #dam by effect
        total=0
        i=len(values)-1
        print(len(values))
        while i>=0:
            damtot=0
            modadd=modaddbase
            if effects[i]!=0:
                #print(effects[i])
                if effects[i]==1:
                    try:
                        damtot=max([int(base),int(line2['cbhit6dam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6dam'].get()])
                    modadd+=self.dxconvert(line2['cbhit6dam2'].get())
                    if (line2['cbhit6dam'].get()=='x2' and multiply!=3):
                        multiply=2
                    elif line2['cbhit6dam'].get()=='x3':
                        multiply=3
                elif effects[i]==3:
                    try:
                        damtot=max([int(base),int(line2['cbwound6dam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbwound6dam'].get()])
                    modadd+=self.dxconvert(line2['cbwound6dam2'].get())
                    if (line2['cbwound6dam'].get()=='x2' and multiply!=3):
                        multiply=2
                    elif line2['cbwound6dam'].get()=='x3':
                        multiply=3
                elif effects[i]==5:
                    try:
                        damtot=max([int(base),int(line2['cbhit6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6pdam'].get()])
                    modadd+=self.dxconvert(line2['cbhit6pdam2'].get())
                    if (line2['cbhit6pdam'].get()=='x2' and multiply!=3):
                        multiply=2
                    elif line2['cbhit6pdam'].get()=='x3':
                        multiply=3
                elif effects[i]==11:
                    try:
                        damtot=max([int(base),int(line2['cbwound6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbwound6pdam'].get()])
                    modadd+=self.dxconvert(line2['cbwound6pdam2'].get())
                    if (line2['cbwound6pdam'].get()=='x2' and multiply!=3):
                        multiply=2
                    elif line2['cbwound6pdam'].get()=='x3':
                        multiply=3
                elif effects[i]==4:
                    try:
                        damtot=max([int(base),int(line2['cbhit6dam'].get()),int(line2['cbwound6dam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6dam'].get(),line2['cbwound6dam'].get()])
                    modadd+=(self.dxconvert(line2['cbhit6dam2'].get())+self.dxconvert(line2['cbwound6dam2'].get()))
                    if ((line2['cbhit6dam'].get()=='x2' or line2['cbwound6dam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbhit6dam'].get()=='x3' or line2['cbwound6dam'].get()=='x3'):
                        multiply=3
                elif effects[i]==9:
                    try:
                        damtot=max([int(base),int(line2['cbhit6dam'].get()),int(line2['cbwound6dam'].get()),int(line2['cbhit6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6dam'].get(),line2['cbwound6dam'].get(),line2['cbhit6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbhit6dam2'].get())+self.dxconvert(line2['cbwound6dam2'].get())+self.dxconvert(line2['cbhit6pdam2'].get()))
                    if ((line2['cbhit6dam'].get()=='x2' or line2['cbwound6dam'].get()=='x2' or line2['cbhit6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbhit6dam'].get()=='x3' or line2['cbwound6dam'].get()=='x3' or line2['cbhit6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==8:
                    try:
                        damtot=max([int(base),int(line2['cbwound6dam'].get()),int(line2['cbhit6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbwound6dam'].get(),line2['cbhit6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbwound6dam2'].get())+self.dxconvert(line2['cbhit6pdam2'].get()))
                    if ((line2['cbwound6dam'].get()=='x2' or line2['cbhit6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbwound6dam'].get()=='x3' or line2['cbhit6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==6:
                    try:
                        damtot=max([int(base),int(line2['cbhit6dam'].get()),int(line2['cbhit6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6dam'].get(),line2['cbhit6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbhit6dam2'].get())+self.dxconvert(line2['cbhit6pdam2'].get()))
                    if ((line2['cbhit6dam'].get()=='x2' or line2['cbhit6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbhit6dam'].get()=='x3' or line2['cbhit6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==16:
                    try:
                        damtot=max([int(base),int(line2['cbhit6pdam'].get()),int(line2['cbwound6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6pdam'].get(),line2['cbwound6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbhit6pdam2'].get())+self.dxconvert(line2['cbwound6pdam2'].get()))
                    if ((line2['cbhit6pdam'].get()=='x2' or line2['cbwound6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbhit6pdam'].get()=='x3' or line2['cbwound6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==14:
                    try:
                        damtot=max([int(base),int(line2['cbwound6dam'].get()),int(line2['cbwound6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbwound6dam'].get(),line2['cbwound6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbwound6dam2'].get())+self.dxconvert(line2['cbwound6pdam2'].get()))
                    if ((line2['cbwound6dam'].get()=='x2' or line2['cbwound6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbwound6dam'].get()=='x3' or line2['cbwound6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==12:
                    try:
                        damtot=max([int(base),int(line2['cbhit6dam'].get()),int(line2['cbwound6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6dam'].get(),line2['cbwound6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbhit6dam2'].get())+self.dxconvert(line2['cbwound6pdam2'].get()))
                    if ((line2['cbhit6dam'].get()=='x2' or line2['cbwound6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbhit6dam'].get()=='x3' or line2['cbwound6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==20:
                    try:
                        damtot=max([int(base),int(line2['cbhit6dam'].get()),int(line2['cbwound6dam'].get()),int(line2['cbhit6pdam'].get()),int(line2['cbwound6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6dam'].get(),line2['cbwound6dam'].get(),line2['cbhit6pdam'].get(),line2['cbwound6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbhit6dam2'].get())+self.dxconvert(line2['cbwound6dam2'].get())+self.dxconvert(line2['cbhit6pdam2'].get())+self.dxconvert(line2['cbwound6pdam2'].get()))
                    if ((line2['cbhit6dam'].get()=='x2' or line2['cbwound6dam'].get()=='x2' or line2['cbhit6pdam'].get()=='x2' or line2['cbwound6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbhit6dam'].get()=='x3' or line2['cbwound6dam'].get()=='x3' or line2['cbhit6pdam'].get()=='x3' or line2['cbwound6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==19:
                    try:
                        damtot=max([int(base),int(line2['cbwound6dam'].get()),int(line2['cbhit6pdam'].get()),int(line2['cbwound6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbwound6dam'].get(),line2['cbhit6pdam'].get(),line2['cbwound6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbwound6dam2'].get())+self.dxconvert(line2['cbhit6pdam2'].get())+self.dxconvert(line2['cbwound6pdam2'].get()))
                    if ((line2['cbwound6dam'].get()=='x2' or line2['cbhit6pdam'].get()=='x2' or line2['cbwound6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbwound6dam'].get()=='x3' or line2['cbhit6pdam'].get()=='x3' or line2['cbwound6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==15:
                    try:
                        damtot=max([int(base),int(line2['cbhit6dam'].get()),int(line2['cbwound6dam'].get()),int(line2['cbwound6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6dam'].get(),line2['cbwound6dam'].get(),line2['cbwound6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbhit6dam2'].get())+self.dxconvert(line2['cbwound6dam2'].get())+self.dxconvert(line2['cbwound6pdam2'].get()))
                    if ((line2['cbhit6dam'].get()=='x2' or line2['cbwound6dam'].get()=='x2' or line2['cbwound6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbhit6dam'].get()=='x3' or line2['cbwound6dam'].get()=='x3' or line2['cbwound6pdam'].get()=='x3'):
                        multiply=3
                elif effects[i]==17:
                    try:
                        damtot=max([int(base),int(line2['cbhit6dam'].get()),int(line2['cbhit6pdam'].get()),int(line2['cbwound6pdam'].get())])
                    except Exception:
                        damtot=self.compare([base,line2['cbhit6dam'].get(),line2['cbhit6pdam'].get(),line2['cbwound6pdam'].get()])
                    modadd+=(self.dxconvert(line2['cbhit6dam2'].get())+self.dxconvert(line2['cbhit6pdam2'].get())+self.dxconvert(line2['cbwound6pdam2'].get()))
                    if ((line2['cbhit6dam'].get()=='x2' or line2['cbhit6pdam'].get()=='x2' or line2['cbwound6pdam'].get()=='x2') and multiply!=3):
                        multiply=2
                    elif (line2['cbhit6dam'].get()=='x3' or line2['cbhit6pdam'].get()=='x3' or line2['cbwound6pdam'].get()=='x3'):
                        multiply=3
                else:
                    print('er sv effects')
            else:
                damtot=base
            damtot=self.dxconvert(damtot)
            #x2 and x3
            damtot*=multiply
            #mod
            damtot+=modadd
            total+=damtot
            i-=1
            
        print('damage',total)
        return total
    
    def compare(self,values):
        i=0
        values2=[]
        convert={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'D3':2,'D6':3.5,'2D3':4,'2D6':7,'x2':0,'x3':0,'0':0}
        #rank=['x2','x3',1,2,'D3',3,'D6',4,'2D3',5,6,'2D6']
        while i<len(values):
            #print('v',values[i])
            values2.append(convert[values[i]])
            i+=1
        a=max(values2)
        b=values2.count(a)
        #multi values
        if (b!=1 and a==0):
            print('er damage=0')
            maxv=0
        elif (b!=1 and a==2):
            c=int(random()*2)
            if c==0:
                maxv=2
            elif c==1:
                maxv=self.dxconvert('D3')
            else:
                print('error compare')
        elif (b!=1 and a==4):
            c=int(random()*2)
            if c==0:
                maxv=4
            elif c==1:
                maxv=self.dxconvert('2D3')
            else:
                print('error compare')
        elif (b!=1 and a==7):
            c=int(random()*2)
            if c==0:
                maxv=7
            elif c==1:
                maxv=self.dxconvert('2D6')
            else:
                print('error compare')
        #non numerical
        else:
            if a==2:
                if 'D3' in values:
                    maxv=self.dxconvert('D3')
                else:
                    maxv=2
            elif a==4:
                if '2D3' in values:
                    maxv=self.dxconvert('2D3')
                else:
                    maxv=4
            elif a==7:
                if '2D6' in values:
                    maxv=self.dxconvert('2D6')
                else:
                    maxv=7
            elif a==3.5:
                if 'D6' in values:
                    maxv=self.dxconvert('D6')
                else:
                    print('er 3.5 no D6')
            else:
                #print('a,',a,type(a))
                maxv=self.dxconvert(a)
            #print(maxv)
            
        return maxv
            
    def reroll6s(self,values,rerolled,effects,effectsr):
        i=len(values)-1
        while i>-1:
            if values[i]==6:
                a=int(random()*6+1)
                rerolled.append(a)
                effectsr.append(effects[i])
                values.pop(i)
                effects.pop(i)
            i-=1
        return values,rerolled,effects,effectsr
    
    def reroll1s(self,values,rerolled,effects,effectsr):
        i=len(values)-1
        while i>-1:
            if values[i]==1:
                a=int(random()*6+1)
                rerolled.append(a)
                effectsr.append(effects[i])
                values.pop(i)
                effects.pop(i)
            i-=1
        return values,rerolled,effects,effectsr
    
    def rerollfail(self,values,rerolled,target,mod,effects,effectsr):
        i=len(values)-1
        if mod<0:
            mod=0
        while i>-1:
            if values[i]==6:
                pass
            elif (((values[i]+mod)<target) or (values[i]==1)):
                a=int(random()*6+1)
                rerolled.append(a)
                effectsr.append(effects[i])
                values.pop(i)
                effects.pop(i)
            i-=1
        return values,rerolled,effects,effectsr
    
    def ex6s1a(self,values,rerolled,line,line2,mod,hittarget,effects,effectsr,rtype,mw):
        if rtype=='hit':
            six=line2['hit6aop'].get()
            sixp=line2['hit6paop'].get()
            rr=[line2['hitrr1op'].get(),line2['hitrrop'].get(),line2['hitrr6op'].get()]
        elif rtype=='wound':
            six=line2['wound6aop'].get()
            sixp=line2['wound6paop'].get()
            rr=[line2['woundrr1op'].get(),line2['woundrrop'].get(),line2['woundrr6op'].get()]
        else:
            print('er extra atk')
        count=0
        for x in values:
            if (x==6 and six==1):
                count+=1
            if ((x+mod)>=6 and sixp==1):
                count+=1
        for y in rerolled:
            if (y==6 and six==1):
                count+=1
            if ((y+mod)>=6 and sixp==1):
                count+=1
        valuestemp=[0]*count
        rerolledtemp=[]
        effectstemp=[0]*count
        effectsrtemp=[]
        #wound extra hits- need hit roll
        if rtype=='wound':
            valuestemp,effectstemp,mw=self.tohit(line,line2,valuestemp,effectstemp,mw,[0,0,0,0,0,0],count)
        
        valuestemp=self.roll(valuestemp,len(valuestemp),[0,0,0,0,0,0])
#        i=0
#        while i<count:
#            a=int(random()*6+1)
#            valuestemp.append(a)
#            effectstemp.append(0)
#            i+=1
        #re-rolls: yours then oppoenents
        #re-roll 1s
        if rr[0]==1:
            valuestemp,rerolledtemp,effectstemp,effectsrtemp=self.reroll1s(valuestemp,rerolledtemp,effectstemp,effectsrtemp)
        #re-roll failed (before mod)
        if rr[1]==1:
            valuestemp,rerolledtemp,effectstemp,effectsrtemp=self.rerollfail(valuestemp,rerolledtemp,hittarget,mod,effectstemp,effectsrtemp)
        #re-roll 6s
        if rr[2]==1:
            valuestemp,rerolledtemp,effectstemp,effectsrtemp=self.reroll6s(valuestemp,rerolledtemp,effectstemp,effectsrtemp)
        
        for xx in valuestemp:
            values.append(xx)
            effects.append(0)
        for yy in rerolledtemp:
            values.append(yy)
            effects.append(0)
        return values,effects,mw
    
    def fail1s(self,values,effects):
        i=len(values)-1
        while i>=0:
            if values[i]==1:
                values.pop(i)
                effects.pop(i)
            i-=1
        return values,effects
    
    def mw6s(self,values,line2,mod,mw,rtype):
        if rtype=='hit':
            six=line2['cbhit6mw'].get()
            sixp=line2['cbhit6pmw'].get()
        elif rtype=='wound':
            six=line2['cbwound6mw'].get()
            sixp=line2['cbwound6pmw'].get()
        else:
            print('er mw 6s')
        tot=0
        totp=0
        if (six!='0' or sixp!='0'):
            i=len(values)-1
            while i>=0:
                if (values[i]==6 and six!='0'):
                    tot+=1
                if ((values[i]+mod)>=6 and sixp!='0'):
                    totp+=1
                if ((values[i]==6 and six!='0' and six.find('atk')!=-1) or ((values[i]+mod)>=6 and sixp!='0' and sixp.find('atk')!=-1)):
                    values.pop(i)
                i-=1
        j=0
        while j<tot:
            x=self.dxconvert(six)
            mw[0]+=1
            mw[1]+=x
            j+=1
        k=0
        while k<totp:
            x=self.dxconvert(sixp)
            mw[0]+=1
            mw[1]+=x
            k+=1
        return values,mw
        
    def dxconvert(self,x):
        if type(x)==type('str'):
            if x.find('atk')!=-1:
                x=x.replace(' atk end','')
        try:
            int(x)
        except Exception:
            if (x=='D3' or x=='D3 atk end'):
                x=int(random()*3+1)
            elif x=='-D3':
                x=-int(random()*3+1)
            elif (x=='D6' or x=='D6 atk end'):
                x=int(random()*6+1)
            elif x=='-D6':
                x=-int(random()*6+1)
            elif (x=='2D3' or x=='2D3 atk end'):
                x=int(random()*3+1)+int(random()*3+1)
            elif x=='-2D3':
                x=-(int(random()*3+1)+int(random()*3+1))
            elif (x=='2D6' or x=='2D6 atk end'):
                x=int(random()*6+1)+int(random()*6+1)
            elif x=='-2D6':
                x=-(int(random()*6+1)+int(random()*6+1))
            else:
                print('type not found')
        return int(x)
    
    def renddameffects(self,values,effects,mod,to):
        i=0
        while i<len(values):
            if values[i]==6:
                effects[i]+=to
#                if (effects[i]!=0 and effects[i]!=to):
#                    effects[i]==3
#                else:
#                    effects[i]=to
            if (values[i]+mod)>=6:
                effects[i]+=(to*3+2)
#                if (effects[i]!=0 and effects[i]!=to):
#                    effects[i]==3
#                else:
#                    effects[i]=to
            i+=1
        return effects
    
    def rollpass(self,values,effects,target,mod,rtype):
        valuespass=[]
        effectspass=[]
        if (rtype=='hit' or rtype=='wound'):
            print(len(values),len(effects))
            i=len(values)-1
            while i>=0:
                #6 auto pass
                if values[i]==6:
                    valuespass.append(values[i])
                    effectspass.append(effects[i])
                    values.pop(i)
                    effects.pop(i)
                elif (values[i]+mod)>=target:
                    valuespass.append(values[i])
                    effectspass.append(effects[i])
                    values.pop(i)
                    effects.pop(i)
                i-=1
        elif rtype=='save':
            mod2=mod
            mod=target
            print(mod,mod2)
            savetarget=[2,3,4,5,6,7]
            i=len(values)-1
            print(len(values))
            while i>=0:
                a=int(random()*6)
                #a=2
                target=savetarget[a]
                #print(target)
                if effects[i]!=0:
                    #print(effects[i])
                    if effects[i]==1:
                        modtot=mod+min([mod2[0],mod2[4],mod2[5]])
                    elif effects[i]==3:
                        modtot=mod+min([mod2[2],mod2[4],mod2[5]])
                    elif effects[i]==5:
                        modtot=mod+min([mod2[1],mod2[4],mod2[5]])
                    elif effects[i]==11:
                        modtot=mod+min([mod2[3],mod2[4],mod2[5]])
                    elif effects[i]==4:
                        modtot=mod+min([mod2[0],mod2[2],mod2[4],mod2[5]])
                    elif effects[i]==9:
                        modtot=mod+min([mod2[0],mod2[1],mod2[2],mod2[4],mod2[5]])
                    elif effects[i]==8:
                        modtot=mod+min([mod2[1],mod2[2],mod2[4],mod2[5]])
                    elif effects[i]==6:
                        modtot=mod+min([mod2[0],mod2[1],mod2[4],mod2[5]])
                    elif effects[i]==16:
                        modtot=mod+min([mod2[1],mod2[3],mod2[4],mod2[5]])
                    elif effects[i]==14:
                        modtot=mod+min([mod2[2],mod2[3],mod2[4],mod2[5]])
                    elif effects[i]==12:
                        modtot=mod+min([mod2[0],mod2[3],mod2[4],mod2[5]])
                    elif effects[i]==20:
                        modtot=mod+min([mod2[0],mod2[1],mod2[2],mod2[3],mod2[4],mod2[5]])
                    elif effects[i]==19:
                        modtot=mod+min([mod2[1],mod2[2],mod2[3],mod2[4],mod2[5]])
                    elif effects[i]==15:
                        modtot=mod+min([mod2[0],mod2[2],mod2[3],mod2[4],mod2[5]])
                    elif effects[i]==17:
                        modtot=mod+min([mod2[0],mod2[1],mod2[3],mod2[4],mod2[5]])
                    else:
                        print('er sv effects')
                else:
                    modtot=min(mod2[4],mod2[5])+mod
                #print(modtot)
                if values[i]!=1:
                    if (values[i]+modtot)>=target:
                        values.pop(i)
                        effects.pop(i)
                i-=1
            print(len(values))
            valuespass=values
            effectspass=effects
        else:
            print('er rollpass')
        return valuespass,effectspass
        
    def multi6s(self,values,effects,line2,rtype):
        addvalues=[]
        addeffects=[]
        if rtype=='hit':
#            a=int(line2['hit62op'].get())
#            b=int(line2['hit63op'].get())
#            c=int(line2['hit6p2op'].get())
#            d=int(line2['hit6p3op'].get())
#            e=int(line2['hitd3op'].get())
#            f=int(line2['hitd6op'].get())
            a=line2['cbhit6op'].get()
            b=line2['cbhit6pop'].get()
            c=line2['cbhitxop'].get()
            mod=int(line2['cbhitmod'].get())
        elif rtype=='wound':
#            a=int(line2['wound62op'].get())
#            b=int(line2['wound63op'].get())
#            c=int(line2['wound6p2op'].get())
#            d=int(line2['wound6p3op'].get())
#            e=int(line2['woundd3op'].get())
#            f=int(line2['woundd6op'].get())
            a=line2['cbwound6op'].get()
            b=line2['cbwound6pop'].get()
            c=line2['cbwoundxop'].get()
            mod=int(line2['cbwoundmod'].get())
        else:
            print('er multi 6s')
        
        i=0
        while i<len(values):
            if (a!='0' and values[i]==6):
                j=self.dxconvert(a)
                while j>=0:
                    addvalues.append(values[i])
                    addeffects.append(effects[i])
                    j=-1
            if (b!='0' and (values[i]+mod)>=6):
                j=self.dxconvert(a)
                while j>=0:
                    addvalues.append(values[i])
                    addeffects.append(effects[i])
                    j=-1
            if (c!='0'): #and (values[i]+mod)>=target, hit/wound should all be passes
                j=self.dxconvert(a)
                while j>=0:
                    addvalues.append(values[i])
                    addeffects.append(effects[i])
                    j=-1
                    
#            if (a==1 and values[i]==6):
#                addvalues.append(values[i])
#                addeffects.append(effects[i])
#            if (b==1 and values[i]==6):
#                addvalues.append(values[i])
#                addeffects.append(effects[i])
#                addvalues.append(values[i])
#                addeffects.append(effects[i])
#            if (c==1 and (values[i]+mod)>=6):
#                addvalues.append(values[i])
#                addeffects.append(effects[i])
#            if (d==1 and (values[i]+mod)>=6):
#                addvalues.append(values[i])
#                addeffects.append(effects[i])
#                addvalues.append(values[i])
#                addeffects.append(effects[i])
#            if (e==1 and (values[i]+mod)>=target):
#                j=int(random()*3+1)
#                while j>=0:
#                    addvalues.append(values[i])
#                    addeffects.append(effects[i])
#                    j=-1
#            if (f==1 and (values[i]+mod)>=target):
#                j=int(random()*6+1)
#                while j>=0:
#                    addvalues.append(values[i])
#                    addeffects.append(effects[i])
#                    j=-1
            i+=1
        #print(addvalues)
        for x in addvalues:
            values.append(x)
        for y in addeffects:
            effects.append(y)
        return values,effects
    
    def commands(self):
        self.btnAdd.configure(command=lambda:self.addLine())
        self.btnDel.configure(command=lambda:self.removeLine(),state=DISABLED)
        self.btnCal.configure(command=lambda:self.calculate())
    
#program
win=Tk()
ops=Mode()
gui=Gui1(win,ops)
win.mainloop()

win2=Tk()
if ops.mode==1:
    gui2=Gui2(win2)
elif ops.mode==2:
    gui2=Gui2(win2)
    gui3=Gui2(win2)
    gui3.title.destroy()
    gui2.title.configure(text='Compare unit ability')
else:
    print('error options')
    win2.destroy()
        
win2.mainloop()
