# MBGC - Monobank to GnuCash Importer

[![Build Status](https://img.shields.io/github/actions/workflow/status/IlliaDhD/MBGC/main.yml?branch=main)](https://github.com/IlliaDhD/MBGC/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple command-line tool to automatically fetch transactions from your Monobank account and import them directly into your GnuCash file, complete with smart categorization.

## The Problem

Manually exporting transaction statements from your bank, cleaning them up, and importing them into GnuCash is a tedious and time-consuming process. This tool automates that entire workflow for Monobank users, saving you time and ensuring your financial records are always up-to-date.

## ✨ Features

* **Direct API Integration**: Fetches transactions directly from the Monobank API.
* **Smart Categorization**: Uses a simple JSON mapping file to automatically assign transactions to the correct GnuCash expense/income accounts.
* **Direct GnuCash Import**: Imports the categorized transactions directly into your `.gnucash` file.
* **Duplicate Prevention**: Keeps track of the last imported transaction to avoid creating duplicate entries.
* **Actionable Reports**: Informs you of any new transaction types that need to be mapped.

## 🔧 Prerequisites

Before you begin, ensure you have the following:

* Python 3.8 or higher.
* An existing GnuCash data file (e.g., `my_finances.gnucash`).
* A Monobank account and your personal API access token.

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### 1. Installation

First, clone the repository to your local machine:
```bash
git clone [https://github.com/IlliaDhD/MBGC.git](https://github.com/IlliaDhD/MBGC.git)
cd MBGC
```

It is highly recommended to use a Python virtual environment:
```bash
# Create a virtual environment
python -m venv venv

# Activate it (on Windows)
.\venv\Scripts\activate

# Activate it (on macOS/Linux)
source venv/bin/activate
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 2. Configuration

This program requires several configuration steps to function correctly. You need to set up environment variables and create two JSON files for account and transaction mapping.

#### Environment Variables

The application requires the following environment variables to be set. You can set them in your shell, or use a `.env` file and a library like `python-dotenv`.

* `MBGC_API_TOKEN`: Your personal API token for the Monobank API.
* `GNUCASH_FILE_PATH`: The absolute or relative path to your GnuCash file (e.g., `/home/user/documents/finances.gnucash`).
* `ACCOUNTS_JSON_PATH`: The path to the `accounts.json` file. Defaults to `accounts.json` in the root directory.
* `MAPPING_JSON_PATH`: The path to the `mapping.json` file. Defaults to `mapping.json` in the root directory.

#### Configuration Files

You must create two JSON files in the project's root directory (or specify their paths using the environment variables above).

##### `accounts.json`

This file should contain a list of all your relevant GnuCash accounts. You need to provide the account name and its unique ID from GnuCash.

**Example `accounts.json`:**
```json
[
  {
    "id": "c3e5d3f2a1b94b0e8a7d6f5c4e3b2a1c",
    "name": "Expenses:Groceries"
  },
  {
    "id": "a1b2c3d4e5f64a7b8c9d0e1f2a3b4c5d",
    "name": "Expenses:Dining Out"
  },
  {
    "id": "f9e8d7c6b5a44b3c2a1b0f9e8d7c6b5a",
    "name": "Expenses:Transport:Fuel"
  },
  {
    "id": "1a2b3c4d5e6f4a7b8c9d0e1f2a3b4c5d",
    "name": "Assets:Current Assets:Monobank"
  }
]
```

##### `mapping.json`

This file maps transaction descriptions from the bank's API to one of your GnuCash account IDs from `accounts.json`. This allows the program to automatically categorize your transactions.

**Example `mapping.json`:**
```json
{
  "SuperMart": "c3e5d3f2a1b94b0e8a7d6f5c4e3b2a1c",
  "The Corner Cafe": "a1b2c3d4e5f64a7b8c9d0e1f2a3b4c5d",
  "Shell Gas Station": "f9e8d7c6b5a44b3c2a1b0f9e8d7c6b5a",
  "Pizzeria Roma": "a1b2c3d4e5f64a7b8c9d0e1f2a3b4c5d"
}
```
*In this example, any transaction with "The Corner Cafe" or "Pizzeria Roma" in its description will be assigned to the "Expenses:Dining Out" account.*

## ▶️ Usage

Once everything is configured, run the main script from the project's root directory:

```bash
python main.py
```

### ✅ Example Output

When you run the program, the expected output will look something like this, indicating the status of the import process:

```
Fetching new transactions from Monobank API...
Found 15 new transactions.
Processing and mapping transactions...
- 12 transactions mapped successfully.
- 3 transactions have no mapping rule. Please update mapping.json for the following descriptions: ['New Bookstore', 'Online Subscription', 'City Parking']
Importing 12 transactions into GnuCash...
Successfully imported 12 transactions into /home/user/documents/finances.gnucash.
Process finished.
```

## 🤝 Contributing

Contributions are welcome! If you have a suggestion or find a bug, please feel free to open an issue or submit a pull request.

1.  **Fork** the project.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.