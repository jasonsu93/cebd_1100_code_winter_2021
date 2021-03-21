import datetime
from PurchaseEntities.Item import Item
import PurchaseEntities.Constant as constant

class Order:
    def __init__(self, order_number):

        self.order_number = order_number
        self.order_date = datetime.datetime.now()

        self.items = []

    def add_item(self, item : Item):
        self.items.append(item)

    def remove_item(self, sku):

        for i in self.items:
            if i.sku == sku:
                pass
                #delete the item here


    def total_item_price_notax(self):

        total_price = 0.0

        for i in self.items:
            total_price = total_price + i.price
        return total_price


    #Assume the tax rate = 15.56%
    def total_item_price_withtax(self):

        total_price = self.total_item_price_notax()

        for i in self.items:
            if i.taxable:
                total_price += i.price * constant.TAX_RATE

        return total_price

    def __str__(self):

        order_text = ("Order number: " + str(self.order_number) + "\n" + ("-" * 20) + "\n"

        for i in self.items:
            order_text = order_text + print(i) + "\n"

        order_text = order_text + "\n"

        order_text = order_text + "Total price with tax : " + str(self.total_item_price_withtax())

        print()
        print("Total price with tax " + str(self.total_item_price_withtax()))