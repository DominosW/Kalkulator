from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox

class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):

        etykietanazwa = QLabel("Dominik Wijas", self)
        etykietanr1 = QLabel("Liczba numer 1:", self)
        etykietanr2 = QLabel("Liczba numer 2:", self)
        etykietanr3 = QLabel("Wynik:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(etykietanr1, 0, 0)
        ukladT.addWidget(etykietanr2, 1, 0)
        ukladT.addWidget(etykietanr3, 2, 0)

        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True

        ukladT.addWidget(self.liczba1Edt, 0, 1)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 2, 1)

        Przycisk_dodaj = QPushButton("&Dodaj", self)
        Przycisk_odejmij = QPushButton("&Odejmij", self)
        Przycisk_dziel = QPushButton("&Mnóż", self)
        Przycisk_mnoz = QPushButton("&Dziel", self)
        Przycisk_zamknij = QPushButton("&Zamknij program", self)
        Przycisk_zamknij.resize(Przycisk_zamknij.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(Przycisk_dodaj)
        ukladH.addWidget(Przycisk_odejmij)
        ukladH.addWidget(Przycisk_dziel)
        ukladH.addWidget(Przycisk_mnoz)

        ukladT.addLayout(ukladH, 5, 0, 1, 3)
        ukladT.addWidget(Przycisk_zamknij, 6, 0, 1, 3)

        self.setLayout(ukladT)

        Przycisk_dodaj.clicked.connect(self.dzialanie)
        Przycisk_odejmij.clicked.connect(self.dzialanie)
        Przycisk_mnoz.clicked.connect(self.dzialanie)
        Przycisk_dziel.clicked.connect(self.dzialanie)
        Przycisk_zamknij.clicked.connect(self.koniec)

        self.liczba1Edt.setFocus()
        self.setGeometry(20, 20, 300, 500)
        self.setWindowTitle("Kalkulator (Dominik Wijas)")
        self.show()

    def koniec(self):
        self.close()

    def dzialanie(self):

        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())
            wynik = ""

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "&Odejmij":
                wynik = liczba1 - liczba2
            elif nadawca.text() == "&Mnóż":
                wynik = liczba1 * liczba2
            else:  # dzielenie
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return

            self.wynikEdt.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Podaj inne dane", QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
