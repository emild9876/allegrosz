from flask import Flask, g


def create_app():
    allegrosz = Flask(__name__)

    allegrosz.config.from_object('allegrosz.config.DevelopmentConfig')

    from .vievs import bp_main
    from .vievs import bp_item

    allegrosz.register_blueprint(bp_main)
    allegrosz.register_blueprint(bp_item)

    @allegrosz.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    return allegrosz
