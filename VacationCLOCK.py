# python lib
import os,sys
import tkinter as tk
import datetime



class vacation:
    def __init__(self,master):
        master.title("Vacation Countdown!")
        self.label_text = tk.StringVar()
        self.message = "PUT IN VACATION DATE (Janurary 12, 2018 as 1,12,2018)"
        self.label_text.set(self.message)
        self.label = tk.Label(master, textvariable=self.label_text)
        self.var1 = tk.StringVar()
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.entry = tk.Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.cal_button = tk.Button(master, text="Calculate", command=self.test)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E)
        self.label.grid(row=0, column=0, columnspan=1, sticky=tk.W + tk.E)
        self.cal_button.grid(row=2, column=0)
        self.windows = []

    def test(self):
        new = tk.Toplevel()
        new.title("Count Down %d" % len(self.windows))
        x = new.winfo_x()
        y = new.winfo_y()
        new.geometry("+100+50")
        cal2 = self.cal
        cal2 = cal2.split(',')
        a = int(cal2[0])
        b = int(cal2[1])
        c = int(cal2[2])
        #print a,b,c
        d0 = datetime.date(c,a,b)
        d1 = datetime.date.today()
        delta2 = (d0 - d1).days
        target_time =datetime.datetime.now() + datetime.timedelta(days=delta2)
        target_time = target_time.replace(hour=0, minute=0, second=0, microsecond=0)
        #print target_time
        delta = target_time - datetime.datetime.now()
        #print delta
        #print target_time
        #print datetime.datetime.now()
        #print delta
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        seconds = delta.seconds % 60
        message = ('{} days, {} hours, {} minutes, {} seconds'.format(delta.days, hours, minutes, seconds))
        #self.message_1 = message
        #print self.message_1
        tmp_label = tk.StringVar()
        tmp_label.set(message)
        label = tk.Label(new, textvariable=tmp_label)
        label.pack()
        label.configure(text=message)
        label.grid(row=0, column=0, columnspan=2, sticky=tk.W + tk.E)
        #self.windows.append(new)
        #root.after(1000,new.destroy)
        root.after(1000,self.test)

    def validate(self, text):
        if text == "":
            # allow null entries so the user can delete everything
            # before entering a value if they wish.
            return True
        try:
            cal = text
            #this is way to pass value within class
            self.cal = cal
            #print cal
            return True
        except ValueError:
            return False


root = tk.Tk()
my_gui = vacation(root)
root.mainloop()

