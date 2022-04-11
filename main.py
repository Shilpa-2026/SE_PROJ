import mysql.connector
from tkinter import *
from tkinter import messagebox as msg
import datetime
import matplotlib.pyplot as plt




def create_account():
    global create_account_screen
    global contact_number
    global name
    global address
    global owner_name
    global newpass
    global confirmpass
    global username

    contact_number = StringVar()
    name = StringVar()
    address = StringVar()
    owner_name = StringVar()
    newpass=StringVar()
    confirmpass = StringVar()
    username=StringVar()

    create_account_screen = Toplevel(main_screen)
    create_account_screen.title("Create New Account")
    create_account_screen.geometry("1000x1000")

    Label(create_account_screen, text="Please enter details below", bg="red").pack()
    Label(create_account_screen, text="").pack()

    name_label = Label(create_account_screen, text="Name of the Organization ")
    name_label.pack()
    name_entry = Entry(create_account_screen, textvariable=name)
    name_entry.pack()

    Label(create_account_screen, text="").pack()

    owner_name_label = Label(create_account_screen, text="Name of the Owner ")
    owner_name_label.pack()
    owner_name_entry = Entry(create_account_screen, textvariable=owner_name)
    owner_name_entry.pack()

    Label(create_account_screen, text="").pack()

    contactnumber_label = Label(create_account_screen, text="Contact number * ")
    contactnumber_label.pack()
    contact_number_entry = Entry(create_account_screen, textvariable=contact_number)
    contact_number_entry.pack()

    Label(create_account_screen, text="").pack()

    address_label = Label(create_account_screen, text="Address ")
    address_label.pack()
    address_entry = Entry(create_account_screen, textvariable=address)
    address_entry.pack()

    Label(create_account_screen, text="").pack()

    user_label = Label(create_account_screen, text="Username * ")
    user_label.pack()
    user_entry = Entry(create_account_screen, textvariable=username)
    user_entry.pack()

    Label(create_account_screen, text="").pack()
    newpass_label = Label(create_account_screen, text="Enter New Password * ")
    newpass_label.pack()
    newpass_entry = Entry(create_account_screen, textvariable=newpass)
    newpass_entry.pack()

    Label(create_account_screen, text="").pack()
    confirmpass_label = Label(create_account_screen, text="Confirm Password * ")
    confirmpass_label.pack()
    confirmpass_entry = Entry(create_account_screen, textvariable=confirmpass)
    confirmpass_entry.pack()

    Label(create_account_screen, text="").pack()

    Button(create_account_screen, text="Create", width=10, height=1, bg="red", command=create_account_sql).pack()
    Button(create_account_screen, text="Go Back", width=10, height=1, bg="red", command=destroy_create_account).pack()

def destroy_create_account():
    create_account_screen.destroy()

def create_account_sql():
    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    contact = str(contact_number.get())

    if len(contact) == 0:
        msg.showinfo('Information', 'Contact number field should not be empty')
        return

    if (len(contact) != 10):
        msg.showinfo('Information', 'Contact number should be of 10 digits only')
        return

    na = str(name.get())

    if (len(na) == 0):
        msg.showinfo('Information', 'NAME OF THE ORGANIZATION field should not be empty')
        return

    na1 = str(owner_name.get())

    if (len(na1) == 0):
        msg.showinfo('Information', 'NAME OF THE OWNER field should not be empty')
        return

    addr = str(address.get())

    if (len(addr) == 0):
        msg.showinfo('Information', 'Address field should not be empty')
        return

    user=str(username.get())

    if(len(user)==0):
        msg.showinfo('Information', 'Username field should not be empty')
        return

    passw=str(newpass.get())
    confirmpassw=str(confirmpass.get())

    if(len(passw)==0):
        msg.showinfo('Information', 'Password field should not be empty')
        return

    if(len(confirmpassw)==0):
        msg.showinfo('Information', 'Confirm Password field should not be empty')
        return

    if(passw != confirmpassw):
        msg.showinfo('Information', 'Passwords and Confirm Passwords field do not match')
        return

    sql3 = "SELECT * FROM login WHERE contact_number = %s "
    cur.execute(sql3, (contact,))
    recor = cur.fetchall()

    if (cur.rowcount != 0):
       msg.showinfo('Information', 'This contact number already has a username')
       return
    else:
        sql2="Insert into create_account(name_organization,name_owner,address,contact_number) values(%s,%s,%s,%s)"
        cur.execute(sql2, (na,na1,addr,contact))
        con.commit()
        sql4="Insert into login (username,password,contact_number) values (%s,%s,%s)"
        cur.execute(sql4, (user, passw, contact))
        con.commit()

    con.close()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("3000x2500")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify


    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()

    Button(login_screen, text="Login", width=30, height=2, bg="red", command=login_verify).pack()
    Button(login_screen, text="GO BACK", width=30, height=2, bg="orange", command=destroy_login).pack()


def destroy_login():
    login_screen.destroy()


def login_verify():
    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    user = str(username_verify.get())
    passwd = str(password_verify.get())
    global contact1

    contact1=StringVar()

    cur.execute("SELECT * FROM login")

    flag = 0
    rows = cur.fetchall()

    for row in rows:

        if (row[0] == user):
            if (row[1] == passwd):
                flag = 1
                break
            else:
                flag = 2
                break
        else:
            flag = 3
            # user_not_found()


    if (flag == 1):
        contact1.set(row[2])
        print(contact1)
        login_sucess()
    elif (flag == 2):
        incorrect_password()
    else:
        user_not_found()

    con.close()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    # Button(login_success_screen, text="OK", command=delete_login_success).pack()
    Button(login_success_screen, text="OK", command=menu).pack()

def add_asset_liablity():
    global add_asset_liablity_screen
    add_asset_liablity_screen = Toplevel(main_screen)
    add_asset_liablity_screen.title("ADD Liabity or Asset")
    add_asset_liablity_screen.geometry("3000x2500")
    Label(add_asset_liablity_screen, text="Please enter details below to login").pack()
    Label(add_asset_liablity_screen, text="").pack()

    global amount
    global description
    global l_or_a

    amount = StringVar()
    description = StringVar()
    l_or_a = IntVar()

    Label(add_asset_liablity_screen, text="Amount * ").pack()
    Amount_entry = Entry(add_asset_liablity_screen, textvariable=amount)
    Amount_entry.pack()
    Label(add_asset_liablity_screen, text="").pack()

    Label(add_asset_liablity_screen, text="Description ").pack()
    Description_entry = Entry(add_asset_liablity_screen, textvariable=description)
    Description_entry.pack()
    Label(add_asset_liablity_screen, text="").pack()

    gender_label = Label(add_asset_liablity_screen, text="Select One")
    gender_label.pack()
    R1 = Radiobutton(add_asset_liablity_screen, text="Liability", variable=l_or_a, value=1,
                     command=sel)
    R1.pack(anchor=W)

    R2 = Radiobutton(add_asset_liablity_screen, text="Asset", variable=l_or_a, value=2,
                     command=sel)
    R2.pack(anchor=W)


    Label(add_asset_liablity_screen, text="").pack()

    Button(add_asset_liablity_screen, text="ADD ", width=30, height=2, bg="red", command=add_asset_liabiltiy_sql).pack()
    Button(add_asset_liablity_screen, text="GO BACK", width=30, height=2, bg="orange", command=destroy_add_asset_liabiltiy).pack()

def destroy_add_asset_liabiltiy():
    add_asset_liablity_screen.destroy()
def add_asset_liabiltiy_sql():
    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    contact2 = str(contact1.get())
    amt=str(amount.get())
    desc=str(description.get())
    type=str(l_or_a.get())
    if(type=='1'):
        type1='Liability'
    elif(type=='2'):
        type1='Asset'
    else:
        pass

    trans_date = datetime.datetime.now()
    sql2 = "Insert into asset_liability(description,type,amount,contact_number,transaction_date) values(%s,%s,%s,%s,%s)"
    cur.execute(sql2, (desc, type1, amt, contact2, trans_date))
    con.commit()

def income_expense_graph():
    global income_expense_graph_screen
    income_expense_graph_screen = Toplevel(main_screen)
    income_expense_graph_screen.title("Login")
    income_expense_graph_screen.geometry("3000x2500")
    Label(income_expense_graph_screen, text="Please enter details below to login").pack()
    Label(income_expense_graph_screen, text="").pack()

    global year1

    year1 = StringVar()

    Label(income_expense_graph_screen, text="Year* ").pack()
    year_entry = Entry(income_expense_graph_screen, textvariable=year1)
    year_entry.pack()
    Label(income_expense_graph_screen ,text="").pack()


    Button(income_expense_graph_screen, text="SHOW PLOT", width=30, height=2, bg="red", command=income_expense_graph_sql).pack()
    Button(income_expense_graph_screen, text="GO BACK", width=30, height=2, bg="orange", command=destroy_graph).pack()

def destroy_graph():
    income_expense_graph_screen.destroy()

def income_expense_graph_sql():
    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    contact2=str(contact1.get())
    year=str(year1.get())
    cur.execute("Select SUM(amount),month(transaction_date) FROM income WHERE year(transaction_date)=%s AND contact_number=%s GROUP BY month(transaction_date) ORDER BY month(transaction_date) " % (year,contact2))
    result = cur.fetchall()
    valuei = []
    valuee = []
    monthi=[]
    monthe=[]
    #months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    for i in result:
        print(i[0])
        print(i[1])
        valuei.append(i[0])
        monthi.append(i[1])

    cur.execute("Select SUM(amount),month(transaction_date) FROM expense WHERE year(transaction_date)=%s AND contact_number=%s GROUP BY month(transaction_date) ORDER BY month(transaction_date) "% (year, contact2))
    result1 = cur.fetchall()

    for i in result1:
        valuee.append(i[0])
        monthe.append(i[1])

    plt.plot(monthi, valuei, label="Income")
    plt.plot(monthe, valuee, label="Expense")

    plt.legend()
    plt.xlabel("Months of the Year")
    plt.ylabel("Rupees")
    plt.title("Income and Expenses Graph")

    plt.show()


def incorrect_password():
    global incorrect_password_screen
    incorrect_password_screen = Toplevel(login_screen)
    incorrect_password_screen.title("Success")
    incorrect_password_screen.geometry("150x100")
    Label(incorrect_password_screen, text="Incorrect Password ").pack()
    Button(incorrect_password_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    incorrect_password_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def add_income():
    global add_income_screen
    add_income_screen = Toplevel(main_screen)
    add_income_screen.title("ADD INCOME")
    add_income_screen.geometry("3000x2500")
    Label(add_income_screen, text="Please enter details below to login").pack()
    Label(add_income_screen, text="").pack()

    global amount
    global description
    global type_of_income

    amount = StringVar()
    description = StringVar()
    type_of_income = IntVar()

    Label(add_income_screen, text="Amount * ").pack()
    Amount_entry = Entry(add_income_screen, textvariable=amount)
    Amount_entry.pack()
    Label(add_income_screen, text="").pack()

    Label(add_income_screen, text="Description ").pack()
    Description_entry = Entry(add_income_screen, textvariable=description)
    Description_entry.pack()
    Label(add_income_screen, text="").pack()

    gender_label = Label(add_income_screen, text="Select Type of Income")
    gender_label.pack()
    R1 = Radiobutton(add_income_screen, text="Product Sales", variable=type_of_income, value=1,
                     command=sel)
    R1.pack(anchor=W)

    R2 = Radiobutton(add_income_screen, text="Service Sales", variable=type_of_income, value=2,
                     command=sel)
    R2.pack(anchor=W)


    Label(add_income_screen, text="").pack()

    Button(add_income_screen, text="ADD INCOME", width=30, height=2, bg="red", command=income_sql).pack()
    Button(add_income_screen, text="GO BACK", width=30, height=2, bg="orange", command=destroy_add_income).pack()


def destroy_add_income():
    add_income_screen.destroy()


def income_sql():
    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    amt = str(amount.get())

    if len(amt) == 0:
        msg.showinfo('Information', 'Amount field should not be empty')
        return

    if (amt == '0'):
        msg.showinfo('Information', 'Amount cannot be zero')
        return

    desc = str(description.get())

    if (len(desc) == 0):
        msg.showinfo('Information', 'Description field should not be empty')
        return

    type = str(type_of_income.get())

    if (type == '1'):
        type1 = 'Product'
    elif (type == '2'):
        type1 = 'Service'
    else:
        msg.showinfo('Information', 'Select the type of Income')
        return

    trans_date = datetime.datetime.now()
    contact2=str(contact1.get())
    sql2 = "Insert into income(description,income_type,amount,contact_number,transaction_date) values(%s,%s,%s,%s,%s)"
    cur.execute(sql2,(desc,type1, amt,contact2,trans_date))
    con.commit()

    update_pnl(type,'2022',amt)


def sel():
    selection = 0
    return selection

def destroy_add_expense():
    add_expense_screen.destroy()

def add_expense():
    global add_expense_screen
    add_expense_screen = Toplevel(main_screen)
    add_expense_screen.title("ADD EXPENSE")
    add_expense_screen.geometry("3000x2500")
    Label(add_expense_screen, text="Please enter details below to login").pack()
    Label(add_expense_screen, text="").pack()

    global amount1
    global description1
    global type_of_expense

    amount1 = StringVar()
    description1 = StringVar()
    type_of_expense = IntVar()

    Label(add_expense_screen, text="Amount * ").pack()
    Amount_entry = Entry(add_expense_screen, textvariable=amount1)
    Amount_entry.pack()
    Label(add_expense_screen, text="").pack()

    Label(add_expense_screen, text="Description ").pack()
    Description_entry = Entry(add_expense_screen, textvariable=description1)
    Description_entry.pack()
    Label(add_expense_screen, text="").pack()

    gender_label = Label(add_expense_screen, text="Select Type of Income")
    gender_label.pack()
    R1 = Radiobutton(add_expense_screen, text=" Sales expense", variable=type_of_expense, value=3,
                     command=sel)
    R1.pack(anchor=W)

    R2 = Radiobutton(add_expense_screen, text="Administrative Expense", variable=type_of_expense, value=4,
                     command=sel)
    R2.pack(anchor=W)

    R3 = Radiobutton(add_expense_screen, text="Manufacturing Expense", variable=type_of_expense, value=5,
                     command=sel)
    R3.pack(anchor=W)

    Label(add_expense_screen, text="").pack()

    Button(add_expense_screen, text="ADD EXPENSE", width=30, height=2, bg="red", command=expense_sql).pack()
    Button(add_expense_screen, text="GO BACK", width=30, height=2, bg="orange", command=destroy_add_expense).pack()



def expense_sql():
    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    amount = str(amount1.get())

    if len(amount) == 0:
        msg.showinfo('Information', 'Amount field should not be empty')
        return


    desc = str(description1.get())

    if (len(desc) == 0):
        msg.showinfo('Information', 'Description field should not be empty')
        return

    type = str(type_of_expense.get())
    if type == '3':
        type1 = 'Sales'
    elif type == '4':
        type1 = 'Administrative'
    elif type == '5':
        type1 = "Manufacturing"
    else:
        msg.showinfo('Information', 'Select the type of Expense')
        return
    transaction_date = datetime.datetime.now()
    contact2 = str(contact1.get())
    sql2 = "Insert into expense(description,expense_type,amount,contact_number,transaction_date) values(%s,%s,%s,%s,%s)"
    cur.execute(sql2, (desc, type1, amount, contact2, transaction_date))
    update_pnl(type,'2022',amount)
    con.commit()

def balance_sheet():
    global balance_sheet_screen
    balance_sheet_screen = Toplevel(main_screen)
    balance_sheet_screen.title("Balance Sheet")
    balance_sheet_screen.geometry("3000x2500")
    asset=0
    liability=0
    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    contact2 = str(contact1.get())
    cur.execute("SELECT type,amount FROM asset_liability WHERE contact_number= %s" % contact2)

    rows = cur.fetchall()

    for row in rows:
        if(row[0]=='Asset'):
            asset+=int(row[1])
        else:
            liability+=int(row[1])

    Label(balance_sheet_screen, text='Asset').grid(row=5, column=0, columnspan=2)
    var = StringVar()
    var.set(str(asset))
    myLabel = Label(balance_sheet_screen, textvariable=var, relief='raised', width=30, height=2)
    myLabel.grid(row=5, column=2, columnspan=2)

    Label(balance_sheet_screen, text='Liability').grid(row=6, column=0, columnspan=2)
    var = StringVar()
    var.set(str(liability))
    myLabel = Label(balance_sheet_screen, textvariable=var, relief='raised', width=30, height=2)
    myLabel.grid(row=6, column=2, columnspan=2)

    balance=asset-liability
    Label(balance_sheet_screen, text='Balance').grid(row=7, column=0, columnspan=2)
    var = StringVar()
    var.set(str(balance))
    myLabel = Label(balance_sheet_screen, textvariable=var, relief='raised', width=30, height=2)
    myLabel.grid(row=7, column=2, columnspan=2)

def pnl():
    global pnl_screen
    pnl_screen = Toplevel(main_screen)
    pnl_screen.title("Profit and Loss")
    pnl_screen.geometry("3000x2500")

    global year
    year = IntVar()

    Label(pnl_screen, text="Year * ").pack()
    year_entry = Entry(pnl_screen, textvariable=year)
    year_entry.pack()
    Label(pnl_screen, text="").pack()

    Button(pnl_screen, text="SHOW STATEMENT", width=30, height=2, bg="red", command=pnl_sql).pack()
    Button(pnl_screen, text="GO BACK", width=30, height=2, bg="orange", command=destroy_pnl).pack()


def pnl_sql():
    global pnl_screen1
    pnl_screen1 = Toplevel(main_screen)
    pnl_screen1.title("Profit and Loss Statement")
    pnl_screen1.geometry("3000x2500")

    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()
    year1=str(year.get())
    cur.execute("SELECT * FROM pnl WHERE year = %s" % year1)
    rows = cur.fetchall()

    for row in rows:

        if (row[0] == 'NULL'):
            ps = 0
        else:
            ps=int(row[0])

        if(row[1]=='NULL'):
            ss=0
        else:
            ss=int(row[1])


        if (row[2] == 'NULL'):
            me = 0
        else:
            me=int(row[2])

        if (row[3] == 'NULL'):
            se = 0
        else:
            se=int(row[3])

        if(row[4] == 'NULL'):
            ae = 0
        else:
            ae=int(row[4])

        if(row[5]=='NULL'):
            dep=0
        else:
            dep=int(row[5])
        if(row[6]=='NULL'):
            rate=0
        else:
            rate=int(row[6])


        tax_rate=int(row[7])

        if(row[10]=='NULL'):
            loan_amt=0
        else:
            loan_amt=int(row[10])

    ts = ps + ss
    total_operating_expense = se+ae
    grossprofit = ts - me

    Label(pnl_screen1, text='Product Sales').grid(row=5, column=0, columnspan=2)
    var=StringVar()
    var.set(str(ps))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=5, column=2, columnspan=2)

    Label(pnl_screen1, text='Service Sales').grid(row=6, column=0, columnspan=2)
    var = StringVar()
    var.set(str(ss))
    myLabel = Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=6, column=2, columnspan=2)

    Label(pnl_screen1, text='Total Sales').grid(row=7, column=0, columnspan=2)
    var = StringVar()
    var.set(str(ts))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=7, column=2, columnspan=2)

    Label(pnl_screen1, text='Manufacturing Expense').grid(row=9, column=0, columnspan=2)
    var = StringVar()
    var.set(str(me))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=9, column=2, columnspan=2)


    Label(pnl_screen1, text='Gross Profit').grid(row=10, column=0, columnspan=2)
    var = StringVar()
    var.set(str(grossprofit))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=10, column=2, columnspan=2)

    Label(pnl_screen1, text='Sales Expense').grid(row=12, column=0, columnspan=2)
    var = StringVar()
    var.set(str(se))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=12, column=2, columnspan=2)

    Label(pnl_screen1, text='Administrative Expense').grid(row=13, column=0, columnspan=2)
    var = StringVar()
    var.set(str(ae))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=13, column=2, columnspan=2)

    Label(pnl_screen1, text='Total Operating Expense').grid(row=14, column=0, columnspan=2)
    var = StringVar()
    var.set(str(total_operating_expense))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=14, column=2, columnspan=2)

    pbitd=grossprofit-total_operating_expense
    Label(pnl_screen1, text='PROFIT BEFORE INTEREST, TAX AND DEPRECIATION - PBITD').grid(row=16, column=0, columnspan=2)
    var = StringVar()
    var.set(str(pbitd))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=16, column=2, columnspan=2)

    Label(pnl_screen1, text='Depreciation').grid(row=17, column=0, columnspan=2)
    var = StringVar()
    var.set(str(dep))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=17, column=2, columnspan=2)

    pbit=ts - me - total_operating_expense-dep
    Label(pnl_screen1, text='PROFIT BEFORE INTEREST, TAX  - PBIT').grid(row=18, column=0, columnspan=2)
    var = StringVar()
    var.set(str(pbit))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=18, column=2, columnspan=2)

    interest=(loan_amt*rate)/100.0
    Label(pnl_screen1, text='Interest').grid(row=19, column=0, columnspan=2)
    var = StringVar()
    var.set(str(interest))
    myLabel =Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=19, column=2, columnspan=2)

    pbt = pbit-interest
    Label(pnl_screen1, text='PROFIT BEFORE TAX  - PBT').grid(row=20, column=0, columnspan=2)
    var = StringVar()
    var.set(str(pbt))
    myLabel = Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=20, column=2, columnspan=2)

    if(pbt<=0):
        tax=0
    else:
        tax=(pbt*tax_rate)/100.0

    Label(pnl_screen1, text='Tax').grid(row=21, column=0, columnspan=2)
    var = StringVar()
    var.set(str(tax))
    myLabel = Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=21, column=2, columnspan=2)

    pat=pbt-tax
    Label(pnl_screen1, text='PROFIT AFTER TAX  - PAT').grid(row=22, column=0, columnspan=2)
    var = StringVar()
    var.set(str(pat))
    myLabel = Label(pnl_screen1, textvariable=var, relief='raised',width=30, height=2)
    myLabel.grid(row=22, column=2, columnspan=2)


def destroy_pnl():
    pnl_screen.destroy()

def update_pnl(type,year,amount):
    con = mysql.connector.connect(db='accounts', user='root', passwd='Fullrevenge1!', host='localhost')
    cur = con.cursor()

    contact2 = str(contact1.get())
    cur.execute("SELECT * FROM pnl WHERE year = %s AND contact_number = %s" % (year,contact2))
    rows = cur.fetchall()
    print(cur.rowcount)
    if(cur.rowcount ==0):
        sql2 = "Insert into pnl(product_sales,service_sales,manufacturing_e,sales_e,administrative_e,depreciation,rate,tax_rate,year,contact_number,loan_amount) " \
               "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql2, ('NULL','NULL','NULL','NULL','NULL','NULL','NULL','40',year,contact2,'NULL'))
        con.commit()

    sales = 0
    if(type=='1'):
        cur.execute("SELECT product_sales FROM pnl WHERE year = %s AND contact_number=%s" % (year,contact2))
        rows = cur.fetchall()
        for row in rows:
            if (row[0] == 'NULL'):
                sales = 0
            else:
                sales = int(row[0])
            print(row[0])
        sales+=int(amount)
        cur.execute("UPDATE pnl SET product_sales = %s WHERE year = %s AND contact_number=%s" % (str(sales), year,contact2))

    elif(type=='2'):
        cur.execute("SELECT service_sales FROM pnl WHERE year = %s AND contact_number=%s" % (year,contact2))
        rows = cur.fetchall()
        for row in rows:
            if (row[0] == 'NULL'):
                sales = 0
            else:
                sales = int(row[0])
            print(row[0])
        sales += int(amount)
        cur.execute("UPDATE pnl SET service_sales = %s WHERE year = %s AND contact_number=%s" % (str(sales), year,contact2))

    elif(type=='3'):
        cur.execute("SELECT sales_e FROM pnl WHERE year = %s AND contact_number=%s" % (year,contact2))
        rows = cur.fetchall()
        for row in rows:
            if (row[0] == 'NULL'):
                sales = 0
            else:
                sales = int(row[0])
            print(row[0])
        sales += int(amount)
        cur.execute("UPDATE pnl SET sales_e = %s WHERE year = %s AND contact_number=%s" % (str(sales), year,contact2))
        con.commit()
    elif(type=='4'):
        cur.execute("SELECT administrative_e FROM pnl WHERE year = %s AND contact_number=%s" % (year,contact2))
        rows = cur.fetchall()
        for row in rows:
            if (row[0] == 'NULL'):
                sales = 0
            else:
                sales = int(row[0])
            print(row[0])
        sales += int(amount)
        cur.execute("UPDATE pnl SET administrative_e = %s WHERE year = %s AND contact_number=%s" % (str(sales), year,contact2))

    elif(type=='5'):
        cur.execute("SELECT manufacturing_e FROM pnl WHERE year = %s AND contact_number=%s" % (year,contact2))
        rows = cur.fetchall()
        for row in rows:
            if (rows[0] == 'NULL'):
                sales = 0
            else:
                sales = int(rows[0])
            print(row[0])
        sales += int(amount)
        cur.execute("UPDATE pnl SET manufacturing_e = %s WHERE year = %s AND contact_number=%s " % (str(sales), year,contact2))
    con.commit()
    con.close()


def menu():
    global menu_screen
    menu_screen = Toplevel(main_screen)
    menu_screen.title("menu")
    menu_screen.geometry("3000x2500")
    Label(menu_screen, text="Menu", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Add Income", height="2", width="30", fg='black', bg='violet', command=add_income).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Add Expense", height="2", width="30", fg='black', bg='violet', command=add_expense).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Profit and Loss", height="2", width="30", fg='black', bg='violet', command=pnl).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Income and Expense Graph", height="2", width="30", fg='black', bg='violet', command=income_expense_graph).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Add Asset or Liability", height="2", width="30", fg='black', bg='violet',command=add_asset_liablity).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Balance Sheet", height="2", width="30", fg='black', bg='violet', command=balance_sheet).pack()
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Logout", height="2", width="30", fg='black', bg='violet', command=logout2).pack()
    Label(menu_screen, text="").pack()


def exiting():
    main_screen.destroy()


def logout2():
    menu_screen.destroy()


def home():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x2500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="50", fg='black', bg='green', font=("Arial Bold", 10), command=login).pack()
    Label(text="").pack()
    Button(text="Create new username", height="5", width="50", fg='black', bg='blue', font=("Arial Bold", 10),
           command=create_account).pack()
    Label(text="").pack()
    Button(text="Exit", height="5", width="50", fg='black', bg='red', font=("Arial Bold", 10),
           command=exiting).pack()

    main_screen.mainloop()


home()