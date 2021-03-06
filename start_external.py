import os
from lookup.flask_app import create_app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.debug = True
    app.run(host='0.0.0.0', port=port)
