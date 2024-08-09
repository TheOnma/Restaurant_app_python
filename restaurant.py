from tkinter import *

# Initialize Tkinter
application = Tk()

# Window size
application.geometry('1020x630+0+0')

# Prevent from maximising
application.resizable(False, False)

# Window title
application.title('My Restaurant - Invoicing System')

# Window background color
application.config(bg='burlywood')

# Top panel
top_panel = Frame(application, bd= 1, relief= FLAT)
top_panel.pack(side= TOP)

# Title tag
title_tag = Label(top_panel, text= 'Invoicing System', fg= 'azure4', font=('Dosis', 58), bg='burlywood', width=27)
title_tag.grid(row=0, column=0)

# Left panel
left_panel = Frame(application, bd=1, relief = FLAT)
left_panel.pack(side=LEFT)

# Cost Panel
cost_panel = Frame(left_panel, bd=1, relief= FLAT)
left_panel.pack(side= BOTTOM)

# Food panel
food_panel = LabelFrame(left_panel, text= 'Food', font= ('Dosis', 19, 'bold'), bd= 1, relief= FLAT, fg= 'azure4')
food_panel.pack(side= LEFT)

# Drink panel
drink_panel = LabelFrame(left_panel, text= 'Drink', font= ('Dosis', 19, 'bold'), bd= 1, relief= FLAT, fg= 'azure4')
drink_panel.pack(side= LEFT)

# Dessert panel
dessert_panel = LabelFrame(left_panel, text= 'Dessert', font= ('Dosis', 19, 'bold'), bd= 1, relief= FLAT, fg= 'azure4')
dessert_panel.pack(side= LEFT)

# Right Panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
calculator_panel.pack()

# Invoice panel
invoice_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
invoice_panel.pack()

# Buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
buttons_panel.pack()

# Product lists
food_list = ['Chicken', 'Lamb', 'Salmon', 'Hake', 'Kebabs', 'Pizza1', 'Pizza2', 'Pizza3']
drink_list = ['Lemonade', 'Soda', 'Juice', 'Cola', 'Wine1', 'Wine2', 'Beer1', 'Beer2']
dessert_list = ['Ice cream', 'Fruit', 'Brownies', 'Pudding', 'Cheesecake', 'Cake1', 'Cake2', 'Cake3']

# Create food items
food_variables = []
food_box = []
food_text = []
counter = 0
for food in food_list:

    #Create checkbuttons
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,
                       text= food.title(),
                       font=('Dosis', 19, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=food_variables[counter])
    food.grid(row= counter,
              column=0,
              sticky=W)

    #Create input boxes
    food_box.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_box[counter] = Entry(food_panel,
                              font= ('Dosis', 18, 'bold'),
                              bd = 1,
                              width=6,
                              state=DISABLED,
                              textvariable=food_text[counter])
    food_box[counter].grid(row=counter,
                           column=1)
    counter +=1



# Create drink items
drink_variables = []
drink_box = []
drink_text = []
counter = 0
for drink in drink_list:
    #Create checkbuttons
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel,
                        text= drink.title(),
                        font=('Dosis', 19, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=drink_variables[counter])
    drink.grid(row= counter,
               column=0,
               sticky=W)

    # Create input boxes
    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_box[counter] = Entry(drink_panel,
                              font=('Dosis', 18, 'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=drink_text[counter])
    drink_box[counter].grid(row=counter,
                           column=1)

    counter +=1


# Create dessert items
dessert_variables = []
dessert_box = []
dessert_text = []
counter = 0
for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel,
                          text= dessert.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=dessert_variables[counter])
    dessert.grid(row= counter,
                 column=0,
                 sticky=W)

    # Create input boxes
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_box[counter] = Entry(dessert_panel,
                               font=('Dosis', 18, 'bold'),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=dessert_text[counter])
    dessert_box[counter].grid(row=counter,
                            column=1)
    counter +=1

# Variables
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_cost_var = StringVar()
taxes_cost_var = StringVar()
total_cost_var = StringVar()

# Cost labels and input fields
food_cost_label = Label(cost_panel,
                        text= 'Food Cost',
                        font= ('Dosis', 12, 'bold'),
                        bg= 'azure4',
                        fg= 'white')
food_cost_label.grid(row=0, column=0)
food_cost_text = Entry(cost_panel,
                       font= ('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state= 'readonly',
                       textvariable= food_cost_var)
food_cost_text.grid(row=0, column=1)

drink_cost_label = Label(cost_panel,
                        text= 'Drink Cost',
                        font= ('Dosis', 12, 'bold'),
                        bg= 'azure4',
                        fg= 'white')
drink_cost_label.grid(row=0, column=0)
drink_cost_text = Entry(cost_panel,
                       font= ('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state= 'readonly',
                       textvariable= drink_cost_var)
drink_cost_text.grid(row=1, column=1)

dessert_cost_label = Label(cost_panel,
                        text= 'Dessert Cost',
                        font= ('Dosis', 12, 'bold'),
                        bg= 'azure4',
                        fg= 'white')
dessert_cost_label.grid(row=0, column=0)
dessert_cost_text = Entry(cost_panel,
                       font= ('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state= 'readonly',
                       textvariable= dessert_cost_var)
dessert_cost_text.grid(row=0, column=1)



# Prevent window from closing
application.mainloop()


