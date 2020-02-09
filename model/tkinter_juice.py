from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def floatTest(num):
    floatTest2 = False
    try:
        float(num)
        floatTest2 = True
    except ValueError:
        floatTest2 = False
    if floatTest2 == True:
        return True
    else:
        return False


def pointCalculator():
    pts = pts_entry.get("1.0", END)
    oreb = oreb_entry.get("1.0", END)
    dreb = dreb_entry.get("1.0", END)
    ast = ast_entry.get("1.0", END)
    stl = stl_entry.get("1.0", END)
    blk = blk_entry.get("1.0", END)
    fgmi = fgmi_entry.get("1.0", END)
    to = to_entry.get("1.0", END)

    # Needs to floatcheck all variables
    if floatTest(pts) == True and floatTest(oreb) == True and floatTest(dreb) == True and floatTest(
            ast) == True and floatTest(stl) == True and floatTest(blk) == True and floatTest(
            fgmi) == True and floatTest(to) == True:
        pts, oreb, dreb, ast = float(pts), float(oreb), float(dreb), float(ast)
        stl, blk, fgmi, to = float(stl), float(blk), float(fgmi), float(to)
        #fantasytotal(pts, oreb, dreb, ast, stl, blk, fgmi, to)
    else:
        messagebox.showinfo("ERROR", "Please input numbers!")


def newPage():
    newPage = Toplevel()
    newPage.title("New Page")

    sex = Label(newPage, text="Sex")
    age = Label(newPage, text="Age")
    medu = Label(newPage, text="Mother Education")
    fedu = Label(newPage, text="Father Education")
    travelTime = Label(newPage, text="Home to School Travel Time")
    studytime = Label(newPage, text="Study Time")
    failures = Label(newPage, text="Failures")
    famsup = Label(newPage, text="Family Support")

    sex.grid(row=0, column=0)
    age.grid(row=1, column=0)
    medu.grid(row=2, column=0)
    fedu.grid(row=3, column=0)
    travelTime.grid(row=4, column=0)
    studytime.grid(row=5, column=0)
    failures.grid(row=6, column=0)
    famsup.grid(row=7, column=0)

    sex_combo = ttk.Combobox(newPage, values=['Male','Female'] )
    age_entry = Text(newPage, width=10, height=1)
    medu_entry = ttk.Combobox(newPage, values=['None','Primary Education',
                                               '5th-9th grade','Secondary Education',
                                               'Higher Education'] )

    fedu_entry = ttk.Combobox(newPage, values=['None', 'Primary Education',
                                               '5th-9th grade', 'Secondary Education',
                                               'Higher Education'])
    travelTime = ttk.Combobox(newPage, values=['None', 'Primary Education',
                                               '5th-9th grade', 'Secondary Education',
                                               'Higher Education'])
    studytime_entry = Text(newPage, width=10, height=1)
    failures_entry = Text(newPage, width=10, height=1)
    famsup_entry = Text(newPage, width=10, height=1)

    sex_combo.grid(row=0, column=1)
    age_entry.grid(row=1, column=1)
    medu_entry.grid(row=2, column=1)
    fedu_entry.grid(row=3, column=1)
    travelTime_entry.grid(row=4, column=1)
    studytime_entry.grid(row=5, column=1)
    failures_entry.grid(row=6, column=1)
    famsup_entry.grid(row=7, column=1)


    calculateButton = Button(newPage, text="Find the best players!", command=pointCalculator)
    calculateButton.grid(row=8, columnspan=2)


# Title Page
def main():
    global root
    root = Tk()
    root.title("Title Page")

    label = Label(root, text="Lets predict how much alchol you drink in a day")
    label.grid(row=0, column=0)
    button = Button(root, text="Get Started!", command=newPage)
    button.grid(row=1, column=0)

    root.mainloop()


main()