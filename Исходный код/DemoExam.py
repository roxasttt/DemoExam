import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
from DatabaseManager import DatabaseManager


class PartnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система управления партнерами")
        self.db_manager = DatabaseManager('company.db')

        self.create_main_menu()

    def create_main_menu(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        add_partner_btn = ttk.Button(main_frame, text="Добавить/Редактировать партнера", command=self.add_edit_partner)
        add_partner_btn.grid(row=0, column=0, pady=5)

        view_sales_history_btn = ttk.Button(main_frame, text="Просмотреть историю продаж",
                                            command=self.view_sales_history)
        view_sales_history_btn.grid(row=1, column=0, pady=5)

    def add_edit_partner(self):
        partner_window = tk.Toplevel(self.root)
        partner_window.title("Добавить/Редактировать партнера")

        form_frame = ttk.Frame(partner_window, padding="10")
        form_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        tk.Label(form_frame, text="Название").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        name_entry = ttk.Entry(form_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(form_frame, text="Адрес").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        address_entry = ttk.Entry(form_frame)
        address_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(form_frame, text="Данные").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        data_entry = ttk.Entry(form_frame)
        data_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(form_frame, text="ID компании").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        company_id_entry = ttk.Entry(form_frame)
        company_id_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        save_btn = ttk.Button(form_frame, text="Сохранить", command=lambda: self.save_partner(
            name_entry.get(), address_entry.get(), data_entry.get(), company_id_entry.get()
        ))
        save_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def save_partner(self, name, address, data, company_id):
        try:
            company_id = int(company_id)
            self.db_manager.add_partner(name, address, data, company_id)
            messagebox.showinfo("Успех", "Партнер добавлен успешно!")
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ID компании")

    def view_sales_history(self):
        sales_window = tk.Toplevel(self.root)
        sales_window.title("История продаж")

        form_frame = ttk.Frame(sales_window, padding="10")
        form_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        tk.Label(form_frame, text="ID партнера").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        partner_id_entry = ttk.Entry(form_frame)
        partner_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        show_btn = ttk.Button(form_frame, text="Показать",
                              command=lambda: self.show_sales_history(partner_id_entry.get()))
        show_btn.grid(row=1, column=0, columnspan=2, pady=10)

        self.sales_tree = ttk.Treeview(form_frame, columns=("Product", "Quantity", "Date"), show="headings")
        self.sales_tree.heading("Product", text="Продукт")
        self.sales_tree.heading("Quantity", text="Количество")
        self.sales_tree.heading("Date", text="Дата")
        self.sales_tree.grid(row=2, column=0, columnspan=2, pady=10)

    def show_sales_history(self, partner_id):
        try:
            partner_id = int(partner_id)
            history = self.db_manager.view_sales_history(partner_id)
            for i in self.sales_tree.get_children():
                self.sales_tree.delete(i)
            for row in history:
                self.sales_tree.insert("", "end", values=row)
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ID партнера")


if __name__ == "__main__":
    root = tk.Tk()
    app = PartnerApp(root)
    root.mainloop()