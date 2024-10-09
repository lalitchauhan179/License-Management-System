from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import datetime, timedelta
from auth import auth
app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///licenses.db'
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Change this!
db = SQLAlchemy(app)
jwt = JWTManager(app)

from models import License

# License validation route
@app.route('/license/validate', methods=['POST'])
def validate_license():
    license_key = request.json.get('license_key', None)
    license = License.query.filter_by(key=license_key).first()

    if not license or license.status != 'active':
        return jsonify({"message": "License invalid or inactive"}), 400

    return jsonify({"message": "License valid"}), 200

# License activation route
@app.route('/license/activate', methods=['POST'])
@jwt_required()
def activate_license():
    license_key = request.json.get('license_key', None)
    license = License.query.filter_by(key=license_key).first()

    if not license:
        return jsonify({"message": "License not found"}), 404

    license.status = 'active'
    db.session.commit()
    return jsonify({"message": "License activated successfully"}), 200

# License revocation route
@app.route('/license/revoke', methods=['POST'])
@jwt_required()
def revoke_license():
    license_key = request.json.get('license_key', None)
    license = License.query.filter_by(key=license_key).first()

    if not license:
        return jsonify({"message": "License not found"}), 404

    license.status = 'revoked'
    db.session.commit()
    return jsonify({"message": "License revoked successfully"}), 200

# Run server
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


# Register the auth blueprint
app.register_blueprint(auth, url_prefix='/auth')

# Now, any request needing admin privileges can be protected with @jwt_required()
