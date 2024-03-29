import tkinter as tk

class Calculator():
    def __init__(self, master):
        self.m = master
        #tk.Tk.__init__(self)
        self.keyboard = [['7','8','9',  '+'],
                         ['6','5','4',  '-'],
                         ['3','2','1',  '*'],
                         ['0','00','C', '/']]

    def menu(self):
        self.e = tk.Entry(self.m)
        self.e.grid(row=0, column=0, columnspan=4, sticky='W')
        #result = eval(f'{self.e.get()}')
        #tk.Label(self, text=f"= {result}").grid(row=0, column=0, columnspan=4, sticky='E')
        for i in range(4):
            for j in range(4):
                b = tk.Button(self.m, text=f"{self.keyboard[i][j]}", width=3, height=2)
                b["command"] = lambda x = self.keyboard[i][j]: self.press_button(x)
                #print(b.__dir__())
                b.grid(row=i+1, column=j)

    def press_button(self, letter):
        t = self.e.get() + letter
        if letter=='C':
            self.e.delete(0, len(t))

        else:
            self.e.delete(0, len(t))
            [self.e.insert(0, let) for let in t[::-1]]
            expression = self.e.get()
            print(repr(expression))
            print(type(expression[-1]) == int)
            #print(type(1)==int)
            if expression[-1] not in ['+', '-', '*', '/', '']:
                result = eval(f'{expression}')
                tk.Label(self.m, text=f"= {result}").grid(row=0, column=0, columnspan=4, sticky='E')

    def del_e(self):
        t = self.e.get()
        t.pop()
        self.e.delete(0, len(t))
        [self.e.insert(0, let) for let in t[::-1]]
    
    def get_result(self):
        result = eval(f"{self.e.get()}")
        tk.Label(self.m, text=f"= {result}").grid(row=0, column=0, columnspan=4, sticky='E')

if __name__ == '__main__':
    r= tk.Tk()
    c = Calculator(r)
    c.menu()
    r.mainloop()
