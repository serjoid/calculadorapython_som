import flet as ft
from playsound import playsound


class CalculatorApp(ft.UserControl):
    def build(self):
        self.reset()
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

        return ft.Container(
            bgcolor=ft.colors.BLACK,
            width=350,
            padding=20,
            border_radius=ft.border_radius.all(10),
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.result], alignment="end"),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="%",
                                expand=1,
                                bgcolor=ft.colors.WHITE10,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="%",),
                            ft.ElevatedButton(
                                text="/",
                                expand=1,
                                bgcolor=ft.colors.WHITE10,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="/",),
                            ft.ElevatedButton(
                                text="X",
                                expand=1,
                                bgcolor=ft.colors.WHITE10,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="*",),
                            ft.ElevatedButton(
                                text="-",
                                expand=1,
                                bgcolor=ft.colors.WHITE10,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="-",),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="7",
                                expand=1,
                                bgcolor=ft.
                                colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="7",),
                            ft.ElevatedButton(
                                text="8",
                                expand=1,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="8",),
                            ft.ElevatedButton(
                                text="9",
                                expand=1,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="9",),
                            ft.ElevatedButton(
                                text="+",
                                expand=1,
                                bgcolor=ft.colors.WHITE10,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="+",),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="4",
                                expand=1,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="4",),
                            ft.ElevatedButton(
                                text="5",
                                expand=1,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="5",),
                            ft.ElevatedButton(
                                text="6",
                                expand=1,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="6",),
                            ft.ElevatedButton(
                                text="=",
                                expand=1,
                                bgcolor=ft.colors.WHITE10,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="=",),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="1",
                                expand=1,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="1",),
                            ft.ElevatedButton(
                                text="2",
                                expand=1,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="2",),
                            ft.ElevatedButton(
                                text="3",
                                expand=1,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="3",),
                            ft.ElevatedButton(
                                text=".",
                                expand=1,
                                bgcolor=ft.colors.WHITE10,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data=".",
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="0",
                                expand=3,
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="0",
                            ),
                            ft.ElevatedButton(
                                text="clr",
                                expand=1,
                                bgcolor=ft.colors.WHITE10,
                                color=ft.colors.WHITE,
                                on_click=self.button_clicked,
                                data="clr",
                            ),
                        ]
                    )
                ]
            )
        )

    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == "Error" or data == "clr":
            self.result.value = "0"
            self.reset()
        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data
            if data == "0":
                playsound('0.mp3')
            elif data == "1":
                playsound("1.mp3")
            elif data == "2":
                playsound("2.mp3")
            elif data == "3":
                playsound("3.mp3")
            elif data == "4":
                playsound("4.mp3")
            elif data == "5":
                playsound("5.mp3")
            elif data == "6":
                playsound("6.mp3")
            elif data == "7":
                playsound("7.mp3")
            elif data == "8":
                playsound("8.mp3")
            elif data == "9":
                playsound("9.mp3")
        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
                self.new_operand = True
            if data == "+":
                playsound("mais.mp3")
            elif data == "-":
                playsound("menos.mp3")
            elif data == "*":
                playsound("x.mp3")
            elif data == "/":
                playsound("dividido.mp3")
        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            if data == "=":
                playsound("igual.mp3")
            self.reset()
        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            if data == "%":
                playsound("porcento.mp3")
            self.reset()
        elif float(self.result.value) < 0:
            self.result.value = str(
                self.format_number(abs(float(self.result.value)))
            )
        if data == ".":
            playsound("ponto.mp3")
        elif data == "clr":
            playsound("limpar.mp3")
        elif data == "snd":
            playsound == False
            if data == "snd":
                playsound == True

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Calculadora com Audio"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    calc = CalculatorApp()
    page.add(calc)


ft.app(target=main)
