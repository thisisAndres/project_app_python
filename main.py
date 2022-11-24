from PyQt6 import QtWidgets, uic
import os
import sys
from FrmCotizacion import *

import traceback
from EntidadesModulo import Persona
from PyQt6 import QtWidgets


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

class FrmCotizacion(QtWidgets.QDialog):
        def __init__(self):
            super(FrmCotizacion,self).__init__()
            super().__init__()
            self.ui = Ui_Form()
            self.objPersona = None
            self.fila = 0
            self.ui.setupUi(self)
            self.inicializarControles()
            self.ui.BtnGenerar.clicked.connect(self.generarCotizacion)
            self.ui.BtnEliminar.clicked.connect(self.eliminarCotizacion)
            self.ui.BtnModificar.clicked.connect(self.modificarCotizacion)
            self.ui.BtnEliminar.setDisabled(True)
            self.ui.BtnModificar.setDisabled(True)
            self.ui.TblInformacion.selectionModel().currentRowChanged.connect(self.onSelectionChanged)

        def generarCotizacion(self):
            cedula = self.ui.txtCedula.text()
            nombre = self.ui.txtNombre.text()
            genero = self.ui.comboBoxGenero.currentText()
            sector = self.ui.comboBoxSector.currentText()
            tipoCredito = self.ui.comboBoxTipoCredito.currentText()
            monto = self.ui.txtMonto.text()
            tasa = self.ui.txtTasa.text()
            plazo = self.ui.comboBoxPlazo.currentText()

           
            self.objPersona = Persona(cedula,nombre,genero,sector,tipoCredito,monto,tasa,plazo)
            self.ui.TblInformacion.insertRow(self.fila)
            celdaCedula = QtWidgets.QTableWidgetItem(self.objPersona.cedula)
            celdaNombre = QtWidgets.QTableWidgetItem(self.objPersona.nombre)
            celdaGenero = QtWidgets.QTableWidgetItem(self.objPersona.genero)
            celdaSector = QtWidgets.QTableWidgetItem(self.objPersona.sector)
            celdaCredito = QtWidgets.QTableWidgetItem(self.objPersona.tipoCredito)
            celdaMonto = QtWidgets.QTableWidgetItem(self.objPersona.monto)
            celdaTasa = QtWidgets.QTableWidgetItem(self.objPersona.tasa)
            celdaPlazo = QtWidgets.QTableWidgetItem(self.objPersona.plazo)

            
            self.ui.TblInformacion.setItem(self.fila, 0, celdaCedula)
            self.ui.TblInformacion.setItem(self.fila, 1, celdaNombre)
            self.ui.TblInformacion.setItem(self.fila, 2, celdaGenero)
            self.ui.TblInformacion.setItem(self.fila, 3, celdaSector)
            self.ui.TblInformacion.setItem(self.fila, 4, celdaCredito)
            self.ui.TblInformacion.setItem(self.fila, 5, celdaMonto)
            self.ui.TblInformacion.setItem(self.fila, 6, celdaTasa)
            self.ui.TblInformacion.setItem(self.fila, 7, celdaPlazo)


            self.fila += 1
            self.inicializarControles()

        def eliminarCotizacion(self):
            indiceAEliminar = self.ui.TblInformacion.currentRow()
            self.ui.TblInformacion.removeRow(indiceAEliminar)
            self.fila -= 1
            self.ui.TblInformacion.selectionModel().clearCurrentIndex()

        def modificarCotizacion(self):
            indiceAEditar = self.ui.TblInformacion.currentRow()
            cedula = self.ui.txtCedula.text()
            nombre = self.ui.txtNombre.text()
            genero = self.ui.comboBoxGenero.currentText()
            sector = self.ui.comboBoxSector.currentText()
            tipoCredito = self.ui.comboBoxTipoCredito.currentText()
            monto = self.ui.txtMonto.text()
            tasa = self.ui.txtTasa.text()
            plazo = self.ui.comboBoxPlazo.currentText()
            
            genero = self.ui.comboBoxGenero.currentText()
            self.objPersona = Persona(cedula,nombre,genero,sector,tipoCredito,monto,tasa,plazo)
            celdaCedula = QtWidgets.QTableWidgetItem(self.objPersona.cedula)
            celdaNombre = QtWidgets.QTableWidgetItem(self.objPersona.nombre)
            celdaGenero = QtWidgets.QTableWidgetItem(self.objPersona.genero)
            celdaSector = QtWidgets.QTableWidgetItem(self.objPersona.sector)
            celdaCredito = QtWidgets.QTableWidgetItem(self.objPersona.tipoCredito)
            celdaMonto = QtWidgets.QTableWidgetItem(self.objPersona.monto)
            celdaTasa = QtWidgets.QTableWidgetItem(self.objPersona.tasa)
            celdaPlazo = QtWidgets.QTableWidgetItem(self.objPersona.plazo)

            
            self.ui.TblInformacion.setItem(indiceAEditar,0,celdaCedula)
            self.ui.TblInformacion.setItem(indiceAEditar,1,celdaNombre)
            self.ui.TblInformacion.setItem(indiceAEditar,2,celdaGenero)
            self.ui.TblInformacion.setItem(indiceAEditar,3,celdaSector)
            self.ui.TblInformacion.setItem(indiceAEditar,4,celdaCredito)
            self.ui.TblInformacion.setItem(indiceAEditar,5,celdaMonto)
            self.ui.TblInformacion.setItem(indiceAEditar,6,celdaTasa)
            self.ui.TblInformacion.setItem(indiceAEditar,7,celdaPlazo)

            self.inicializarControles()
            self.ui.TblInformacion.selectionModel().clearCurrentIndex()      


        def onSelectionChanged(self, selected):
            if (selected.row() != -1):
                self.ui.BtnEliminar.setEnabled(True)
                self.ui.BtnModificar.setEnabled(True)
            else:
                self.ui.BtnEliminar.setDisabled(True)
                self.ui.BtnModificar.setDisabled(True)

        def inicializarControles(self):
            self.ui.txtCedula.clear()
            self.ui.txtNombre.clear()
            self.ui.txtMonto.clear()
            self.ui.txtTasa.clear()

            self.ui.comboBoxGenero.setCurrentIndex(0)
            self.ui.comboBoxSector.setCurrentIndex(2)
            self.ui.comboBoxTipoCredito.setCurrentIndex(2)
            self.ui.comboBoxPlazo.setCurrentIndex(2)

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = FrmCotizacion()
        myapp.show()
        sys.exit(app.exec())

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
