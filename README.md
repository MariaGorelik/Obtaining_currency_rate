### Project Name
Currency Rate Application

### Description
The Currency Rate Application is a Flask-based web application that allows users to fetch and display currency exchange rates for a specified date. Users can either get the rate for a specific currency code or view all currency rates for a given date. The application retrieves data from an external [currency API](https://www.nbrb.by/apihelp/exrates).

### Installation
1. Clone the repository:
    ```bash  
    git clone https://github.com/MariaGorelik/Obtaining_currency_rate.git
    cd Obtaining_currency_rate
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
4. Run the Flask application:
    ```bash
    python app.py
5. Access the application:
    Open your web browser and navigate to http://127.0.0.1:5000/.
### Usage
Enter a date in the format YYYY-MM-DD to get currency rates for that date.
Optionally, enter a currency code (ISO 4217 format) to get the rate for a specific currency.
### Authors
[Maria Gorelik](https://github.com/MariaGorelik)
### Links and additional notes
[api of the National Bank of the Republic of Belarus](https://www.nbrb.by/apihelp/exrates)