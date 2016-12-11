import logging
from flask import Flask, request


def create_app(config_filename = None):
    app = Flask(__name__, instance_relative_config = True)
    print app.instance_path
    if app.config.from_pyfile("settings.conf"):
        print "Settings loaded from local instance"
    if app.config["DEBUG"]:
        app.debug = True

    log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    root_logger = logging.getLogger("werkzeug")
    if app.config["DEBUG"]:
        root_logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    from extensions import db
    import models
    db.init_app(app)
    models.create_all(app)

    from views import views_bp
    app.register_blueprint(views_bp)
    return app


if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
