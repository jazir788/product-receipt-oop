import pandas as pd
from fpdf import FPDF


df = pd.read_csv("articles.csv", dtype={"id": str})

class Product:

    def __init__(self, product_id):
        self.product_id = product_id
        self.name = df.loc[df["id"] == self.product_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.product_id, "price"].squeeze()

    def available(self):
        in_stock = df.loc[df["id"] == self.product_id, 'in stock'].squeeze()
        return in_stock


class Receipt:

    def __init__(self, article):
        self.article = article

    def generate_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.product_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")



print(df)

p_id = input("Choose a product to buy: ")
product = Product(p_id)
if product.available():
    receipt = Receipt(product)
    receipt.generate_receipt()
else:
    print("No such product in stock")

