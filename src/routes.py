from flask import request, jsonify
from src.email_utils import send_email

def register_routes(app, s):
    @app.route('/')
    def run():
        return "Server is running.."

    @app.route('/signup', methods=['POST'])
    def signup():
        email = request.json.get('email')
        username = request.json.get('username')

        if not email or not username:
            return jsonify({"message": "Email and Username are required"}), 400

        # Generate a verification token for the email
        token = s.dumps(email, salt='email-confirm')

        # Create the verification link
        verification_link = f'http://localhost:5000/verify/{token}'

        # Send verification email
        send_email(
            subject='Confirm Your Email',
            recipient=email,
            body=f'Hello! {username}:),\n\nPlease click the link to verify your email: {verification_link}'
        )

        return jsonify({"message": "Verification email sent!"}), 200

    @app.route('/verify/<token>', methods=['GET'])
    def verify_email(token):
        try:
            email = s.loads(token, salt='email-confirm', max_age=3600)
            send_email(
                subject="Welcome to Payppy:)",
                recipient=email,
                body="Thank you for verifying your email! We're glad to have you."
            )
            return jsonify({"message": "Email verified successfully!"}), 200
        except Exception:
            return jsonify({"message": "The verification link is invalid or has expired."}), 400
