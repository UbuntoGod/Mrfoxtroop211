import csv

headers = ["Date", "Description", "Category", "Amount"]
categories = [
    "Housing",
    "Utilities",
    "Groceries",
    "Transportation",
    "Entertainment",
    "Miscellaneous",
]

with open("budget_template.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerow([])
    writer.writerow(["Total Spending", "", "", "=SUM(D:D)"])
    writer.writerow([])
    writer.writerow(["Category Totals:"])
    writer.writerow(["Category", "Total"])
    for cat in categories:
        writer.writerow([cat, f"=SUMIF(C:C,\"{cat}\",D:D)"])
