from flask import Blueprint, jsonify, request

blue_result = Blueprint("result", __name__, url_prefix="/result")