# StockFlow - Inventory Management System

**StockFlow** is a Django-based inventory management system designed to help users manage their stock and sales efficiently. This project includes functionality for adding items to stock, selling items, and generating PDF sales reports.

## Features

- **Add Items to Stock:** Users can add new items to the inventory with fields such as item name, quantity, and price.
- **Sell Items from Stock:** Users can sell items, which will update the stock accordingly.
- **Generate PDF Sales Reports:** The system can generate a PDF report of all sales, detailing item names, quantities sold, and total revenue.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/stock_flow.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd stock_flow
   ```
3. **Create a Virtual Environment:**
   ```bash
   python3 -m venv env
   ```
4. **Activate the Virtual Environment:**
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     .\env\Scriptsctivate
     ```
5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

## Usage

- **Add Items to Stock:** Navigate to `/add-item/` to add new items to the stock.
- **Sell Items from Stock:** Go to `/sell-item/` to sell an item and update the stock.
- **Generate Sales Report:** Access `/sales-report/` to generate a PDF report of all sales.

## Dependencies

- Django
- WeasyPrint (or other PDF generation package like xhtml2pdf)

Install all dependencies listed in `requirements.txt`.

## Contributing

Feel free to fork this repository, create a new branch, and submit a pull request if you would like to contribute to this project.
