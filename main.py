from PyQt6 import QtWidgets, uic
import os
import sys
import traceback


class main(QtWidgets.QDialog):
    def __init__(self):
        super(main, self).__init__()
        self.rutaFileUI = os.path.dirname(os.path.abspath(__file__))
        self.ruta = os.path.join(self.rutaFileUI, "FrmCotizacion.ui")
        uic.load_ui.loadUi(self.ruta, self)
        self.show()

        # setear los controles para escribir
        # info cliente
        self.txtCedula = self.findChild(
            QtWidgets.QLineEdit, "txtCedula"
        )
        self.txtNombre = self.findChild(
            QtWidgets.QLineEdit, "txtNombre"
        )
        self.comboBoxGenero = self.findChild(
            QtWidgets.QComboBox, "comboBoxGenero"
        )
        self.comboBoxSector = self.findChild(
            QtWidgets.QComboBox, "comboBoxSector"
        )
        # info cotizacion
        self.comboBoxTipoCredito = self.findChild(
            QtWidgets.QComboBox, "comboBoxTipoCredito"
        )
        self.txtMonto = self.findChild(
            QtWidgets.QLineEdit, "txtMonto"
        )
        self.txtTasa = self.findChild(
            QtWidgets.QLineEdit, "txtTasa"
        )
        self.comboBoxPlazo = self.findChild(
            QtWidgets.QComboBox, "comboBoxPlazo"
        )

        # setear boton para generar cotizacion
        self.btnGenerar = self.findChild(
            QtWidgets.QPushButton, "btnGenerar"
        )
        self.btnGenerar.clicked.connect(self.escribirArchivo)

        # Setear checkbox
        self.checkBoxCargos = self.findChild(
            QtWidgets.QCheckBox, "checkBoxCargos"
        )

        # controlador de columnas y set de tablewidget
        self.fila = 0
        self.tableWidget = self.findChild(
            QtWidgets.QTableWidget, "tableWidget"
        )

    def escribirArchivo(self):
        try:

            infoClienteCredito = (
                "--------------------> INFORMACION DE CLIENTE <-----------------------\n" +
                "\n" +
                f"[Nombre: {self.txtNombre.text()}] || [Cedula: {self.txtCedula.text()}] || [Genero: {self.comboBoxGenero.currentText()}] || [Sector: {self.comboBoxSector.currentText()}]\n" +
                "\n" +
                "--------------------> INFORMACION DE CREDITO <-----------------------\n" +
                "\n" +
                f"[Tipo de credito: {self.comboBoxTipoCredito.currentText()}] || [Monto del credito: {self.txtMonto.text()}] || [Interes: {self.txtTasa.text()}%] || [Plazo: {self.comboBoxPlazo.currentText()} meses]\n" +
                "\n" +
                "--------------->     TABLA DE PAGOS 	<-----------------------\n" +
                "Numero de cuota || Saldo pendiente || Intereses por mes || monto de cuota\n"
            )

            nombre = os.path.join(
                self.rutaFileUI, f"Cotizacion_{self.txtNombre.text()}")
            archivo = open(nombre, "a")
            archivo.write(infoClienteCredito)
            archivo.close()

            # Escribir en la tabla
            self.escribirTabla()

            # llamando a la funcion para generar la tabla de pagos
            self.generarTablaPagos()

            # Seteando contoles a sus valores orignales
            self.inicializarControles()

        except OSError as err:
            print(err.strerror)
            archivo.close()
        except BaseException:
            archivo.close()
            print(traceback.format_exc())

    def generarTablaPagos(self):

        numeroDePago = 1
        p = int(self.txtMonto.text())
        i = int(self.txtTasa.text())/100
        m = int(self.comboBoxPlazo.currentText())
        cargosAdicionales = 0

        if self.checkBoxCargos.isChecked() == True:
            cargosAdicionales = 500

        p = p + cargosAdicionales

        # calculo de la cuota
        c = (p + (p*i)) / m

        totPagar = p+(p*i)
        iPorcuota = p * i

        # Abrir archivo
        nombre = os.path.join(
            self.rutaFileUI, f"Cotizacion_{self.txtNombre.text()}")
        archivo = open(nombre, "a")

        while (numeroDePago <= m):

            informacion = f"{format(numeroDePago, '0,.0f')}    ||    {format(totPagar, '0,.0f')}    ||    {format(iPorcuota,'0,.0f')}    ||    {format(c, '0,.0f')}\n"
            archivo.write(
                informacion
            )
            iPorcuota = totPagar*i
            numeroDePago = numeroDePago + 1
            totPagar = totPagar - c

        archivo.close()

    def escribirTabla(self):
        cedula = QtWidgets.QTableWidgetItem(self.txtCedula.text())
        nombre = QtWidgets.QTableWidgetItem(self.txtNombre.text())
        monto = QtWidgets.QTableWidgetItem(self.txtMonto.text())
        tasa = QtWidgets.QTableWidgetItem(self.txtTasa.text())
        genero = QtWidgets.QTableWidgetItem(self.comboBoxGenero.currentText())
        plazo = QtWidgets.QTableWidgetItem(self.comboBoxPlazo.currentText())
        sector = QtWidgets.QTableWidgetItem(self.comboBoxSector.currentText())
        tipoCredito = QtWidgets.QTableWidgetItem(
            self.comboBoxTipoCredito.currentText())

        # generar el texto
        self.tableWidget.insertRow(self.fila)
        self.tableWidget.setItem(self.fila, 0, cedula)
        self.tableWidget.setItem(self.fila, 1, nombre)
        self.tableWidget.setItem(self.fila, 2, genero)
        self.tableWidget.setItem(self.fila, 3, sector)
        self.tableWidget.setItem(self.fila, 4, tipoCredito)
        self.tableWidget.setItem(self.fila, 5, monto)
        self.tableWidget.setItem(self.fila, 6, tasa)
        self.tableWidget.setItem(self.fila, 7, plazo)

        self.fila += 1

    def inicializarControles(self):

        self.txtCedula.clear()
        self.txtMonto.clear()
        self.txtNombre.clear()
        self.txtTasa.clear()
        self.comboBoxGenero.setCurrentIndex(0)
        self.comboBoxPlazo.setCurrentIndex(0)
        self.comboBoxSector.setCurrentIndex(0)
        self.comboBoxTipoCredito.setCurrentIndex(0)


app = QtWidgets.QApplication(sys.argv)
gestor = main()
sys.exit(app.exec())
