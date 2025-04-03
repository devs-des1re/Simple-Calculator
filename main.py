from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.config import Config

Builder.load_file("main.kv")

class MainWidget(Widget):
    def clear(self):
        self.ids.answer_box.text = "0"

    def number_pressed(self, number):
        prev_number = self.ids.answer_box.text

        if prev_number == "0" or prev_number == "Math Error" or prev_number == "Syntax Error":
            self.ids.answer_box.text = f"{number}"
        else:
            self.ids.answer_box.text = f"{prev_number}{number}"

    def sign_pressed(self, sign):
        prev_number = self.ids.answer_box.text

        if prev_number[-1] == "÷" or prev_number[-1] == "×" or prev_number[-1] == "+" or prev_number[-1] == "-":
            prev_number = prev_number[:-1]
            self.ids.answer_box.text = f"{prev_number}{sign}"
        elif prev_number == "Math Error" or prev_number == "Syntax Error":
            self.ids.answer_box.text = "0"
        else:
            self.ids.answer_box.text = f"{prev_number}{sign}"

    def pn_pressed(self):
        prev_number = self.ids.answer_box.text
        
        if prev_number != "0":
            if "-" in prev_number:
                self.ids.answer_box.text = f"{prev_number.replace('-', '')}"
            else:
                self.ids.answer_box.text = f"-{prev_number}"
    
    def dm_pressed(self):
        prev_number = self.ids.answer_box.text
        if not prev_number[-1] == ".":
            self.ids.answer_box.text = f"{prev_number}."

    def delete_pressed(self):
        prev_number = self.ids.answer_box.text
        if prev_number != "0":
            prev_number = prev_number[:-1]
            if prev_number == "":
                self.ids.answer_box.text = "0"
            else:
                self.ids.answer_box.text = prev_number

    def equals_pressed(self):
        text = self.ids.answer_box.text
        text = text.replace("%", "/100")
        text = text.replace("×", "*")
        text = text.replace("÷", "/")

        try:
            answer = eval(text)
            if isinstance(answer, float) and answer.is_integer():
                self.ids.answer_box.text = str(int(answer))
            else:
                self.ids.answer_box.text = str(answer)
        except SyntaxError:
            self.ids.answer_box.text = "Syntax Error"
        except ZeroDivisionError:
            self.ids.answer_box.text = "Math Error"
        except:
            self.ids.answer_box.text = "Math Error"


class MainApp(App):
    def build(self):
        return MainWidget()
    
if __name__ == "__main__":
    MainApp().run()