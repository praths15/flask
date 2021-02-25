"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template


@app.route("/")
def home():
    """Landing page."""
    return render_template(
        "index.jinja2",
        title="Percephone Demo UI",
        description="Embed Plotly Dash into your Flask applications.",
        template="home-template",
        body="This is a homepage",
    )

#decorators
@app.route('/main')
def main():
    return render_template('main.jinja2', title='Campaigns')
