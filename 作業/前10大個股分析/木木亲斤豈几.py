import tkinter
import tkinter.ttk as ttk
# from tkinter import ttk
import tkinter.messagebox
import requests
import datetime

url = "https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=%d&selectType=ALL"

def findBtnClicked():
    try:
        entry1Value = int(entry1.get())
        entry2Value = float(entry2.get())
        entry3Value = float(entry3.get())
        entry4Value = float(entry4.get())
    except BaseException as e:
        tkinter.messagebox.showinfo("欄位資料內容錯誤", e)
        return
    try:
        req = requests.get(url.format(entry1Value))
    except BaseException as e:
        tkinter.messagebox.showinfo("資料載入失敗", e)
        return

    if req.status_code == 200:
        lines = req.text.split('\n')
        skipline = 0
        for oneline in lines:
            if skipline < 2:
                skipline += 1
                continue
            elif oneline.strip() == '""':
                break
            # print(oneline)
            fields = tuple(v.replace("\"", "") for v in oneline.split(","))
            try:
                if float(fields[2]) >= entry2Value and float(fields[4]) <= entry3Value and float(fields[5]) <= entry4Value:
                    tree.insert("", "end", values=fields)
            except BaseException as e:
                print("%s 資料異常 %s" % (oneline.strip(), e))
    else:
        tkinter.messagebox.showinfo("資料載入失敗", "Status Code = %d".format(req.status_code))


def closeBtnClicked():
    win.quit()


win = tkinter.Tk()
win.title("前10大個股日本益比、殖利率及股價淨值比")
win.geometry("800x600")

panel1 = tkinter.Frame(win)
panel1.pack(fill=tkinter.BOTH)
panel1.pack_propagate(False)

panel1.rowconfigure((0, 1, 2, 3, 4), weight=1)
panel1.columnconfigure((0, 1), weight=1)

label1 = tkinter.Label(panel1, text="日期")
label1.grid(row=0, column=0, pady=(5, 0))

entry1 = tkinter.Entry(panel1, justify=tkinter.CENTER)
entry1.grid(row=0, column=1, pady=(5, 0))
entry1.insert(0, str(datetime.datetime.today().date()).replace("-", ""))

label2 = tkinter.Label(panel1, text="殖利率 >=")
label2.grid(row=1, column=0, pady=(5, 0))

entry2 = tkinter.Entry(panel1, justify=tkinter.CENTER)
entry2.grid(row=1, column=1, pady=(5, 0))
entry2.insert(0, "5.0")

label3 = tkinter.Label(panel1, text="本益比 <=")
label3.grid(row=2, column=0, pady=(5, 0))

entry3 = tkinter.Entry(panel1, justify=tkinter.CENTER)
entry3.grid(row=2, column=1, pady=(5, 0))
entry3.insert(0, "5.0")

label4 = tkinter.Label(panel1, text="股價淨值比 <=")
label4.grid(row=3, column=0, pady=(5, 0))

entry4 = tkinter.Entry(panel1, justify=tkinter.CENTER)
entry4.grid(row=3, column=1, pady=(5, 0))
entry4.insert(0, "5.0")

findBtn = tkinter.Button(panel1, text="查找", command=findBtnClicked)
findBtn.grid(row=4, column=0, pady=(5, 5))

closeBtn = tkinter.Button(panel1, text="關閉", command=closeBtnClicked)
closeBtn.grid(row=4, column=1, pady=(5, 5))

panel2 = tkinter.Frame(win, relief="sunken", borderwidth=3)
panel2.pack(fill=tkinter.BOTH, expand=True)
panel2.pack_propagate(False)

tree = ttk.Treeview(panel2, columns=["1", "2", "3", "4", "5", "6", "7"], show="headings")
tree.column("1", width=100, anchor="center")
tree.column("2", width=100, anchor="center")
tree.column("3", width=100, anchor="center")
tree.column("4", width=100, anchor="center")
tree.column("5", width=100, anchor="center")
tree.column("6", width=100, anchor="center")
tree.column("7", width=100, anchor="center")
tree.heading("1", text="證券代號")
tree.heading("2", text="證券名稱")
tree.heading("3", text="殖利率(%)")
tree.heading("4", text="股利年度")
tree.heading("5", text="本益比")
tree.heading("6", text="股價淨值比")
tree.heading("7", text="財報年/季")

tree.pack(fill=tkinter.BOTH, expand=True)
tree.pack_propagate(False)

win.mainloop()