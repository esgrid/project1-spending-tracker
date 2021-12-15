from flask import Flask, Blueprint, render_template, request, redirect
import repositories.merchant_repository as merchant_repository
from models.merchants import Merchant

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/index.html', merchants = merchants)

# To be able to show all the transactions to this merchant besides the details of the merchant
@merchants_blueprint.route('/merchants/<id>')
def show_merchant(id):
    merchant = merchant_repository.select(id)
    transactions = merchant_repository.transactions(merchant)
    return render_template('merchants/show.html', merchant = merchant, transactions = transactions)

@merchants_blueprint.route('/merchants', methods = ['POST'])
def create_merchant():
    form = request.form
    active = True if 'active' in form else False
    merchant_repository.save(Merchant(form['name'], active))
    return redirect('/merchants')

@merchants_blueprint.route('/merchants/edit/<id>', methods = ['POST'])
def update_merchant(id):
    form = request.form
    name = form['name']
    active = True if 'active' in form else False
    merchant_repository.update(Merchant(name, active, id))
    return redirect(f'/merchants/{id}')

