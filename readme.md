# Advanced Python Calculator

# Project Overview
The Advanced Python Calculator is a command-line application and it demonstrates:

1. A REPL (Read-Eval-Print Loop) interface for performing arithmetic operations.
2. A plugin system for dynamic command loading and extension of functionality.
3. Robust history management using Pandas to record and manage calculations.
4. Logging using Python’s built-in logging module, with log levels and destinations controlled by environment variables.
5. The use of multiple Design Patterns—such as Command, Facade, Singleton, and Strategy/Factory—to create a scalable, maintainable codebase.
6. Comprehensive testing with Pytest, including coverage reports and code quality checks with Pylint.

## Features
- **REPL Interface:**  
  Interactively execute commands with instant feedback. Type `menu` to view available commands and `exit` to quit.
  
- **Plugin System:**  
  Dynamically load additional commands from the `app/plugins/` directory without modifying core code. Examples include:
  - `greet_plugin` – Returns a customized greeting.
  - `export_csv` – Exports the calculation history to a CSV file.
  - Math plugins: `sqrt`, `power`, `factorial`, and `log`.

- **Calculation History Management:**  
  Uses Pandas to log every calculation into a CSV file. Supports saving, loading, clearing, and deleting history.

- **Logging:**  
  Logs detailed application events, errors, and data manipulations. Logs are written to a file (`applog.log`) and the log level is configurable via environment variables.

- **Design Patterns:**  
    - Command Pattern: Each calculator operation is encapsulated in its own command class (e.g., AddCommand, SubtractCommand, etc.), all implementing an execute() method, ([app/commands/basic_commands.py](https://github.com/TanushriVijay12/midterm1/blob/master/app/commands/basic_commands.py)). 
    - Facade Pattern: A simplified interface that hides the complexity of underlying data manipulations.The history manager module wraps complex Pandas operations (loading, saving, and clearing history) into simple methods.([HistoryManager](https://github.com/TanushriVijay12/midterm1/blob/master/app/history_manager.py)) 
    - Factory/Strategy-like Approach: Plugin system - A dynamic method for extending application functionality without changing core code. New commands are "registered" via plugins. (implemented in [PluginManager](https://github.com/TanushriVijay12/midterm1/blob/master/app/plugin_manager.py))
    - Singleton Pattern (Implicit): Ensures a class has only one instance. While not explicitly implemented as a separate Singleton class, the logging configuration in [app/main.py](https://github.com/TanushriVijay12/midterm1/blob/master/app/main.py) is initialized once and behaves similarly to a Singleton, ensuring consistent logging throughout the application.

- **Environment Variables:**  
  The application loads configuration values (such as `LOG_LEVEL`) from environment variables using `python-dotenv` ([app/main.py](https://github.com/TanushriVijay12/midterm1/blob/master/app/main.py)). This approach allows secure and dynamic configuration without hardcoding sensitive data.

- **Logging:**  
  A comprehensive logging system is set up in [app/main.py](https://github.com/TanushriVijay12/midterm1/blob/master/app/main.py) using Python’s logging module. Logs are written to `applog.log` and include detailed messages with timestamps and severity levels, aiding in monitoring and debugging.

- **Exception Handling:**  
  The code uses try/except blocks to handle errors gracefully, following both the EAFP and LBYL philosophies. Input is validated before operations, and errors (such as conversion failures or invalid operations) are caught and logged ([app/main.py](https://github.com/TanushriVijay12/midterm1/blob/master/app/main.py))


## Setup and Installation

### Prerequisites
- Python 3.10 (or later)
- pip

### Steps to Set Up
1. **Clone the Repository:**
    git clone https://github.com/TanushriVijay12/midterm1.git
    cd midterm1
2. Create and Activate a Virtual Environment
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
     Ensure your requirements.txt is up-to-date (it should include packages like pandas, pytest, python-dotenv, etc.)
    pip install -r requirements.txt
4. Set Up Environment Variables
    Create a .env file in the project root (this file is listed in .gitignore):
    LOCAL_ENV=development
    LOG_LEVEL=DEBUG

5. Configure GitHub Actions
    A workflow file is located in .github/workflows/python-app.yml that automatically runs tests and linting on every push and pull request.


## Application Execution

### Run application by executing:
python -m app.main

### Sample commands:
add 3 2
sqrt 16
greet_plugin Alice
export_csv export_history.csv
log 2.71828
log 100 10

## Testing and Continuous Integration

### Local testing
1. pytest
2. pytest --pylint
3. pytest --pylint --cov

### Github Actions
A GitHub Actions workflow is configured in .github/workflows/python-app.yml



