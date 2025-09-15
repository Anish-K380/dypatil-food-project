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
        layouta = qtw.QGridLayout()
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

        layouta.addWidget(qtw.QLabel('basic'), 4, 4)
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
