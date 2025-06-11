import tkinter as tk
from tkinter import messagebox, simpledialog

menu = {
    "Pizza": 40,
    "Pasta": 90,
    "Burger": 40,
    "Sandwitches": 60,
    "Samosa": 15,
    "Momos": 30,
}

def order_food():
    order_total = 0
    menu_text = "\n".join([f"{item}: ₹{price}" for item, price in menu.items()])
    messagebox.showinfo("Menu", f"Hi! Here's the menu:\n{menu_text}")

    item1 = simpledialog.askstring("Order", "Please enter the item name:")
    if item1 and item1 in menu:
        order_total += menu[item1]
        messagebox.showinfo("Order", f"Your item {item1} has been successfully ordered")
    else:
        messagebox.showwarning("Order", "Please order according to Menu")
        return

    another_order = simpledialog.askstring("Order", "Do you want another order? Type Y / N")
    if another_order and another_order.upper() == "Y":
        item2 = simpledialog.askstring("Order", "Please enter another order:")
        if item2 and item2 in menu:
            order_total += menu[item2]
            messagebox.showinfo("Order", f"Your item {item2} has been successfully ordered")
        else:
            messagebox.showwarning("Order", "Ordered item isn't available right now")

    messagebox.showinfo("Transaction ", f"Your total transaction amount is ₹{order_total}, Thank You!")

window = tk.Tk()
window.title("Welcome To FullCafe  ")
window.geometry('500x400')
heading = tk.Label(window, text="Welcome To FullCafe \n Your Organisation's GUI based ordering system", font=("Georgia", 24, "bold"))
heading.pack(pady=20)


order_btn = tk.Button(window, text="Order Food ", command=order_food, font=("Georgia", 16))
order_btn.pack(pady=50)

window.mainloop()