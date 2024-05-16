from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Componentes para agregar doctor...
        self.lbl_agregar_doctor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_agregar_doctor.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.lbl_agregar_doctor.setObjectName("lbl_agregar_doctor")
        self.lbl_nombre_doctor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nombre_doctor.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.lbl_nombre_doctor.setObjectName("lbl_nombre_doctor")
        self.txt_nombre_doctor = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nombre_doctor.setGeometry(QtCore.QRect(80, 50, 141, 20))
        self.txt_nombre_doctor.setObjectName("txt_nombre_doctor")
        self.lbl_dni_doctor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_dni_doctor.setGeometry(QtCore.QRect(20, 80, 51, 16))
        self.lbl_dni_doctor.setObjectName("lbl_dni_doctor")
        self.txt_dni_doctor = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_dni_doctor.setGeometry(QtCore.QRect(80, 80, 141, 20))
        self.txt_dni_doctor.setObjectName("txt_dni_doctor")
        self.lbl_especialidad_doctor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_especialidad_doctor.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.lbl_especialidad_doctor.setObjectName("lbl_especialidad_doctor")
        self.txt_especialidad_doctor = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_especialidad_doctor.setGeometry(QtCore.QRect(80, 110, 141, 20))
        self.txt_especialidad_doctor.setObjectName("txt_especialidad_doctor")
        self.btn_agregar_doctor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_agregar_doctor.setGeometry(QtCore.QRect(80, 140, 141, 23))
        self.btn_agregar_doctor.setObjectName("btn_agregar_doctor")

        # Componentes para buscar doctor
        self.lbl_buscar_doctor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_buscar_doctor.setGeometry(QtCore.QRect(300, 20, 121, 16))
        self.lbl_buscar_doctor.setObjectName("lbl_buscar_doctor")
        self.txt_buscar_doctor = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_buscar_doctor.setGeometry(QtCore.QRect(430, 20, 141, 20))
        self.txt_buscar_doctor.setObjectName("txt_buscar_doctor")
        self.btn_buscar_doctor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar_doctor.setGeometry(QtCore.QRect(430, 50, 141, 23))
        self.btn_buscar_doctor.setObjectName("btn_buscar_doctor")

        # Tabla para mostrar resultados de doctores
        self.tabla_doctores = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_doctores.setGeometry(QtCore.QRect(20, 200, 761, 351))
        self.tabla_doctores.setColumnCount(4)
        self.tabla_doctores.setRowCount(0)
        self.tabla_doctores.setHorizontalHeaderLabels(["Nombre", "DNI", "Especialidad", "Hospital"])
        self.tabla_doctores.setObjectName("tabla_doctores")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Conectar acciones con funciones
        self.btn_agregar_doctor.clicked.connect(self.agregar_doctor)
        self.btn_buscar_doctor.clicked.connect(self.buscar_doctor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Información Hospitalaria"))
        self.lbl_agregar_doctor.setText(_translate("MainWindow", "Agregar Doctor"))
        self.lbl_nombre_doctor.setText(_translate("MainWindow", "Nombre:"))
        self.lbl_dni_doctor.setText(_translate("MainWindow", "DNI:"))
        self.lbl_especialidad_doctor.setText(_translate("MainWindow", "Especialidad:"))
        self.btn_agregar_doctor.setText(_translate("MainWindow", "Agregar Doctor"))
        self.lbl_buscar_doctor.setText(_translate("MainWindow", "Buscar Doctor por DNI:"))
        self.btn_buscar_doctor.setText(_translate("MainWindow", "Buscar Doctor"))

    def agregar_doctor(self):
        # Lógica para agregar un doctor
        nombre = self.txt_nombre_doctor.text()
        dni = self.txt_dni_doctor.text()
        especialidad = self.txt_especialidad_doctor.text()
        # Llamar a la función que agrega el doctor con los datos ingresados
        pass

    def buscar_doctor(self):
        # Lógica para buscar un doctor
        dni = self.txt_buscar_doctor.text()
        # Llamar a la función que busca el doctor con el DNI ingresado
        pass

    def actualizar_tabla_doctores(self, lista_doctores):
        self.tabla_doctores.setRowCount(len(lista_doctores))
        for i, doctor in enumerate(lista_doctores):
            self.tabla_doctores.setItem(i, 0, QtWidgets.QTableWidgetItem(doctor.nombre))
            self.tabla_doctores.setItem(i, 1, QtWidgets.QTableWidgetItem(doctor.dni))
            self.tabla_doctores.setItem(i, 2, QtWidgets.QTableWidgetItem(doctor.especialidad))
            self.tabla_doctores.setItem(i, 3, QtWidgets.QTableWidgetItem(str(doctor.id_hospital)))

    def actualizar_tabla_hospitales(self, lista_hospitales):
        self.tabla_hospitales.setRowCount(len(lista_hospitales))
        for i, hospital in enumerate(lista_hospitales):
            self.tabla_hospitales.setItem(i, 0, QtWidgets.QTableWidgetItem(hospital.nombre))
            self.tabla_hospitales.setItem(i, 1, QtWidgets.QTableWidgetItem(str(hospital.id)))


# Código para ejecutar la aplicación
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
