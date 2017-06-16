#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
	Nome: API Calculadora
 	Autor: Felipe Samuel
 	Facebook: fb.me/samukajobs
 	Site: www.felipesamuel.com
 	E-mail: contato@felipesamuel.com
 	Telefone: +55 87 9 8821-4383
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calcule', methods=['POST'])
def soma():

	return jsonify({"expressao":request.get_json(), "resultado":eval(request.get_json()['expressao'])})

if __name__ == '__main__':
	app.run(port=8080, debug=True)
