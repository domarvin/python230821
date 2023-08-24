import openpyxl
from openpyxl import Workbook

# Sample electronic product sales data
sales_data = [
    ["Product Name", "Price", "Quantity", "Total Sales"],
    ["Product A", 500, 10, "=B2*C2"],
    ["Product B", 800, 5, "=B3*C3"],
    ["Product C", 1200, 8, "=B4*C4"],
]

# Create a new Workbook and select the active worksheet
workbook = Workbook()
worksheet = workbook.active

# Populate the worksheet with the sales data
for row in sales_data:
    worksheet.append(row)

# Save the workbook to a specific file
file_path = "electronic_sales_data.xlsx"
workbook.save(file_path)

print("Sales data saved to", file_path)
