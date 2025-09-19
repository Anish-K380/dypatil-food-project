import PyQt6.QtWidgets as qtw
from functools import partial

class node:
    def __init__(self, value, button, prev = None, after = None):
        self.val = value
        self.button = button
        self.left = prev
        self.right = after

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        def turnwhite():self.current_button.setStyleSheet('background-color: white;')
        def turnblue():self.current_button.setStyleSheet('background-color: lightblue;')
        def shift_basic():
            layout2.setCurrentIndex(0)
            turnwhite()
            self.current_button = button_basic
            turnblue()
        def shift_contains():
            layout2.setCurrentIndex(1)
            turnwhite()
            self.current_button = button_contains
            turnblue()
        def shift_diet():
            layout2.setCurrentIndex(2)
            turnwhite()
            self.current_button = button_diet
            turnblue()
        def shift_disease():
            layout2.setCurrentIndex(3)
            turnwhite()
            self.current_button = button_disease
            turnblue()
        def shift_description():
            layout2.setCurrentIndex(4)
            turnwhite()
            self.current_button = button_description
            turnblue()
        def create_new_nutrient():
            if self.last_nutrient.val.text() != '':
                self.last_nutrient.val.returnPressed.disconnect(create_new_nutrient)
                self.last_nutrient.right = node(qtw.QLineEdit(), qtw.QPushButton('-'))
                self.last_nutrient.right.left = self.last_nutrient
                self.last_nutrient = self.last_nutrient.right
                nutrient_text.addWidget(self.last_nutrient.val)
                nutrient_button.addWidget(self.last_nutrient.button)
                self.last_nutrient.val.returnPressed.connect(create_new_nutrient)
                self.last_nutrient.val.setFocus()
                contains_buttons[self.contains_button_id] = self.last_nutrient
                nutrient_group.addButton(self.last_nutrient.button, self.contains_button_id)
                self.contains_button_id += 1
        def delete_nutrient(button):
            if self.last_nutrient.left == None:return None
            n_id = nutrient_group.id(button)
            nutrient = contains_buttons[n_id]
            if nutrient.right == None:
                self.last_nutrient = nutrient.left
                self.last_nutrient.val.returnPressed.connect(create_new_nutrient)
                self.last_nutrient.right = None
            else:nutrient.right.left = nutrient.left
            if nutrient.left != None:nutrient.left.right = nutrient.right
            nutrient.val.setParent(None)
            nutrient.button.setParent(None)
            nutrient.val.deleteLater()
            nutrient.button.deleteLater()
            contains_buttons.pop(n_id)
        def create_new_ingredient():
            if self.last_ingredient.val.text() != '':
                self.last_ingredient.val.returnPressed.disconnect(create_new_ingredient)
                self.last_ingredient.right = node(qtw.QLineEdit(), qtw.QPushButton('-'))
                self.last_ingredient.right.left = self.last_ingredient
                self.last_ingredient = self.last_ingredient.right
                ingredient_text.addWidget(self.last_ingredient.val)
                ingredient_button.addWidget(self.last_ingredient.button)
                self.last_ingredient.val.returnPressed.connect(create_new_ingredient)
                self.last_ingredient.val.setFocus()
                contains_buttons[self.contains_button_id] = self.last_ingredient
                ingredient_group.addButton(self.last_ingredient.button, self.contains_button_id)
                self.contains_button_id += 1
        def delete_ingredient(button):
            if self.last_ingredient.left == None:return None
            i_id = ingredient_group.id(button)
            ingredient = contains_buttons[i_id]
            if ingredient.right == None:
                self.last_ingredient = ingredient.left
                ingredient.left.val.returnPressed.connect(create_new_ingredient)
                ingredient.left.right = None
            else:ingredient.right.left = ingredient.left
            if ingredient.left != None:ingredient.left.right = ingredient.right
            ingredient.val.setParent(None)
            ingredient.button.setParent(None)
            ingredient.val.deleteLater()
            ingredient.button.deleteLater()
            contains_buttons.pop(i_id)
        def create_text(num):
            if len(last_text[num].val.text()) != 0:
                last_text[num].val.returnPressed.disconnect(functions[num])
                last_text[num].right = node(qtw.QLineEdit(), qtw.QPushButton('-'))
                last_text[num].right.left = last_text[num]
                last_text[num] = last_text[num].right
                text_layouts[num].addWidget(last_text[num].val)
                button_layouts[num].addWidget(last_text[num].button)
                last_text[num].val.returnPressed.connect(functions[num])
                last_text[num].val.setFocus()
                texts[self.button_id] = last_text[num]
                groups[num].addButton(last_text[num].button, self.button_id)
                self.button_id += 1
        def delete_text(num, button_id):
            if last_text[num].left == None:return None
            text = texts[button_id]
            if text.right == None:
                last_text[num] = text.left
                text.left.right = None
                text.left.val.returnPressed.connect(functions[num])
            else:text.right.left = text.left
            if text.left != None:text.left.right = text.right
            text.val.setParent(None)
            text.button.setParent(None)
            text.val.deleteLater()
            text.button.deleteLater()
            texts.pop(button_id)
        def anchor():
            temp = qtw.QWidget()
            temp.setFixedHeight(0)
            temp.setFixedWidth(0)
            return temp

        super().__init__()
        layout = qtw.QHBoxLayout() #master layout

        layout1 = qtw.QVBoxLayout()  #contains buttons and open space
        layout1_ = qtw.QVBoxLayout() #the empty space
        button_layout = qtw.QVBoxLayout() #contains the buttons

        layout2 = qtw.QStackedLayout() #will contain the content
        window_basic = qtw.QWidget()
        window_contains = qtw.QWidget()
        window_diet = qtw.QWidget()
        window_disease = qtw.QWidget()
        window_description = qtw.QWidget()
        layouta = qtw.QVBoxLayout()
        layoutb = qtw.QHBoxLayout()
        layoutc = qtw.QHBoxLayout()
        layoutd = qtw.QGridLayout()
        layoute = qtw.QGridLayout()

        button_basic = qtw.QPushButton('basic')
        button_contains = qtw.QPushButton('contains')
        button_diet = qtw.QPushButton('diet')
        button_disease = qtw.QPushButton('disease')
        button_description = qtw.QPushButton('description')
        button_exit = qtw.QPushButton('exit')

        self.current_button = button_basic
        turnblue()

        button_exit.clicked.connect(app.quit)

        button_layout.addWidget(button_basic)
        button_layout.addWidget(button_contains)
        button_layout.addWidget(button_diet)
        button_layout.addWidget(button_disease)
        button_layout.addWidget(button_description)
        button_layout.addStretch(6)
        button_layout.addWidget(button_exit)
        button_layout.addStretch(1)

        layouta.addStretch(2)
        layoutname = qtw.QHBoxLayout()
        layoutname.addStretch(1)
        layoutname.addWidget(qtw.QLabel('name:'))    #Basic page
        name = qtw.QLineEdit()
        layoutname.addWidget(name)
        layoutname.addStretch(1)
        layouta.addLayout(layoutname)
        layoutage = qtw.QHBoxLayout()
        layouta.addStretch(1)
        layoutage.addStretch(2)
        layoutage.addWidget(qtw.QLabel('Age Lower Limit:'))
        age_lower_limit = qtw.QSpinBox()
        age_lower_limit.setMinimum(0)
        age_lower_limit.setMaximum(200)
        layoutage.addWidget(age_lower_limit)
        layoutage.addStretch(1)
        layoutage.addWidget(qtw.QLabel('Age Upper Limit:'))
        age_upper_limit = qtw.QSpinBox()
        age_upper_limit.setMinimum(0)
        age_upper_limit.setMaximum(200)
        layoutage.addWidget(age_upper_limit)
        layoutage.addStretch(2)
        layouta.addLayout(layoutage)
        layouta.addStretch(1)
        layoutcalories = qtw.QHBoxLayout()
        layoutcalories.addStretch(1)
        layoutcalories.addWidget(qtw.QLabel('Calories:'))
        calories = qtw.QDoubleSpinBox()
        layoutcalories.addWidget(calories)
        layoutcalories.addWidget(qtw.QLabel('kcal/100gm'))
        layoutcalories.addStretch(1)
        layouta.addLayout(layoutcalories)
        layouta.addStretch(1)
        layoutquantity = qtw.QHBoxLayout()
        layoutquantity.addStretch(1)
        layoutquantity.addWidget(qtw.QLabel('Ideal quantity per serving:'))
        quantity = qtw.QDoubleSpinBox()
        quantity.setMinimum(0)
        layoutquantity.addWidget(quantity)
        quantityunit = qtw.QVBoxLayout()
        gm = qtw.QRadioButton('gms')
        mg = qtw.QRadioButton('mg')
        quantitygroup = qtw.QButtonGroup()
        quantitygroup.addButton(gm, 0)
        quantitygroup.addButton(mg, 1)
        quantityunit.addWidget(gm)
        quantityunit.addWidget(mg)
        layoutquantity.addLayout(quantityunit)
        layoutquantity.addStretch(1)
        layouta.addLayout(layoutquantity)
        layouta.addStretch(2)

        last_text = [0, 1]
        text_layouts = [0, 1]
        functions = [0, 1]
        button_layouts = [0, 1]
        groups = [0, 1]
        texts = dict()
        self.button_id = 5

        nutrient_half = qtw.QVBoxLayout()
        nutrient_header = qtw.QHBoxLayout()
        nutrient_content = qtw.QHBoxLayout()
        nutrient_text = qtw.QVBoxLayout()
        nutrient_button = qtw.QVBoxLayout()
        nutrient_header.addStretch(1)
        nutrient_header.addWidget(qtw.QLabel('Nutrients'))
        nutrient_header.addStretch(1)
        nutrient_text.addWidget(anchor())
        nutrient_button.addWidget(anchor())
        self.last_nutrient = node(qtw.QLineEdit(), qtw.QPushButton('-'))
        self.contains_button_id = 2
        self.last_nutrient.val.returnPressed.connect(create_new_nutrient)
        contains_buttons = dict()
        contains_buttons[0] = self.last_nutrient
        nutrient_group = qtw.QButtonGroup()
        nutrient_group.addButton(self.last_nutrient.button, 0)
        nutrient_group.buttonClicked.connect(delete_nutrient)
        nutrient_text.addWidget(self.last_nutrient.val)
        nutrient_button.addWidget(self.last_nutrient.button)
        nutrient_content.addStretch(1)
        nutrient_content.addLayout(nutrient_text)
        nutrient_content.addLayout(nutrient_button)
        nutrient_content.addStretch(1)
        nutrient_half.addLayout(nutrient_header)
        nutrient_half.addStretch(1)
        nutrient_half.addLayout(nutrient_content)
        nutrient_half.addStretch(4)
        ingredient_half = qtw.QVBoxLayout()
        ingredient_header = qtw.QHBoxLayout()
        ingredient_content = qtw.QHBoxLayout()
        ingredient_text = qtw.QVBoxLayout()
        ingredient_button = qtw.QVBoxLayout()
        ingredient_header.addStretch(1)
        ingredient_header.addWidget(qtw.QLabel('Ingredients'))
        ingredient_header.addStretch(1)
        ingredient_text.addWidget(anchor())
        ingredient_button.addWidget(anchor())
        self.last_ingredient = node(qtw.QLineEdit(), qtw.QPushButton('-'))
        self.last_ingredient.val.returnPressed.connect(create_new_ingredient)
        ingredients = dict()
        contains_buttons[1] = self.last_ingredient
        ingredient_group = qtw.QButtonGroup()
        ingredient_group.addButton(self.last_ingredient.button, 1)
        ingredient_group.buttonClicked.connect(delete_ingredient)
        ingredient_text.addWidget(self.last_ingredient.val)
        ingredient_button.addWidget(self.last_ingredient.button)
        ingredient_content.addStretch(1)
        ingredient_content.addLayout(ingredient_text)
        ingredient_content.addLayout(ingredient_button)
        ingredient_content.addStretch(1)
        ingredient_half.addLayout(ingredient_header)
        ingredient_half.addStretch(1)
        ingredient_half.addLayout(ingredient_content)
        ingredient_half.addStretch(4)
        layoutb.addLayout(nutrient_half)
        layoutb.addStretch(1)
        layoutb.addLayout(ingredient_half)
        layoutb.addStretch(1)

        bt_layout = qtw.QVBoxLayout()
        diet_layout = qtw.QVBoxLayout()
        btte_layout = qtw.QVBoxLayout()
        bt_header = qtw.QHBoxLayout()
        diet_header = qtw.QHBoxLayout()
        btte_header = qtw.QHBoxLayout()
        bt_header.addStretch(1)
        diet_header.addStretch(1)
        btte_header.addStretch(1)
        bt_header.addWidget(qtw.QLabel('Body Type'))
        diet_header.addWidget(qtw.QLabel('Diet'))
        btte_header.addWidget(qtw.QLabel('Best time to eat'))
        bt_header.addStretch(1)
        diet_header.addStretch(1)
        btte_header.addStretch(1)
        bt_layout.addLayout(bt_header)
        diet_layout.addLayout(diet_header)
        btte_layout.addLayout(btte_header)
        bt_layout.addStretch(1)
        diet_layout.addStretch(1)
        btte_layout.addStretch(1)
        bt_content = qtw.QHBoxLayout()
        diet_content = qtw.QHBoxLayout()
        btte_content = qtw.QHBoxLayout()
        bt_content.addStretch(1)
        diet_content.addStretch(1)
        btte_content.addStretch(1)
        bt_text = qtw.QVBoxLayout()
        diet_text = qtw.QVBoxLayout()
        btte_text = qtw.QVBoxLayout()
        bt_text.addWidget(anchor())
        diet_text.addWidget(anchor())
        btte_text.addWidget(anchor())
        bt_button = qtw.QVBoxLayout()
        diet_button = qtw.QVBoxLayout()
        btte_button = qtw.QVBoxLayout()
        bt_button.addWidget(anchor())
        diet_button.addWidget(anchor())
        btte_button.addWidget(anchor())
        last_text.append(node(qtw.QLineEdit(), qtw.QPushButton('-')))
        last_text.append(node(qtw.QLineEdit(), qtw.QPushButton('-')))
        last_text.append(node(qtw.QLineEdit(), qtw.QPushButton('-')))
        texts[2] = last_text[2]
        texts[3] = last_text[3]
        texts[4] = last_text[4]
        text_layouts.append(bt_text)
        text_layouts.append(diet_text)
        text_layouts.append(btte_text)
        button_layouts.append(bt_button)
        button_layouts.append(diet_button)
        button_layouts.append(btte_button)
        functions.append(partial(create_text, 2))
        functions.append(partial(create_text, 3))
        functions.append(partial(create_text, 4))
        groups.append(qtw.QButtonGroup())
        groups.append(qtw.QButtonGroup())
        groups.append(qtw.QButtonGroup())
        groups[2].addButton(last_text[2].button, 2)
        groups[3].addButton(last_text[3].button, 3)
        groups[4].addButton(last_text[4].button, 4)
        groups[2].idClicked.connect(partial(delete_text, 2))
        groups[3].idClicked.connect(partial(delete_text, 3))
        groups[4].idClicked.connect(partial(delete_text, 4))
        last_text[2].val.returnPressed.connect(functions[2])
        last_text[3].val.returnPressed.connect(functions[3])
        last_text[4].val.returnPressed.connect(functions[4])
        bt_text.addWidget(last_text[2].val)
        diet_text.addWidget(last_text[3].val)
        btte_text.addWidget(last_text[4].val)
        bt_button.addWidget(last_text[2].button)
        diet_button.addWidget(last_text[3].button)
        btte_button.addWidget(last_text[4].button)
        bt_content.addLayout(bt_text)
        diet_content.addLayout(diet_text)
        btte_content.addLayout(btte_text)
        bt_content.addLayout(bt_button)
        diet_content.addLayout(diet_button)
        btte_content.addLayout(btte_button)
        bt_content.addStretch(1)
        diet_content.addStretch(1)
        btte_content.addStretch(1)
        bt_layout.addLayout(bt_content)
        diet_layout.addLayout(diet_content)
        btte_layout.addLayout(btte_content)
        bt_layout.addStretch(4)
        diet_layout.addStretch(4)
        btte_layout.addStretch(4)
        layoutc.addLayout(bt_layout)
        layoutc.addLayout(diet_layout)
        layoutc.addLayout(btte_layout)
        
        layoutd.addWidget(qtw.QLabel('disease'), 4, 4)
        layoute.addWidget(qtw.QLabel('description'), 4, 4)

        window_basic.setLayout(layouta)
        window_contains.setLayout(layoutb)
        window_diet.setLayout(layoutc)
        window_disease.setLayout(layoutd)
        window_description.setLayout(layoute)

        layout1.addLayout(button_layout, stretch = 3)   #space taken by buttons in tabs bar
        layout1.addLayout(layout1_, stretch = 1)

        layout2.addWidget(window_basic)
        layout2.addWidget(window_contains)
        layout2.addWidget(window_diet)
        layout2.addWidget(window_disease)
        layout2.addWidget(window_description)

        button_basic.clicked.connect(shift_basic)
        button_contains.clicked.connect(shift_contains)
        button_diet.clicked.connect(shift_diet)
        button_disease.clicked.connect(shift_disease)
        button_description.clicked.connect(shift_description)

        layout.addLayout(layout1, stretch = 1)       #space taken by content and tab bar
        layout.addLayout(layout2, stretch = 7)

        widget = qtw.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = qtw.QApplication([])
window = MainWindow()
window.show()
app.exec()
