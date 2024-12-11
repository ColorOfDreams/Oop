class item:
    def __init__(self, name, price, discount):
        self._name = name
        self._price = price
        self._discount = discount
    
    def __str__(self):
        return f"name : {self._name}; price : {self._price}; discount : {self._discount}"

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Yêu cầu giá tiền phải là số và có giá trị lớn hơn 0.")
        self._price = value
    
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        self._discount = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Yêu cầu tên không trống và chỉ được chứa kí tự chữ.")
        self._name = value.strip()


class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"name : {self.name}"

class BillLine:
    def __init__(self, item, quantity):
        self.quantity = quantity
        self.item = item

    @property
    def quantity(self):
        return self._quantity 

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, (int)) or value < 0:
            raise ValueError("Yêu cầu số lượng phải là số và có giá trị lớn hơn hoặc bằng 0")
        self._quantity = value

    def TotalLinePrice(self):
        return self.quantity * self.item.price

    def TotalLineDiscount(self):
        return self.quantity * self.item.discount
    
    def __str__(self):
        return f"name : {self.item.name}; quantity : {self.quantity}; total price : {self.TotalLinePrice()}"

class GroceryBill:
    def __init__(self, clerk):
        self.clerk = clerk
        self.bill_lines = []

    def add(self, bill_line):
        self.bill_lines.append(bill_line)

    def Total(self):
        return sum(line.TotalLinePrice() for line in self.bill_lines)

    def print(self):
        print(f"Clerk: {self.clerk.name}\nReceipt:")
        for line in self.bill_lines:
            print(line)
        print(f"Total: ${self.Total():.2f}")


class DiscountBill(GroceryBill):
    def __init__(self, clerk, preferred):
        super().__init__(clerk)
        self.preferred = preferred

    def Total(self):
        if not self.preferred:
            return super().Total()
        return super().Total() - self.DiscountAmount()
    
    def DiscountCount(self):
        return sum(1 for line in self.bill_lines if line.item.discount > 0)
    
    def DiscountAmount(self):
        return sum(line.TotalLineDiscount() for line in self.bill_lines)
    
    def DiscountPercent(self):
        if super().Total() == 0:
            return 0
        return (self.DiscountAmount() / super().Total()) * 100
    
    def print(self):
        super().print()
        if self.preferred:
            print(f"Discount: ${self.DiscountAmount():.2f} ({self.DiscountPercent():.2f}%)")

    
if __name__ == "__main__":
    clerk = Employee("John")

    item1 = item("Candy Bar", 1.35, 0.25)
    item2 = item("Apple", 0.50, 0.0)
    item3 = item("Milk", 3.00, 0.5)

    bill_line1 = BillLine(item1,2)

    bill_line2 = BillLine(item2,5)

    bill_line3 = BillLine(item3,1)

    print("GroceryBill")
    grocery_bill = GroceryBill(clerk)
    grocery_bill.add(bill_line1)
    grocery_bill.add(bill_line2)
    grocery_bill.add(bill_line3)
    grocery_bill.print()

    print("DiscountBill (Preferred Customer) ")
    discount_bill = DiscountBill(clerk, preferred=True)
    discount_bill.add(bill_line1)
    discount_bill.add(bill_line2)
    discount_bill.add(bill_line3)
    discount_bill.print()
    print(f"Discount Count: {discount_bill.DiscountCount()}")
    print(f"Discount Amount: ${discount_bill.DiscountAmount():.2f}")
    print(f"Discount Percent: {discount_bill.DiscountPercent():.2f}%")
