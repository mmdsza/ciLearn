from flask import Flask, request, jsonify

def create_app():
    """Creates and configures a Flask application instance."""
    app = Flask(__name__)

    @app.route('/')
    def home():
        """Serves the homepage."""
        return jsonify({"status": "ok"}), 200

    @app.route('/echo', methods=['POST'])
    def echo():
        """Echoes a 'message' from a JSON payload."""
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.get_json()
        message = data.get('message')

        if not message:
            return jsonify({"error": "Missing 'message' field"}), 400

        return jsonify({"echo": message}), 200

    @app.route('/add/<a>/<b>')
    def add(a, b):
        """Adds two numbers from the URL path and returns the sum."""
        try:
            result = int(a) + int(b)
            return jsonify({"sum": result}), 200
        except ValueError:
            return jsonify({"error": "Inputs must be integers"}), 400

    return app