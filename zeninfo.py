import PyQt6.QtWidgets as qtw

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
        layoutb = qtw.QGridLayout()
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

        layoutb.addWidget(qtw.QLabel('contains'), 4, 4)
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
