from flask import Flask
from config import Config
from extensions import db, jwt, cors
from routes.auth_routes import auth_bp
from routes.ocr_routes import ocr_bp
from routes.subjects import subjects_bp
from routes.exams import exams_bp 
from routes.questions import questions_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(ocr_bp)
    app.register_blueprint(subjects_bp)
    app.register_blueprint(exams_bp)   
    app.register_blueprint(questions_bp)
    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    print("Jelo")
    app.run(debug=True)
