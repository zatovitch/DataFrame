# requirements.txt
# This file is intentionally left blank.

# DataFrame Project

## Description
The DataFrame project is a Python application that demonstrates the creation and manipulation of a DataFrame using the `pandas` library. It provides functionalities to display data, calculate statistics, and perform group operations.

## Features
- Creates a DataFrame from a dictionary of data.
- Displays the DataFrame.
- Calculates the average and maximum salary.
- Additional functionalities like grouping by department and calculating average salary per department.

## Getting Started

### Prerequisites
Make sure you have Python and `pandas` installed on your machine. You can install `pandas` using `pip`.

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dataframe-project.git
    ```
2. Navigate to the project directory:
    ```sh
    cd dataframe-project
    ```
3. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```sh
    pip install pandas
    ```

## Usage
To start the application, run the following command:
```sh
python src/DataFrame.py
```

## Project Structure
```
dataframe-project
├── src
│   ├── DataFrame.py       # Main script to create and manipulate the DataFrame
│   ├── DataFrame1.py      # Additional functionalities or examples related to DataFrame
├── data
│   └── sample_data.csv    # Sample CSV data file (if any)
├── tests
│   └── test_dataframe.py  # Unit tests for DataFrame functionalities
└── README.md              # Project documentation
```

## exemples de données

data = {
    "Nom": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Âge": [25, 30, 35, 40, 28, 33, 38, 45, 50, 55],
    "Salaire": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 85000, 90000, 95000],
    "Département": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"]
}


## Contributing

python -m unittest discover -s tests

## License

This project is open-source and available for modification and distribution.