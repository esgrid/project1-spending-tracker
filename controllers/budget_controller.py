from flask import Flask, render_template, redirect, Blueprint, request

from models.budget import Budget, Tracking

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.budget_repository as budget_repository

budget_blueprint = Blueprint('budget', __name__)

# @budget_blueprint.route('/budget')
# def budget():
#     budget = budget_repository.select_all()
#     return render_template('/', budget = budget)

@budget_blueprint.route('/budget', methods = ['POST'])
def create_budget():
    form = request.form
    amount = form['budget']
    budget = budget_repository.save(Budget(amount))
    return render_template('/index.html', budget = budget)

@budget_blueprint.route('/budget/<id>', methods = ['POST'])
def change_budget(id):
    form = request.form
    budget_repository.update(Budget(form['budget'], id))
    budget = budget_repository.select(id)
    return render_template('/index.html', budget = budget)

