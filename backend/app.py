from flask import Flask, send_from_directory
import os

def create_app():
    app = Flask(__name__, static_folder='../frontend/build')

    @app.route('/')
    def serve():
        return send_from_directory(app.static_folder, 'index.html')

    @app.errorhandler(404)
    def not_found(e):
        return send_from_directory(app.static_folder, 'index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5001)