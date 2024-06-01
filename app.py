from flask import Flask, request, jsonify, json, render_template
import requests
from currency_API import CurrencyAPI
from validator import Validator

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_currency_form():
    return render_template('currency_rate_form.html')


@app.route('/getCurrRate/<date>/', methods=['GET'])
def get_currency_information_by_date(date):
    if not Validator.is_valid_date(date):
        return render_template('currency_rate_form.html', error_message_date_code = "Wrong date, please try again")
    params = {'ondate': date, 'periodicity': 0}
    try:
        response = requests.get(CurrencyAPI.target_url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


@app.route('/getCurrRateByDateCurCode', methods=['GET'])
def get_currency_information_by_date_and_code():
    date = request.args.get('date')
    cur_id = request.args.get('cur_id')
    if not Validator.is_valid_date(date):
        return render_template('currency_rate_form.html', error_message_date_code = "Wrong date, please try again")
    target_url = CurrencyAPI.target_url + '/' + str(cur_id).upper()
    params = {'ondate': date, 'periodicity': 0, 'parammode': 2}
    try:
        response = requests.get(target_url, params=params)
        response.raise_for_status()
        response_json = response.json()
        rate_date_curr_id = {'Cur_Abbreviation': response_json.get('Cur_Abbreviation'),
                             'Date': response_json.get('Date')[:10], 'Cur_Scale': response_json.get('Cur_Scale'),
                             'Cur_OfficialRate': response_json.get('Cur_OfficialRate')}
        return render_template('currency_rate_form.html', rate_date_curr_id=rate_date_curr_id)
    except requests.exceptions.HTTPError as http_err:
        error_message = f'HTTP error occurred: {http_err}'
        if http_err.response.status_code == 404:
            error_message = 'Currency data not found. Please check the date and currency code.'
        return render_template('currency_rate_form.html', error_message_date_code=error_message)

    except requests.exceptions.ConnectionError:
        error_message = 'Connection error. Please check your network connection and try again.'
        return render_template('currency_rate_form.html', error_message_date_code=error_message)

    except requests.exceptions.Timeout:
        error_message = 'The request timed out. Please try again later.'
        return render_template('currency_rate_form.html', error_message_date_code=error_message)

    except requests.exceptions.RequestException as e:
        error_message = f'An error occurred: {e}'
        return render_template('currency_rate_form.html', error_message_date_code=error_message)


if __name__ == '__main__':
    app.run()
