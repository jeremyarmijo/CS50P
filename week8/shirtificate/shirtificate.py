from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", "", 50)
        self.cell(0, 60, "CS50 Shirtificate", align="C")

    def create_shirtificate(self, name):
        self.add_page()
        self.set_font("Helvetica", size=25)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, name, align="C")
        self.image("shirtificate.png", x=10, y=70, w=190, h=190)
        self.text(110 - (len(name) * 2), 130, name)


def main():
    name = input("Name: ")
    shirtificate = Shirtificate(orientation="P", unit="mm", format="A4")
    shirtificate.create_shirtificate(f"{name} took CS50")
    shirtificate.output("shirtificate.pdf")


if __name__ == "__main__":
    main()