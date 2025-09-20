import PyQt6.QtWidgets as qtw

class FoodDetails(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Details")

        layout = qtw.QVBoxLayout()

        # Example 1: Apple
        apple_group = qtw.QGroupBox("🍎 Apple")
        apple_layout = qtw.QFormLayout()
        apple_layout.addRow("Food Type:", qtw.QLabel("Veg"))
        apple_layout.addRow("Calories:", qtw.QLabel("52 kcal / 100g"))
        apple_layout.addRow("Best For:", qtw.QLabel("Morning, Snacks"))
        apple_layout.addRow("Contains:", qtw.QLabel("Vitamin C, Fiber, Natural Sugar"))
        apple_layout.addRow("Suitable For:", qtw.QLabel("✅ Heart, ❌ Diabetes"))
        apple_layout.addRow("Description:", qtw.QLabel("A sweet, crunchy fruit rich in fiber and Vitamin C."))
        apple_group.setLayout(apple_layout)
        layout.addWidget(apple_group)

        # Example 2: Carrot
        carrot_group = qtw.QGroupBox("🥕 Carrot")
        carrot_layout = qtw.QFormLayout()
        carrot_layout.addRow("Food Type:", qtw.QLabel("Veg"))
        carrot_layout.addRow("Calories:", qtw.QLabel("41 kcal / 100g"))
        carrot_layout.addRow("Best For:", qtw.QLabel("Lunch, Evening Snack"))
        carrot_layout.addRow("Contains:", qtw.QLabel("Beta-Carotene, Fiber"))
        carrot_layout.addRow("Suitable For:", qtw.QLabel("✅ Eyesight, ✅ Heart"))
        carrot_layout.addRow("Description:", qtw.QLabel("A root vegetable high in beta-carotene, good for eyesight."))
        carrot_group.setLayout(carrot_layout)
        layout.addWidget(carrot_group)

        # finalize
        container = qtw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = qtw.QApplication([])
window = FoodDetails()
window.show()
app.exec()

