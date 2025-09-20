import PyQt6.QtWidgets as qtw

class SearchResults(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Page")

        main_layout = qtw.QVBoxLayout()

        # --- Search bar ---
        search_layout = qtw.QHBoxLayout()
        self.search_input = qtw.QLineEdit()
        self.search_input.setPlaceholderText("Search by Nutrient or Ingredient...")
        search_button = qtw.QPushButton("Search")
        search_button.clicked.connect(self.show_results)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        main_layout.addLayout(search_layout)

        # --- Fake filters (checkboxes just for show) ---
        filters_group = qtw.QGroupBox("Filters")
        filters_layout = qtw.QHBoxLayout()
        filters_layout.addWidget(qtw.QCheckBox("Veg"))
        filters_layout.addWidget(qtw.QCheckBox("Non-Veg"))
        filters_layout.addWidget(qtw.QCheckBox("Egg"))
        filters_layout.addWidget(qtw.QCheckBox("Low Calorie"))
        filters_layout.addWidget(qtw.QCheckBox("Morning Snack"))
        filters_group.setLayout(filters_layout)
        main_layout.addWidget(filters_group)

        # --- Results section ---
        self.results_label = qtw.QLabel("Results will appear here...")
        self.results_list = qtw.QListWidget()
        main_layout.addWidget(self.results_label)
        main_layout.addWidget(self.results_list)

        # finalize
        container = qtw.QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def show_results(self):
        query = self.search_input.text().strip().lower()
        self.results_list.clear()

        if query == "vitamin c":
            self.results_label.setText("🔍 Results for Nutrient: Vitamin C")
            self.results_list.addItems([
                "Apple (Rich in Vitamin C)",
                "Orange (High Vitamin C content)"
            ])
        elif query == "apple":
            self.results_label.setText("🔍 Results for Ingredient: Apple")
            self.results_list.addItems([
                "Apple Pie (contains Apple Flesh)",
                "Fruit Salad (contains Apple Flesh)"
            ])
        else:
            self.results_label.setText("No results found.")


app = qtw.QApplication([])
window = SearchResults()
window.show()
app.exec()

