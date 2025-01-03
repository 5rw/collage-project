import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets, QtGui, QtCore
import sys 
from quantcrypt.dss import Dilithium 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time 
 
 
class MyApp(QtWidgets.QMainWindow): 
    def init(self, parent=None): 
        super().init(parent) 
        self.setupUi(self) 
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 960)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #2e2e2e;  /* Slightly dark gray */\n"
"    color: #ffffff;  /* Default text color */\n"
"    font: 12px \"Arial\";  /* Default font */\n"
"}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(20, 20, 1325, 91)
        self.textEdit.setPlaceholderText("Type Here to Encrypt ...")
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    background-color: #d6d6d6;  /* Slightly white background */\n"
"    color: #333333;  /* Dark gray text for contrast */\n"
"    border: 2px solid #cccccc;  /* Light gray border */\n"
"    border-radius: 8px;  /* Rounded corners */\n"
"    padding: 8px;  /* Internal padding for text */\n"
"    font: 12px \"Arial\";  /* Font style */\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 2px solid #bbbbbb;  /* Slightly darker border on hover */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #aaaaaa;  /* Highlighted border on focus */\n"
"    background-color: #ffffff;  /* Brighter background on focus */\n"
"}")

        self.pushButton = QtWidgets.QPushButton("Encrypt and Verify", self.centralwidget)
        self.pushButton.setGeometry(20, 130, 211, 51)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #a9e1ff;  /* Slightly white background */\n"
"    color: #333333;  /* Dark gray text for contrast */\n"
"    border: 2px solid #cccccc;  /* Light gray border */\n"
"    border-radius: 8px;  /* Rounded corners */\n"
"    padding: 8px 16px;  /* Button padding */\n"
"    font: bold 12px \"Arial\";  /* Font style */\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eaeaea;  /* Slightly darker background on hover */\n"
"    border: 2px solid #bbbbbb;  /* Slightly darker border on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dddddd;  /* Even darker background on press */\n"
"    border: 2px solid #aaaaaa;  /* Darker border on press */\n"
"}")

        self.encryptiontable = QtWidgets.QTableView(self.centralwidget)
        self.encryptiontable.setGeometry(20, 360, 391, 321)
        self.encryptiontable.setStyleSheet("QTableView {\n"
"    background-color: #f7f7f7;  /* Slightly white background */\n"
"    color: #333333;  /* Dark gray text for contrast */\n"
"    border: 2px solid #cccccc;  /* Light gray border */\n"
"    border-radius: 8px;  /* Rounded corners */\n"
"    gridline-color: #dddddd;  /* Light gray grid lines */\n"
"    font: 12px \"Arial\";  /* Font style */\n"
"    selection-background-color: #eaeaea;  /* Light gray selection background */\n"
"    selection-color: #000000;  /* Black text for selected items */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #eeeeee;  /* Light gray header background */\n"
"    color: #333333;  /* Dark gray header text */\n"
"    border: 1px solid #cccccc;  /* Light gray border for headers */\n"
"    padding: 4px;  /* Padding for header text */\n"
"    font: bold 12px \"Arial\";  /* Font style for headers */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #eeeeee;  /* Light gray corner button */\n"
"    border: 1px solid #cccccc;  /* Border for corner button */\n"
"}")

        self.viewtable = QtWidgets.QTableView(self.centralwidget)
        self.viewtable.setGeometry(20, 200, 391, 141)
        self.viewtable.setStyleSheet("QTableView {\n"
"    background-color: #f7f7f7;  /* Slightly white background */\n"
"    color: #333333;  /* Dark gray text for contrast */\n"
"    border: 2px solid #cccccc;  /* Light gray border */\n"
"    border-radius: 8px;  /* Rounded corners */\n"
"    gridline-color: #dddddd;  /* Light gray grid lines */\n"
"    font: 12px \"Arial\";  /* Font style */\n"
"    selection-background-color: #eaeaea;  /* Light gray selection background */\n"
"    selection-color: #000000;  /* Black text for selected items */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #eeeeee;  /* Light gray header background */\n"
"    color: #333333;  /* Dark gray header text */\n"
"    border: 1px solid #cccccc;  /* Light gray border for headers */\n"
"    padding: 4px;  /* Padding for header text */\n"
"    font: bold 12px \"Arial\";  /* Font style for headers */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #eeeeee;  /* Light gray corner button */\n"
"    border: 1px solid #cccccc;  /* Border for corner button */\n"
"}")

        self.drawtable = QtWidgets.QWidget(self.centralwidget)
        self.drawtable.setGeometry(430, 200, 915, 481)
        self.drawtable.setStyleSheet("QTableView {\n"
"    background-color: #f7f7f7;  /* Slightly white background */\n"
"    color: #333333;  /* Dark gray text for contrast */\n"
"    border: 2px solid #cccccc;  /* Light gray border */\n"
"    border-radius: 8px;  /* Rounded corners */\n"
"    gridline-color: #dddddd;  /* Light gray grid lines */\n"
"    font: 12px \"Arial\";  /* Font style */\n"
"    selection-background-color: #eaeaea;  /* Light gray selection background */\n"
"    selection-color: #000000;  /* Black text for selected items */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #eeeeee;  /* Light gray header background */\n"
"    color: #333333;  /* Dark gray header text */\n"
"    border: 1px solid #cccccc;  /* Light gray border for headers */\n"
"    padding: 4px;  /* Padding for header text */\n"
"    font: bold 12px \"Arial\";  /* Font style for headers */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #eeeeee;  /* Light gray corner button */\n"
"    border: 1px solid #cccccc;  /* Border for corner button */\n"
"}")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        layout = QtWidgets.QVBoxLayout(self.drawtable)
        layout.addWidget(self.canvas)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Lattice-Based Algorithm")
 
        self.pushButton.clicked.connect(self.process_encryption) 
 

    def process_encryption(self): 
        message = self.textEdit.toPlainText().encode("utf-8") 
        dss = Dilithium() 
        public_key, private_key = dss.keygen() 

        start_time = time.time() 
        signature = dss.sign(private_key, message) 
        sign_time = time.time() - start_time 

        start_verify = time.time() 
        valid = dss.verify(public_key, message, signature) 
        verify_time = time.time() - start_verify 

        message_size = len(message) 

        self.ax.clear() 
        self.ax.bar(["Sign Time", "Verify Time"], [sign_time, verify_time], color=['red', 'purple'])  # Aggressive colors
        self.ax.set_title(f"Message Size: {message_size} bytes") 
        self.canvas.draw() 

        # Metric and Value Table
        model = QtGui.QStandardItemModel() 
        model.setHorizontalHeaderLabels(["Metric", "Value"]) 
        model.appendRow([QtGui.QStandardItem("Sign Time"), QtGui.QStandardItem(f"{sign_time:.6f} s")]) 
        model.appendRow([QtGui.QStandardItem("Verify Time"), QtGui.QStandardItem(f"{verify_time:.6f} s")]) 
        model.appendRow([QtGui.QStandardItem("Message Size"), QtGui.QStandardItem(f"{message_size} bytes")]) 
        model.appendRow([QtGui.QStandardItem("Signature Validation"), QtGui.QStandardItem("Valid" if valid else "Invalid")]) 
        self.viewtable.setModel(model) 

        header = self.viewtable.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #004080;  /* Dark blue background */
                color: #ffffff;  /* White text */
                font: bold 14px "Arial";
                border: 1px solid #66b3ff;
                padding: 4px;
            }
        """)

        # Key Type and Key Value Table
        view_model = QtGui.QStandardItemModel() 
        view_model.setHorizontalHeaderLabels(["Key Type", "Key Value"]) 
        view_model.appendRow([QtGui.QStandardItem("Public Key"), QtGui.QStandardItem(str(public_key))]) 
        view_model.appendRow([QtGui.QStandardItem("Private Key"), QtGui.QStandardItem(str(private_key))]) 
        view_model.appendRow([QtGui.QStandardItem("Signature"), QtGui.QStandardItem(str(signature))]) 
        self.encryptiontable.setModel(view_model) 

        # Adjust table header and layout
        self.viewtable.horizontalHeader().setStretchLastSection(True)
        self.viewtable.verticalHeader().setVisible(False)  # Hide vertical header indices
        self.viewtable.setContentsMargins(0, 0, 0, 0)  # Remove extra padding
        self.viewtable.resizeColumnsToContents()
        self.viewtable.resizeRowsToContents()
        self.viewtable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.viewtable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.encryptiontable.horizontalHeader().setStretchLastSection(True)
        self.encryptiontable.verticalHeader().setVisible(False)  # Hide vertical header indices
        self.encryptiontable.setContentsMargins(0, 0, 0, 0)  # Remove extra padding
        self.encryptiontable.resizeColumnsToContents()
        self.encryptiontable.resizeRowsToContents()
        self.encryptiontable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.encryptiontable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        header = self.encryptiontable.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #800000;  /* Dark red background */
                color: #ffffff;  /* White text */
                font: bold 14px "Arial";
                border: 1px solid #ff6666;
                padding: 4px;
            }
        """)
        start_time = time.time() 
        signature = dss.sign(private_key, message) 
        sign_time = time.time() - start_time 
 
        start_verify = time.time() 
        valid = dss.verify(public_key, message, signature) 
        verify_time = time.time() - start_verify 
 
        message_size = len(message) 
 
        self.ax.clear() 
        self.ax.bar(["Sign Time", "Verify Time"], [sign_time, verify_time], color=['blue', 'green']) 
        self.ax.set_title(f"Message Size: {message_size} bytes") 
        self.canvas.draw() 
 
        model = QtGui.QStandardItemModel() 
        model.setHorizontalHeaderLabels(["Metric", "Value"]) 
        model.appendRow([QtGui.QStandardItem("Sign Time"), QtGui.QStandardItem(f"{sign_time:.6f} s")]) 
        model.appendRow([QtGui.QStandardItem("Verify Time"), QtGui.QStandardItem(f"{verify_time:.6f} s")]) 
        model.appendRow([QtGui.QStandardItem("Message Size"), QtGui.QStandardItem(f"{message_size} bytes")]) 
        model.appendRow([QtGui.QStandardItem("Signature Validation"), QtGui.QStandardItem("Valid" if valid else "Invalid")]) 
        self.viewtable.setModel(model) 
 
        view_model = QtGui.QStandardItemModel() 
        view_model.setHorizontalHeaderLabels(["Key Type", "Key Value"]) 
        view_model.appendRow([QtGui.QStandardItem("Public Key"), QtGui.QStandardItem(str(public_key))]) 
        view_model.appendRow([QtGui.QStandardItem("Private Key"), QtGui.QStandardItem(str(private_key))]) 
        view_model.appendRow([QtGui.QStandardItem("Signature"), QtGui.QStandardItem(str(signature))]) 
        self.encryptiontable.setModel(view_model) 
 
 
def main(): 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow() 
    ui = MyApp() 
    ui.setupUi(MainWindow) 
    MainWindow.show() 
    sys.exit(app.exec_()) 
 
 
if __name__ == "__main__": 
    main()
