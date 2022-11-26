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

    def escribirArchivo(self):
        try:

            infoClienteCredito = (
                "--------------------> INFORMACION DE CLIENTE <-----------------------\n" +
                "\n" +
                f"[{self.txtNombre.text()}] || [{self.txtCedula.text()}] || [{self.comboBoxGenero.currentText()}] || [{self.comboBoxSector.currentText()}]\n" +
                "\n" +
                "--------------------> INFORMACION DE CREDITO <-----------------------\n" +
                "\n" +
                f"[{self.comboBoxTipoCredito.currentText()}] || [{self.txtMonto.text()}] || [{self.txtTasa.text()}] || [{self.comboBoxPlazo.currentText()}]\n" +
                "\n" +
                "--------------->     TABLA DE PAGOS 	<-----------------------\n"
            )

            nombre = os.path.join(
                self.rutaFileUI, f"Cotizacion_{self.txtNombre.text()}")
            archivo = open(nombre, "a")
            archivo.write(infoClienteCredito)
            archivo.close()
            # Seteando contoles a sus valores orignales
            self.inicializarControles()

        except OSError as err:
            print(err.strerror)
            archivo.close()
        except BaseException:
            archivo.close()
            print(traceback.format_exc())

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
