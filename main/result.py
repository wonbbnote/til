import os

from flask import Blueprint, jsonify, request

blue_result = Blueprint("result", __name__, url_prefix="/")


@blue_result.route('/result', methods=['GET'])
def result():
    filenames = os.listdir('static/img')
    


    

    
