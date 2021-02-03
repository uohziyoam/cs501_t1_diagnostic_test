# project/server/user/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

user_blueprint = Blueprint('user', __name__)

class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def post(self):
    	responseObject = {
    		'status': 'success',
    		'message': 'Request successful but please send an HTTP GET request to register the user.'
    	}
    	return make_response(jsonify(responseObject)), 201

    def get(self):
        user = db.session.query(User).all()
        users_list = []
        for u in user:
            user_email = u.email
            users_list.append(user_email)
        
        responseObject = {
            'users': users_list
        }

        return  jsonify(responseObject), 201


# define the API resources
registration_view = RegisterAPI.as_view('register_api')

# add Rules for API Endpoints
user_blueprint.add_url_rule(
    '/user/index',
    view_func=registration_view,
    methods=['POST', 'GET']
)