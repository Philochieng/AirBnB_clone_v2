from flask import Flask, render_template
from models import storage
import os

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database session after each request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display HBNB filters."""
    states = sorted(storage.all("State").values(), key=lambda s: s.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda a: a.name)
    cities = sorted(storage.all("City").values(), key=lambda c: c.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities, cities=cities)


if __name__ == "__main__":
    os.system("cp web_static/styles/3-footer.css web_flask/static/styles/")
    os.system("cp web_static/styles/3-header.css web_flask/static/styles/")
    os.system("cp web_static/styles/4-common.css web_flask/static/styles/")
    os.system("cp web_static/styles/6-filters.css web_flask/static/styles/")
    os.system("cp web_static/images/icon.png web_flask/static/images/")
    os.system("cp web_static/images/logo.png web_flask/static/images/")
    app.run(host='0.0.0.0', port=5000)

