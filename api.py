from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()