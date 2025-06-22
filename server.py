from flask import Flask, send_from_directory, make_response, request, jsonify
import os

app = Flask(__name__, static_folder=".")

def add_security_headers(response):
    """Add security headers to the response"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.route('/favicon.ico')
def favicon():
    """Return an empty response for favicon requests"""
    return '', 204

@app.route('/')
def serve_index():
    """Serve the index.html file with security headers"""
    response = make_response(send_from_directory(".", "index.html"))
    return add_security_headers(response)

@app.route('/login', methods=['POST'])
def login():
    """Handle login requests"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        # Simple authentication (for demo purposes)
        if username == 'admin' and password == 'admin':
            return jsonify({
                'status': 'success',
                'message': 'Login successful'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Invalid username or password'
            }), 401
            
    except Exception as e:
        print(f"Login error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Internal server error'
        }), 500

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files with security headers"""
    if path != 'favicon.ico':
        response = make_response(send_from_directory(".", path))
        return add_security_headers(response)
    return '', 204

if __name__ == '__main__':
    port = 8000
    print(f'Starting server on port {port}...')
    app.run(host='0.0.0.0', port=port)
