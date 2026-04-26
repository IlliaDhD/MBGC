# MBGC - Monobank Transaction Categorizer

[![Build Status](https://img.shields.io/github/actions/workflow/status/IlliaDhD/MBGC/main.yml?branch=main)](https://github.com/IlliaDhD/MBGC/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MBGC is a command-line tool to fetch transactions from your Monobank account, categorize them using custom rules, and export the results to CSV for further analysis or import into other systems.

## Overview

This tool automates the process of retrieving Monobank transactions, mapping them to categories based on your configuration, and saving the results. It is highly configurable and extensible, making it easy to adapt to your personal finance workflow.

## ✨ Features

- **Direct Monobank API Integration**: Fetches transactions for a configurable period.
- **Custom Categorization**: Uses JSON files to map transaction descriptions to categories.
- **Automatic Detection of New Institutions**: Unmapped transaction descriptions are added to the mapping file for easy future categorization.
- **CSV Export**: Saves processed transactions as CSV files for further use.
- **Configurable via Environment Variables**: All paths and options are set via environment variables (see below).

## Prerequisites

- Python 3.8 or higher
- Monobank account and API token

## Project Structure

```
MBGC/
├── entrypoint.sh                # Script to activate venv, set env vars, and run main.py
├── requirements.txt             # Python dependencies
├── main.py                      # Main application logic
├── config.py                    # Configuration and environment variable handling
├── app/
│   ├── api/
│   │   ├── mono_api.py          # Monobank API interaction
│   │   └── time_bounds.py       # Time period calculation utilities
│   └── data_processing/
│       ├── data_processing.py   # Data transformation and categorization
│       └── saving.py            # CSV and mapping file saving utilities
├── data/
│   ├── categories.json          # Category definitions
│   └── institution_to_category.json # Mapping of descriptions to categories
├── tests/                       # Unit tests
└── README.md
```

## 🚀 Getting Started

Clone the repository and set up your environment:
```bash
git clone https://github.com/IlliaDhD/MBGC.git
cd MBGC
```

It is highly recommended to use a Python virtual environment:

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (Linux/macOS)
source .venv/bin/activate
# Activate it (Windows)
.\.venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

All configuration is handled via environment variables. You can set them in your shell, in `entrypoint.sh`, or with a `.env` file (if you use a tool like `python-dotenv`).

**Required environment variables:**

- `API_TOKEN` — Your Monobank API token
- `MONO_ACCOUNT_ID` — Your Monobank account ID (default: 0)
- `MONO_REQUEST_PERIOD` — Period (in seconds) to fetch transactions for (default: 1 month)
- `MONO_REQUEST_PERIOD_DAYS` — Alternative: number of days to fetch (overrides period)
- `CATEGORIES_JSON_PATH` — Path to `categories.json` (category definitions)
- `CATEGORIES_MAPPER_JSON_PATH` — Path to `institution_to_category.json` (description-to-category mapping)
- `RESULT_CSV_PATH` — Directory to save result CSV files
- `DEFAULT_CATEGORY` — Default category name for unmapped transactions
- `DEFAULT_CATEGORY_ID` — Default category ID for new institutions

**Data files:**

- `data/categories.json` — Maps category IDs to category names
- `data/institution_to_category.json` — Maps transaction descriptions to category IDs

## Usage

You can run the application using the provided `entrypoint.sh` script (recommended):

```bash
./entrypoint.sh
```

Or manually:

```bash
source .venv/bin/activate
python main.py
```

## Example Workflow

1. The app fetches transactions from Monobank for the configured period.
2. It loads categories and mapping data from JSON files.
3. Each transaction is mapped to a category. New/unmapped descriptions are added to the mapping file with a default category.
4. The processed transactions are saved as a CSV file in the results directory.

## Example Output

```
Requesting transactions for period: [(1700000000.0, 1700864000.0)]
Obtained transactions: [...]
Mapped 15 transactions timestamps to ISO format
Mapped operationAmount for 15 transactions
Wrote new institutions to the mappers file
Wrote results the file: data/2025-10-23-2025-12-22.csv
```

## Testing

Unit tests are located in the `tests/` directory. To run tests:

```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is distributed under the MIT License. See the `LICENSE` file for more information.