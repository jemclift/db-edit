from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+input("What is the path of your db file ➜ ")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class users(db.Model):
    __tablename__ = 'users'
#     __tablename__ = input("What is the name of the table you want to edit ➜ ")
    __table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True)
    
def print_logo():
    print("""
    \u001b[30;1m──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\u001b[0m
    
    
                                           ╔═══╗               ╔═══╗
                                           ║ ✪ ╟───────────────╢ ✪ ║
                                           ╚═╤═╬═══════════════╬═╤═╝
                         \u001b[31;1mbbbbbbbb\u001b[0m            │ ║  \u001b[1mMade by Jem\u001b[0m  ║ │                 \u001b[35;1mdddddddd\u001b[0m
    \u001b[34;1mDDDDDDDDDDDDD        \u001b[31;1mb::::::b\u001b[0m          ╔═╧═╬═══════════════╬═╧═╗               \u001b[35;1md::::::d  \u001b[33miiii           \u001b[36mtttt\u001b[0m
    \u001b[34;1mD::::::::::::DDD     \u001b[31;1mb::::::b\u001b[0m          ║ ✪ ╟───────────────╢ ✪ ║               \u001b[35;1md::::::d \u001b[33mi::::i       \u001b[36mttt:::t\u001b[0m
    \u001b[34;1mD:::::::::::::::DD   \u001b[31;1mb::::::b\u001b[0m          ╚═══╝               ╚═══╝               \u001b[35;1md::::::d  \u001b[33miiii        \u001b[36mt:::::t\u001b[0m
    \u001b[34;1mDDD:::::DDDDD:::::D   \u001b[31;1mb:::::b                                                 \u001b[35;1md:::::d               \u001b[36mt:::::t\u001b[0m
      \u001b[34;1mD:::::D    D:::::D  \u001b[31;1mb:::::bbbbbbbbb             \u001b[32;1meeeeeeeeeeee         \u001b[35;1mddddddddd:::::d \u001b[33miiiiiii \u001b[36mttttttt:::::ttttttt\u001b[0m
      \u001b[34;1mD:::::D     D:::::D \u001b[31;1mb::::::::::::::bb         \u001b[32;1mee::::::::::::ee     \u001b[35;1mdd::::::::::::::d \u001b[33mi:::::i \u001b[36mt:::::::::::::::::t\u001b[0m
      \u001b[34;1mD:::::D     D:::::D \u001b[31;1mb::::::::::::::::b       \u001b[32;1me::::::eeeee:::::ee  \u001b[35;1md::::::::::::::::d  \u001b[33mi::::i \u001b[36mt:::::::::::::::::t\u001b[0m
      \u001b[34;1mD:::::D     D:::::D \u001b[31;1mb:::::bbbbb:::::::b     \u001b[32;1me::::::e     e:::::e \u001b[35;1md:::::::ddddd:::::d  \u001b[33mi::::i \u001b[36mtttttt:::::::tttttt\u001b[0m
      \u001b[34;1mD:::::D     D:::::D \u001b[31;1mb:::::b    b::::::b     \u001b[32;1me:::::::eeeee::::::e \u001b[35;1md::::::d    d:::::d  \u001b[33mi::::i       \u001b[36mt:::::t\u001b[0m
      \u001b[34;1mD:::::D     D:::::D \u001b[31;1mb:::::b     b:::::b     \u001b[32;1me:::::::::::::::::e  \u001b[35;1md:::::d     d:::::d  \u001b[33mi::::i       \u001b[36mt:::::t\u001b[0m
      \u001b[34;1mD:::::D     D:::::D \u001b[31;1mb:::::b     b:::::b     \u001b[32;1me::::::eeeeeeeeeee   \u001b[35;1md:::::d     d:::::d  \u001b[33mi::::i       \u001b[36mt:::::t\u001b[0m
      \u001b[34;1mD:::::D    D:::::D  \u001b[31;1mb:::::b     b:::::b     \u001b[32;1me:::::::e            \u001b[35;1md:::::d     d:::::d  \u001b[33mi::::i       \u001b[36mt:::::t    tttttt\u001b[0m
    \u001b[34;1mDDD:::::DDDDD:::::D   \u001b[31;1mb:::::bbbbbb::::::b     \u001b[32;1me::::::::e           \u001b[35;1md::::::ddddd::::::dd\u001b[33mi::::::i      \u001b[36mt::::::tttt:::::t\u001b[0m
    \u001b[34;1mD:::::::::::::::DD    \u001b[31;1mb::::::::::::::::b       \u001b[32;1me::::::::eeeeeeee    \u001b[35;1md:::::::::::::::::d\u001b[33mi::::::i      \u001b[36mtt::::::::::::::t\u001b[0m
    \u001b[34;1mD::::::::::::DDD      \u001b[31;1mb:::::::::::::::b         \u001b[32;1mee:::::::::::::e     \u001b[35;1md:::::::::ddd::::d\u001b[33mi::::::I        \u001b[36mtt:::::::::::tt\u001b[0m
    \u001b[34;1mDDDDDDDDDDDDD         \u001b[31;1mbbbbbbbbbbbbbbbb            \u001b[32;1meeeeeeeeeeeeee      \u001b[35;1mddddddddd   ddddd\u001b[33miiiiiiii          \u001b[36mttttttttttt\u001b[0m


    \u001b[30;1m──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\u001b[0m""")



def draw_table():
    search = users.query
    columns = users.__table__.columns.keys()
    records = []
    
    records.append(columns)
    for user in search:
        new_record = []
        for column in columns:
            new_record.append(getattr(user, column))
        records.append(new_record)

    # Find the maximum length of each coloumn

    lengths = []   
    for column in range(len(records[0])):
        max_length = 0
        for row in records:
            if len(str(row[column])) > max_length:
                max_length = len(str(row[column]))
        lengths.append(max_length)

    # Draw table

    print("\n ┌",end="")
    for index, length in enumerate(lengths):
        print("─"*(length+2),end="")
        if index != len(lengths)-1:
            print("┬",end="")
    print("┐\n ",end="")

    for record_id, record in enumerate(records):
        if record_id == 0:
            for index, value in enumerate(record):
                print("│\u001b[1m\u001b[46;1m",str(value).center(lengths[index],' '),end=" \u001b[0m")
            print("│\n ",end="")
        else:  
            for index, value in enumerate(record):
                print("│",str(value).ljust(lengths[index],' '),end=" ")
            print("│\n ",end="")

        if record_id != len(records)-1:
            print("├",end="")
            for index, length in enumerate(lengths):
                print("─"*(length+2),end="")
                if index != len(lengths)-1:
                    print("┼",end="")
            print("┤\n ",end="")

    print("└",end="")
    for index, length in enumerate(lengths):
        print("─"*(length+2),end="")
        if index != len(lengths)-1:
            print("┴",end="")
    print("┘")
    
    input("\n \u001b[1mPRESS ENTER TO CONTINUE \u001b[0m")

def delete():
    search_id = input("\n ID of the user ➜ ")
    search = users.query.filter_by(id=search_id).first()
    columns = users.__table__.columns.keys()

    if search is None:
        print("User not found\n")
    else:
        print()
        record = []
        for column in columns:
            record.append(str(getattr(search,column)))
        columns_len = len(max(columns,key=len))
        values_len = len(max(record,key=len))
        print(" ┌─"+("─"*columns_len)+"─┬─"+("─"*values_len)+"─┐")
        for row in range(len(columns)):
            print(" │ "+columns[row].ljust(columns_len," ")+" │ "+record[row].ljust(values_len," ")+" │")
            if row != len(columns)-1:
                print(" ├─"+("─"*columns_len)+"─┼─"+("─"*values_len)+"─┤")
        print(" └─"+("─"*columns_len)+"─┴─"+("─"*values_len)+"─┘")

    if input("\n Are you sure you want to delete this user? y/n ") == "y": 
        db.session.delete(search)
        db.session.commit()
        print("\n [ Deleted ]")

def insert():
    columns = users.__table__.columns.keys()
    
    new = users()
    print()
    for column in columns[1:]:
        setattr(new, column, input(" \u001b[43;1m\u001b[30;1m Enter "+column+" \u001b[0m\n ➜ "))

    db.session.add(new)
    db.session.commit()
    
if __name__ == "__main__":
    print_logo()
    while True:
        print(
"""
 ╔══════════════════════════╗
 ║\u001b[44;1m       \u001b[1mDB EDIT MENU       \u001b[0m║
 ╚══════════════════════════╝
 ╔═══╤══════════════════════╗
 ║ 1 │ View                 ║
 ╟───┼──────────────────────╢
 ║ 2 │ \u001b[31;1mDelete\u001b[0m               ║
 ╟───┼──────────────────────╢
 ║ 3 │ Insert               ║
 ╟───┼──────────────────────╢
 ║ 4 │ Quit                 ║
 ╚═══╧══════════════════════╝
""")
        choice = input(" ➜ ")
        if choice.lower() == "v" or choice.lower() == "view" or choice == "1":
            draw_table()
        elif choice.lower() == "d" or choice.lower() == "delete" or choice == "2":
            delete()
        elif choice.lower() == "i" or choice.lower() == "insert" or choice == "3":
            insert()
        elif choice.lower() == "q" or choice.lower() == "quit" or choice == "4":
            print()
            break
