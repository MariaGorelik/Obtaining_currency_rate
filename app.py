from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    cur_id = 440
    target_url = f"https://api.nbrb.by/exrates/rates/{cur_id}"

    params = {'ondate': '2024-05-29', 'periodicity': 0}

    try:
        response = requests.get(target_url, params=params)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


@app.route('/<date>/') # change url
def upload_currency_information(date):
    target_url = "https://api.nbrb.by/exrates/rates"
    params = {'ondate': date, 'periodicity': 0}
    try:
        response = requests.get(target_url, params=params)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


@app.route('/<date>/<cur_id>/')
def get_currency_information(date, cur_id):
    target_url = f"https://api.nbrb.by/exrates/rates/{cur_id}"
    params = {'ondate': date, 'periodicity': 0, 'parammode': 2}
    try:
        response = requests.get(target_url, params=params)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
