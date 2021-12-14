from flask import Flask, Blueprint, render_template, request, redirect
import repositories.merchant_repository as merchant_repository

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

# maybe not needed -- if the form is in the index
# @merchants_blueprint.route('/merchants')
# def new_merchant():

