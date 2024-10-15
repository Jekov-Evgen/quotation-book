from tkinter import ttk
from tkinter import *
import random

def erorr():
    info = Tk()
            
    Label(info, text="Произошла ошибка попробуйте еще раз").grid(row=0, column=0, padx=10, pady=10)
    Button(info, text="OK", command=info.destroy).grid(row=1, column=0, padx=10, pady=10)

class MainWindow:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Цитатник")
        frm = ttk.Frame(self.root, padding=10)
        frm.grid
        
        ttk.Label(text="Добро пожаловать в цитатник", font="30").grid(row=0, column=0, padx=10, pady=10)
        
        self.quote = ttk.Entry(width=50)
        self.quote.grid(row=1, column=0, padx=10, pady=10)
        
        ttk.Button(text="Добавить цитату", width=50, command=self.add_quote).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(text="Просмотреть все цитаты", width=50, command=self.look_quote).grid(row=3, column=0, padx=10, pady=10)
        ttk.Button(text="Получить рандомную цитату", width=50, command=self.random_quote).grid(row=4, column=0, padx=10, pady=10)
            
    def run(self):
        self.root.mainloop()
        
    def add_quote(self):
        try:
            getting_a_quote = self.quote.get()
        except:
            erorr()
            
        with open("quote.txt", "a", encoding="UTF-8") as f:
            f.write(getting_a_quote)
            f.write("\n")
            
    def look_quote(self):
        result = []
        
        try:
            with open("quote.txt", 'r', encoding="UTF-8") as f:
                temp = f.read().splitlines()
            
            result.append(temp)
        except:
            erorr()
            
        quote_window = Tk()
        
        for i in range(len(result[0])):
            temp = result[0][i]
            Label(quote_window, text=f"{temp}", font=30).grid(row=i, column=0, padx=10, pady=10)
            
        Button(quote_window, text="ВЫХОД", command=quote_window.destroy).grid(row=len(result[0]) + 1, column=0 ,padx=10, pady=10)
        
    def random_quote(self):
        result = []
        
        try:
            with open("quote.txt", 'r', encoding="UTF-8") as f:
                temp = f.read().splitlines()
            
            result.append(temp)
        except:
            erorr()
            
        rand = random.randint(0, len(result[0]) - 1)
        random_quote_window = Tk()
        
        Label(random_quote_window, text="Твоя рандомная цитата", font="30").grid(row=0, column=0, padx=10, pady=10)
        Label(random_quote_window, text=f"{result[0][rand]}", font="30").grid(row=1, column=0, padx=10, pady=10)
        Label(random_quote_window, text="Пусть она мотивирует тебя", font="30").grid(row=2, column=0 ,padx=10 ,pady=10)
        
        Button(random_quote_window, text="ВЫЙТИ", width=50, command=random_quote_window.destroy).grid(row=3, column=0 ,padx=10, pady=10)       