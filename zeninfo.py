import PyQt6.QtWidgets as qtw

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
                nutrients[self.nutrient_id] = self.last_nutrient
                nutrient_group.addButton(self.last_nutrient.button, self.nutrient_id)
                self.nutrient_id += 1
        def delete_nutrient(button):
            if self.last_nutrient.left == None:return None
            nutrient = nutrients[nutrient_group.id(button)]
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
        layoutc = qtw.QGridLayout()
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
        self.nutrient_id = 1
        self.last_nutrient.val.returnPressed.connect(create_new_nutrient)
        nutrients = dict()
        nutrients[0] = self.last_nutrient
        nutrient_group = qtw.QButtonGroup()
        nutrient_group.addButton(self.last_nutrient.button)
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
        layoutb.addLayout(nutrient_half)
        
        layoutc.addWidget(qtw.QLabel('diet'), 4, 4)
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
