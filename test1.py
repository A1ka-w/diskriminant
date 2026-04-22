import sys
import math
import io
import random  # оставил, как в вашем коде
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class QuadraticApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Квадратное уравнение')
        self.resize(320, 280)

        layout = QVBoxLayout()

        # Поля ввода (заменяют input())
        self.lbl_a = QLabel('Введите a:')
        self.line_a = QLineEdit()
        self.lbl_b = QLabel('Введите b:')
        self.line_b = QLineEdit()
        self.lbl_c = QLabel('Введите c:')
        self.line_c = QLineEdit()

        layout.addWidget(self.lbl_a)
        layout.addWidget(self.line_a)
        layout.addWidget(self.lbl_b)
        layout.addWidget(self.line_b)
        layout.addWidget(self.lbl_c)
        layout.addWidget(self.line_c)

        # Кнопка запуска
        self.btn_solve = QPushButton('Решить')
        self.btn_solve.clicked.connect(self.run_original_code)
        layout.addWidget(self.btn_solve)

        # Поле вывода (заменяет print())
        self.lbl_result = QLabel('Здесь появится результат...')
        self.lbl_result.setWordWrap(True)
        self.lbl_result.setStyleSheet("padding: 10px; background-color: #f0f0f0; border-radius: 5px;")
        layout.addWidget(self.lbl_result)

        self.setLayout(layout)

    def run_original_code(self):
        try:
            a = int(self.line_a.text())
            b = int(self.line_b.text())
            c = int(self.line_c.text())
        except ValueError:
            self.lbl_result.setText("⚠️ Ошибка: введите целые числа")
            return

        # Перенаправляем print() в память, чтобы не менять ваш код
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        try:
            # =========================================================
            #  ВАШ ИСХОДНЫЙ КОД (ВСТАВЛЕН БЕЗ ЕДИНОГО ИЗМЕНЕНИЯ)
            # =========================================================
            D = (b**2)- (4*a*c)

            if D > 0:
                D = math.sqrt(D)
                x1 = (-b - D ** 0.5) / (2 * a)
                x2 = (-b + D ** 0.5) / (2 * a)
                print({x1},{x2})
            elif D == 0:
                x = -b / 2 * a
                print({x})
            elif D < 0:
                print("Нет корней")
            # =========================================================
            #  КОНЕЦ ВАШЕГО КОДА
            # =========================================================

            # Забираем всё, что было выведено через print(), и показываем в GUI
            output = sys.stdout.getvalue()
            self.lbl_result.setText(output)

        except Exception as e:
            self.lbl_result.setText(f"❌ Ошибка выполнения: {e}")
        finally:
            # Возвращаем стандартный вывод на место
            sys.stdout = old_stdout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuadraticApp()
    window.show()
    sys.exit(app.exec_())