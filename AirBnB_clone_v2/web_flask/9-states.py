from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Display a list of states."""
    states = sorted(storage.all("State").values(), key=lambda s: s.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_details(id):
    """Display details of a specific state."""
    state = storage.get("State", id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

