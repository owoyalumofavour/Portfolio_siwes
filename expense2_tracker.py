# expense tracker with gui
# a graphical expense tracking app built with tkinter

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# file where expenses are stored
data_file = "expenses.json"

# load expenses from json file
def load_expenses():
    if not os.path.exists(data_file):
        return []
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except:
        return []

# save expenses to json file
def save_expenses(expenses):
    with open(data_file, "w") as f:
        json.dump(expenses, f, indent=2)

# main app class
class expenseapp:
    def __init__(self, root):
        self.root = root
        self.root.title("expense tracker")
        self.root.geometry("800x600")
        self.root.configure(bg="#f4f4f4")

        # load existing expenses
        self.expenses = load_expenses()

        # build the interface
        self.build_header()
        self.build_input_section()
        self.build_filter_section()
        self.build_table()
        self.build_summary()
        self.build_buttons()

        # show expenses on startup
        self.refresh_table()

    # top header with title
    def build_header(self):
        header = tk.Frame(self.root, bg="#667eea", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="expense tracker",
            font=("segoe ui", 22, "bold"),
            bg="#667eea",
            fg="white"
        )
        title.pack(pady=20)

    # input area for adding new expenses
    def build_input_section(self):
        frame = tk.LabelFrame(
            self.root,
            text=" add new expense ",
            font=("segoe ui", 11, "bold"),
            bg="#f4f4f4",
            padx=15,
            pady=15
        )
        frame.pack(fill="x", padx=20, pady=(20, 10))

        # description input
        tk.Label(frame, text="description:", bg="#f4f4f4", font=("segoe ui", 10)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.desc_entry = tk.Entry(frame, font=("segoe ui", 10), width=25)
        self.desc_entry.grid(row=0, column=1, padx=5, pady=5)

        # category dropdown
        tk.Label(frame, text="category:", bg="#f4f4f4", font=("segoe ui", 10)).grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.category_var = tk.StringVar(value="food")
        categories = ["food", "transport", "shopping", "bills", "entertainment", "other"]
        self.category_menu = ttk.Combobox(
            frame,
            textvariable=self.category_var,
            values=categories,
            font=("segoe ui", 10),
            width=15,
            state="readonly"
        )
        self.category_menu.grid(row=0, column=3, padx=5, pady=5)

        # amount input
        tk.Label(frame, text="amount:", bg="#f4f4f4", font=("segoe ui", 10)).grid(row=0, column=4, sticky="w", padx=5, pady=5)
        self.amount_entry = tk.Entry(frame, font=("segoe ui", 10), width=12)
        self.amount_entry.grid(row=0, column=5, padx=5, pady=5)

        # add button
        add_btn = tk.Button(
            frame,
            text="add expense",
            command=self.add_expense,
            bg="#667eea",
            fg="white",
            font=("segoe ui", 10, "bold"),
            padx=15,
            pady=5,
            relief="flat",
            cursor="hand2"
        )
        add_btn.grid(row=0, column=6, padx=10, pady=5)

    # filter section
    def build_filter_section(self):
        frame = tk.Frame(self.root, bg="#f4f4f4")
        frame.pack(fill="x", padx=20, pady=(5, 5))

        tk.Label(frame, text="filter by category:", bg="#f4f4f4", font=("segoe ui", 10)).pack(side="left", padx=5)

        self.filter_var = tk.StringVar(value="all")
        filter_options = ["all", "food", "transport", "shopping", "bills", "entertainment", "other"]
        filter_menu = ttk.Combobox(
            frame,
            textvariable=self.filter_var,
            values=filter_options,
            font=("segoe ui", 10),
            width=15,
            state="readonly"
        )
        filter_menu.pack(side="left", padx=5)
        filter_menu.bind("<<comboboxselected>>", lambda e: self.refresh_table())

        # reset button
        reset_btn = tk.Button(
            frame,
            text="reset filter",
            command=self.reset_filter,
            bg="#e0e0e0",
            font=("segoe ui", 9),
            padx=10,
            relief="flat",
            cursor="hand2"
        )
        reset_btn.pack(side="left", padx=5)

    # table showing all expenses
    def build_table(self):
        frame = tk.Frame(self.root, bg="#f4f4f4")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        # scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        # treeview table
        columns = ("date", "description", "category", "amount")
        self.tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=12
        )
        scrollbar.config(command=self.tree.yview)

        # column headings
        self.tree.heading("date", text="date")
        self.tree.heading("description", text="description")
        self.tree.heading("category", text="category")
        self.tree.heading("amount", text="amount")

        # column widths
        self.tree.column("date", width=140, anchor="center")
        self.tree.column("description", width=280, anchor="w")
        self.tree.column("category", width=120, anchor="center")
        self.tree.column("amount", width=100, anchor="e")

        self.tree.pack(fill="both", expand=True)

    # summary bar at the bottom
    def build_summary(self):
        frame = tk.Frame(self.root, bg="#1e293b", height=50)
        frame.pack(fill="x", padx=20, pady=(0, 10))
        frame.pack_propagate(False)

        self.summary_label = tk.Label(
            frame,
            text="total: 0.00",
            font=("segoe ui", 14, "bold"),
            bg="#1e293b",
            fg="#38bdf8"
        )
        self.summary_label.pack(pady=12)

    # action buttons
    def build_buttons(self):
        frame = tk.Frame(self.root, bg="#f4f4f4")
        frame.pack(fill="x", padx=20, pady=(0, 20))

        # delete selected button
        delete_btn = tk.Button(
            frame,
            text="delete selected",
            command=self.delete_selected,
            bg="#ef4444",
            fg="white",
            font=("segoe ui", 10, "bold"),
            padx=15,
            pady=8,
            relief="flat",
            cursor="hand2"
        )
        delete_btn.pack(side="left", padx=5)

        # clear all button
        clear_btn = tk.Button(
            frame,
            text="clear all",
            command=self.clear_all,
            bg="#f59e0b",
            fg="white",
            font=("segoe ui", 10, "bold"),
            padx=15,
            pady=8,
            relief="flat",
            cursor="hand2"
        )
        clear_btn.pack(side="left", padx=5)

        # exit button
        exit_btn = tk.Button(
            frame,
            text="exit",
            command=self.root.quit,
            bg="#64748b",
            fg="white",
            font=("segoe ui", 10, "bold"),
            padx=15,
            pady=8,
            relief="flat",
            cursor="hand2"
        )
        exit_btn.pack(side="right", padx=5)

    # add a new expense
    def add_expense(self):
        description = self.desc_entry.get().strip()
        category = self.category_var.get().strip().lower()
        amount_text = self.amount_entry.get().strip()

        # validate inputs
        if not description:
            messagebox.showwarning("missing info", "please enter a description.")
            return

        if not amount_text:
            messagebox.showwarning("missing info", "please enter an amount.")
            return

        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("invalid amount", "amount must be a positive number.")
            return

        # create expense record
        expense = {
            "description": description,
            "category": category,
            "amount": amount,
            "date": datetime.now().strftime("%y-%m-%d %h:%m")
        }

        self.expenses.append(expense)
        save_expenses(self.expenses)

        # clear input fields
        self.desc_entry.delete(0, tk.end)
        self.amount_entry.delete(0, tk.end)
        self.desc_entry.focus()

        # refresh the display
        self.refresh_table()

    # refresh the table with current filter
    def refresh_table(self):
        # clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # apply filter
        filter_value = self.filter_var.get()
        if filter_value == "all":
            filtered = self.expenses
        else:
            filtered = [e for e in self.expenses if e["category"] == filter_value]

        # add rows
        for i, exp in enumerate(filtered):
            tag = "even" if i % 2 == 0 else "odd"
            self.tree.insert(
                "",
                "end",
                values=(
                    exp["date"],
                    exp["description"],
                    exp["category"],
                    f"{exp['amount']:.2f}"
                ),
                tags=(tag,)
            )

        # alternate row colors
        self.tree.tag_configure("even", background="#ffffff")
        self.tree.tag_configure("odd", background="#f9f9f9")

        # update the total
        total = sum(e["amount"] for e in filtered)
        self.summary_label.config(text=f"total: {total:,.2f}")

    # reset filter to show all
    def reset_filter(self):
        self.filter_var.set("all")
        self.refresh_table()

    # delete the selected expense
    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("no selection", "please select an expense to delete.")
            return

        # get the values from the selected row
        values = self.tree.item(selected[0], "values")
        date, description, category, amount_str = values

        # find the matching expense in the list
        for exp in self.expenses:
            if (exp["date"] == date and exp["description"] == description
                    and exp["category"] == category
                    and f"{exp['amount']:.2f}" == amount_str):
                self.expenses.remove(exp)
                break

        save_expenses(self.expenses)
        self.refresh_table()

    # clear all expenses
    def clear_all(self):
        if not self.expenses:
            messagebox.showinfo("nothing to clear", "there are no expenses to clear.")
            return

        confirm = messagebox.askyesno(
            "confirm",
            "are you sure you want to delete all expenses? this cannot be undone."
        )
        if confirm:
            self.expenses = []
            save_expenses(self.expenses)
            self.refresh_table()


# run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = expenseapp(root)
    root.mainloop()