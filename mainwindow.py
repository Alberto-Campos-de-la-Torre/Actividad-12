from PySide2.QtWidgets import QMainWindow, QFileDialog,QMessageBox,QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particulas
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  

        self.particulas = Particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.finalcap.clicked.connect(self.click_agregarfinal)
        self.ui.Iniciocap.clicked.connect(self.click_agregarinicio)      
        self.ui.Mostrar.clicked.connect(self.click_mostrar)
        self.ui.OrigenX.valueChanged.connect(self.setValue)
        self.ui.OrigenY.valueChanged.connect(self.setValue)
        self.ui.DestinoX.valueChanged.connect(self.setValue)
        self.ui.DestinoY.valueChanged.connect(self.setValue)
        self.ui.Verde.valueChanged.connect(self.setValue)
        self.ui.Rojo.valueChanged.connect(self.setValue)
        self.ui.Azul.valueChanged.connect(self.setValue)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.Mostrartabla_push.clicked.connect(self.Mostrar_tabla)
        self.ui.Buscar_push.clicked.connect(self.buscar_id)
        
    @Slot()
    def Mostrar_tabla(self):
        self.ui.Tabla.setColumnCount(10)
        headers = ["Id", "origen_x", "origen_y", "destino_x", "destino_y", "velocidad","rojo", "verde","azul", "distancia"]
        self.ui.Tabla.setHorizontalHeaderLabels(headers)

        self.ui.Tabla.setRowCount(len(self.particulas))

        row = 0
        for particula in self.particulas:
            Id_widget = QTableWidgetItem(str(particula.Id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula. origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))           
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            rojo_widget = QTableWidgetItem(str(particula.rojo))
            verde_widget = QTableWidgetItem(str(particula.Id))
            azul_widget = QTableWidgetItem(str(particula.azul))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.Tabla.setItem(row, 0,  Id_widget)
            self.ui.Tabla.setItem(row, 1,  origen_x_widget)
            self.ui.Tabla.setItem(row, 2,  origen_y_widget)
            self.ui.Tabla.setItem(row, 3,  destino_x_widget)
            self.ui.Tabla.setItem(row, 4,  destino_y_widget)
            self.ui.Tabla.setItem(row, 5,  velocidad_widget)
            self.ui.Tabla.setItem(row, 6,  rojo_widget)
            self.ui.Tabla.setItem(row, 7,  verde_widget)
            self.ui.Tabla.setItem(row, 8,  azul_widget)
            self.ui.Tabla.setItem(row, 9,  distancia_widget)

            row += 1
            
    @Slot()
    def buscar_id(self):

        headers = ["Id", "origen_x", "origen_y", "destino_x", "destino_y", "velocidad","rojo", "verde","azul", "distancia"]
        Id = self.ui.LineadeBusqueda.text()
        
        encontrado = False

        for particula in self.particulas:
            if Id == str(particula.Id):
                self.ui.Tabla.clear()
                self.ui.Tabla.setRowCount(1)
                self.ui.Tabla.setColumnCount(10)
                self.ui.Tabla.setHorizontalHeaderLabels(headers)
                
                Id_widget = QTableWidgetItem(str(particula.Id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula. origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))           
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                rojo_widget = QTableWidgetItem(str(particula.rojo))
                verde_widget = QTableWidgetItem(str(particula.Id))
                azul_widget = QTableWidgetItem(str(particula.azul))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.Tabla.setItem(0, 0,  Id_widget)
                self.ui.Tabla.setItem(0, 1,  origen_x_widget)
                self.ui.Tabla.setItem(0, 2,  origen_y_widget)
                self.ui.Tabla.setItem(0, 3,  destino_x_widget)
                self.ui.Tabla.setItem(0, 4,  destino_y_widget)
                self.ui.Tabla.setItem(0, 5,  velocidad_widget)
                self.ui.Tabla.setItem(0, 6,  rojo_widget)
                self.ui.Tabla.setItem(0, 7,  verde_widget)
                self.ui.Tabla.setItem(0, 8,  azul_widget)
                self.ui.Tabla.setItem(0, 9,  distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'El libro con el titulo "{Id}" no fue encontrado'
            )


    @Slot()
    def action_abrir_archivo(self):
       # print('Abrir Archivo')
        ubicacion = QFileDialog.getOpenFileName(
           self,
           'Abrir Archivo',
           '.',
           'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('Guardar Archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
               self,
               "Error",
               "No se pudo crear el archivo " + ubicacion
            )
     
    @Slot()
    def click_agregarfinal(self):
        Id = self.ui.ID.value()
        Ox = self.ui.OrigenX.value()   
        Oy = self.ui.OrigenY.value() 
        Dx = self.ui.DestinoX.value()
        Dy = self.ui.DestinoY.value()
        Vel = self.ui.Velocidad.value()
        Red = self.ui.Rojo.value()
        Blue = self.ui.Azul.value()
        Green = self.ui.Verde.value()   

        particula = Particula(Id,Ox,Oy,Dx,Dy,Vel,Red,Blue,Green)
        self.particulas.agregar_final(particula)
        
        #print(particula)
        #self.ui.salida.insertPlainText(str(IDD)+str(Ox)+str(Oy)+str(Dx)+str(Dy)+str(Vel)+str(Red)+str(Blue)+str(Green))

    @Slot()
    def click_agregarinicio(self):
        Id = self.ui.ID.value()
        Ox = self.ui.OrigenX.value()   
        Oy = self.ui.OrigenY.value() 
        Dx = self.ui.DestinoX.value()
        Dy = self.ui.DestinoY.value()
        Vel = self.ui.Velocidad.value()
        Red = self.ui.Rojo.value()
        Blue = self.ui.Azul.value()
        Green = self.ui.Verde.value()

        particula = Particula(Id,Ox,Oy,Dx,Dy,Vel,Red,Blue,Green)
        self.particulas.agregar_inicio(particula)

        #print(IDD,Ox,Oy,Dx,Dy,Vel,Red,Blue,Green)
        #self.ui.salida.insertPlainText(str(IDD)+str(Ox)+str(Oy)+str(Dx)+str(Dy)+str(Vel)+str(Red)+str(Blue)+str(Green))

    @Slot()
    def click_mostrar(self):
       # self.particulas.mostrar()
       self.ui.salida.clear()
       self.ui.salida.insertPlainText(str(self.particulas))
    
    @Slot()
    def setValue(self,valor):
       self.ui.NumAct.clear()
       self.ui.NumAct.insertPlainText(str(valor))