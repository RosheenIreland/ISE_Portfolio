# Creating a currency converter

#First installed 'tkinter' for UI
#Installed 'request' to get url

# Importing Libraries

import requests
from tkinter import *
import tkinter as tk 
from tkinter import ttk 

# Creating currency converter class (code template for creating objects)
class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data= requests.get(url).json()
        self.currencies = self.data("rates")

def convert(self, from_currency, to_currency, amount):
    initial_amount = amount
    # Converts to EURO if it is not in Euro

    if from_currency != 'EURO' :
        amount = amount / self.currencies[from_currency]

    # Limiting to 4 decimal points
    amount = round(amount * self.currencies[to_currency])
    return amount
