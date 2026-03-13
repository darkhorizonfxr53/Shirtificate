from fpdf import FPDF
#FPDF (Free pdf = a popular library allowing to program a doc instead of typing it on word or google docs)
#Used to automate the process using coding properties like loops, f(x), etc.
class Shirtificate(FPDF): #Inheritance, instead of writing pdf from scratch, you "inherit" from pdf library (having all of its tools: e.g. image(), cell(), and output().)
    def __init__(self, name): #Constructor (Setup f(x) auto runs when typed pdf = Shirtiticate ("Your Name"), takes user's name as input 4 later)
        super().__init__(orientation="P", unit="mm", format="A4")
                        #Sets page to portrait mode (Unit measure alles in mm (ezier 4 A4), format(Set page size to standard 210mm x 297mm))
        self.add_page()# add_page(): Creates a new blank sheet.
        self.set_auto_page_break(False) #By having this off, prevent library from creating a second blank page if shirt image gets too close to margin.
        self._draw_header() #method call of def_draw_header(self)
        self._draw_shirt(name) #self._draw_shirt(name) These aren't built-in FPDF commands. These are custom functions you wrote (or will write) within your class. By calling them inside __init__, you ensure that the second you create the object, it immediately draws the title and the shirt without you having to call those functions manually in main.

# image(): Places a .jpg or .png file at specific coordinates.
# output(): Saves the final result to your computer.
    def _draw_header(self):
        self.set_font("helvetica", "B", 45)
        # set_font(): Loads the typeface (like Helvetica or Arial).
        # cell(): Prints a line of text.
        # 2. Print the text "CS50 Shirtificate"
    # 0 = use full width of page
    # 60 = height of the cell (creating top margin)
    # align="C" = Center the text
        self.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    def _draw_shirt(self, name):
        # Image centering: A4 width is 210mm.
        # If image width is 190mm, x should be (210 - 190) / 2 = 10
        self.image("shirtificate.png", x=10, y=70, w=190)

        # Set text color to white for the name on the shirt
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", "B", 25)

        # Move "y" to the middle of the shirt area
        self.set_y(140)
        self.cell(0, 10, f"{name} took CS50", align="C")
#Main function
def main():
    name = input("Name: ") #Get user's name
    pdf = Shirtificate(name) #Call the constructor/class
    pdf.output("shirtificate.pdf")  #Give out the pdf with it's name in brackets
#Run the program
if __name__ == "__main__":
    main()
