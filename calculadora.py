import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QGridLayout, QPushButton, QLineEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora PyQt6")
        self.setGeometry(100, 100, 300, 400) # x, y, ancho, alto
        self.init_ui()

    def init_ui(self):
        # --- Layout Principal ---
        # Usamos un layout vertical: Pantalla arriba, botones abajo
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # --- Pantalla (Display) ---
        self.display = QLineEdit()
        self.display.setFixedHeight(50) #Establece el alto de la pantalla donde ser verán los números
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight) #alinea los botones
        self.display.setFont(QFont('Arial', 20))
        self.display.setReadOnly(True) # Para que solo se escriba con botones
        main_layout.addWidget(self.display) #crea la pantalla como tal

        # --- Contenedor de Botones (Grid) ---
        
        grid_layout = QGridLayout() # genera la variable  para el grid del layout
        main_layout.addLayout(grid_layout) #invoca la propiedad del main enviadno por parametro la variable del grid

        # Lista de botones (etiqueta, posición fila, posición columna)
        botones = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        # Generación automática de botones
        for texto, fila, col in botones:
            boton = QPushButton(texto)
            boton.setFont(QFont('Arial', 14))
            boton.setFixedSize(60, 60)
            # Conectamos el clic. Usamos lambda para pasar el texto del botón
            boton.clicked.connect(lambda _, t=texto: self.on_click(t))
            grid_layout.addWidget(boton, fila, col)

    def on_click(self, texto):
        """Maneja la lógica cuando se presiona un botón."""
        if texto == '=':
            try:
                # eval() calcula la expresión matemática (ej: "2+2")
                expresion = self.display.text()
                resultado = str(eval(expresion)) 
                self.display.setText(resultado)
            except Exception:
                self.display.setText("Error")
        
        elif texto == 'C':
            # Borrar pantalla
            self.display.clear()
        
        else:
            # Agregar texto presionado a la pantalla actual
            texto_actual = self.display.text()
            self.display.setText(texto_actual + texto)

# --- Punto de entrada de la aplicación ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Aplicar un estilo oscuro (Opcional, para que se vea moderna)
    app.setStyle("Fusion")
    
    window = Calculadora()
    window.show()
    sys.exit(app.exec())