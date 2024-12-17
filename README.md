# Expense Tracker

## Overview  
The **Expense Tracker** is a Flask-based web application that helps users manage their income and expenses efficiently. It allows users to add, view, and categorize financial transactions, enabling better budget management and financial tracking.

---

## Features  
- **Add Transactions**: Add income and expense details, including type, category, date, and amount.  
- **View Transactions**: View a list of all transactions in a table sorted by date.  
- **Database Integration**: All data is stored in a SQLite database (`expenseDB.db`).  
- **Secure Configuration**: Flask `SECRET_KEY` for security.  
- **Organized Codebase**: Cleanly organized with models, routes, and templates.

---

## Project Structure  

```
/PROJECT 4 EXPENSE TRACKER
│
├── run.py                       # Entry point for the Flask app
│
├── /application
│   ├── __init__.py              # Initializes the Flask app and database
│   ├── models.py                # Database models
│   ├── routes.py                # Application routes (logic)
│   ├── forms.py                 # WTForms for handling form submissions
│   └── templates/               # HTML templates for rendering pages
│
├── expenseDB.db                 # SQLite database file (auto-created)
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation
```

---

## Installation  

1. **Clone the Repository**  
   Clone this project to your local machine:  
   ```bash
   git clone https://github.com/vansh070605/Expense-Manager-App.git
   cd Expense-Manager-App
   ```

2. **Set Up Virtual Environment**  
   Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate       # For Linux/Mac
   venv\Scripts\activate          # For Windows
   ```

3. **Install Dependencies**  
   Install required packages using `pip`:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   Initialize the database and run the application:  
   ```bash
   python run.py
   ```

   The app will be accessible at:  
   **`http://127.0.0.1:5000/`**

---

## Dependencies  

- Flask  
- Flask-SQLAlchemy  
- Flask-WTF  
- WTForms  

Install all dependencies using:  
```bash
pip install -r requirements.txt
```

---

## Database Configuration  

The application uses **SQLite** as the database. The database file `expenseDB.db` will be automatically created when you run the app for the first time. To initialize the database manually, use:  

```python
from application import db, app
with app.app_context():
    db.create_all()
```

---

## Usage  

1. **Add Transactions**: Add new income or expense entries.  
2. **View Transactions**: View all transactions sorted by date.  
3. **Categories**: Group transactions by category for better analysis.

---

## Future Enhancements  

- Add user authentication for multiple users.  
- Generate visual reports (charts) for income/expense analysis.  
- Export transactions as CSV or PDF.  
- Add date-based filters to view transactions.  

---

## License  
This project is licensed under the MIT License.

---

## Contact  
For questions or contributions, please contact:  
**Vansh Agrawal** - [vansh070605@gmail.com]  
**GitHub**: [https://github.com/vansh070605](https://github.com/vannsh070605)
