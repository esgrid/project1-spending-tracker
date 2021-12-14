from flask import Flask, render_template

from controllers.merchant_controller import merchants_blueprint
from controllers.tag_controller import tags_blueprint
from controllers.transaction_controller import transactions_blueprint
from controllers.budget_controller import budget_blueprint

import repositories.budget_repository as budget_repository

app = Flask(__name__)

app.register_blueprint(budget_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(transactions_blueprint)

@app.route('/')
def home():
    try:
        budget = budget_repository.select_all()[0]
    except:
        budget = ''

    return render_template('index.html', budget = budget)

if __name__ == '__main__':
    app.run(debug = True)