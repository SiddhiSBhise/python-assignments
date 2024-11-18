import datetime
import matplotlib.pyplot as plt

def get_expenses():
    expenses = {}
    while True:
        category = input("Enter expense category (or 'done' to finish): ").lower()
        if category == "done":
            break
        amount = float(input(f"Enter amount for {category}: $"))
        expenses[category] = expenses.get(category, 0) + amount
    return expenses

def calculate_savings(income, expenses):
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    return total_expenses, savings

def visualize_expenses(expenses):
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Breakdown")
    plt.show()

income = float(input("Enter your monthly income: $"))
expenses = get_expenses()
total_expenses, savings = calculate_savings(income, expenses)
print(f"\nTotal Expenses: ${total_expenses}")
print(f"Savings: ${savings}")

visualize_expenses(expenses)

Solution 2:
import os
import shutil

def organize_files(folder_path):
    file_types = {
        "Documents": [".pdf", ".docx", ".txt"],
        "Images": [".jpg", ".jpeg", ".png"],
        "Music": [".mp3", ".wav"],
        "Videos": [".mp4", ".avi"],
    }
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(folder_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, dest_folder)
                    print(f"Moved: {file_name} -> {folder}")
                    break

folder_path = input("Enter the folder path to organize: ")
organize_files(folder_path)
