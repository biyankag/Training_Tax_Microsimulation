# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:56:40 2022

@author: wb305167
"""
import json
from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter.messagebox import showinfo
from tkinter import filedialog

from threading import Thread

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import sys
#from taxcalc import *

from PIL import Image,ImageTk

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
        self.terminal = sys.stderr

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

    def clear(self):
        self.widget.configure(state="normal")
        self.widget.delete('1.0', tk.END)
        self.widget.configure(state="disabled")

    def flush(self):
        self.terminal.flush()
       
def display_error(self, widget, varname):
    self.vars[varname] = int(widget.get())
    self.text = scrolledtext.ScrolledText(self.TAB7, 
                                  wrap = tk.WORD, 
                                  width = 40, 
                                  height = 10, 
                                  font = ("Times New Roman",
                                          15))
    self.text.place(relx = 0.72, rely=0.70)
    #self.text.insert('end', "stderr")
    #sys.stdout = TextRedirector(self.text, "stdout")
    self.logger = TextRedirector(self.text, "stderr")
    sys.stderr = self.logger
    #sys.stderr = TextRedirector(self.text, "stderr")

def tab7(self):    
   
    self.block_1_title_pos_x = 0.15
    self.block_1_title_box_y = 0.15

    self.block_2_title_pos_x = 0.45
    
    self.block_3_title_pos_x = 0.75

    self.TAB7_root_title=tk.Label(self.TAB7,text="Tax Microsimulation Model",
             font = self.fontStyle_title)
    self.TAB7_root_title.place(relx = self.title_pos_x, rely = self.title_pos_y, anchor = "n")
    
    self.TAB7_root_title=Label(self.TAB7,text="Settings",
             font = self.fontStyle_sub_title)
    self.TAB7_root_title.place(relx = self.title_pos_x, rely = self.sub_title_pos_y, anchor = "n")
    
    self.vars['show_error_log'] = 0
    self.error_chk = tk.IntVar()
    self.error_chk_box = tk.Checkbutton(self.TAB7, text='Show Error Log', 
                                      font = self.fontStyle, variable=self.error_chk,
                                      command=lambda: self.display_error(self.error_chk, 'show_error_log'))
    self.error_chk_box.place(relx = self.block_1_title_pos_x, rely = self.block_1_title_pos_y, anchor = "w")
