from google.oauth2 import id_token
from google.auth.transport import requests
from flask_cors import cross_origin
from flask import current_app as app
from flask import request, jsonify

from application.database import db

from flask_security import login_user, current_user



@app.route('/api/google-signin', methods=['POST'])
@cross_origin()
def google_signin():
    data = request.json
    token = data.get('gcode', {}).get('credential')
    if not token:
        return jsonify({'success': False, 'error': 'Token not provided'}), 400

    try:
        # Specify the CLIENT_ID of the app that accesses the backend
        CLIENT_ID = '788845846356-e34ued6ntmj3t4l2417nm5hmvrefsrna.apps.googleusercontent.com'
        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), CLIENT_ID)

        # ID token is valid. Get the user's Google Account info
        email = idinfo['email']
        first_name = idinfo['given_name']
        last_name = idinfo['family_name']
        profile_picture = idinfo['picture']
        print(email, first_name, last_name, profile_picture)

        # Check if the user already exists
        user = app.security.datastore.find_user(email=email)
        if not user:
            # Create a new user if not exists
            user = app.security.datastore.create_user(
                email=email,
                username=first_name,
                password="123456",
                active=True
            )
            db.session.commit()
            if user.email == '21f1005675@ds.study.iitm.ac.in':
                app.security.datastore.add_role_to_user(user=user, role='instructor')
            else:
                app.security.datastore.add_role_to_user(user=user, role='user')
            db.session.commit()

        # Log the user in
        login_user(user)

        userDetails = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name
        }

        response_data = {
            'success': True,
            'user_data': userDetails,
            'token': current_user.get_auth_token(),
            'role': user.roles[0].name,
            'user_id': current_user.id 
        }

        return jsonify(response_data), 200
    except ValueError as e:
        # Invalid token
        return jsonify({'success': False, 'error': str(e)}), 400
