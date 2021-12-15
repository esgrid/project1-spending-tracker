from flask import Flask, render_template, redirect, Blueprint, request

from models.transactions import Transaction

from datetime import date

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.budget_repository as budget_repository

transactions_blueprint = Blueprint('transactions', __name__)

@transactions_blueprint.route('/transactions')
def transactions():
    transactions = transaction_repository.select_all()
    return render_template('transactions/index.html', transactions = transactions)

# The route GETS something (the id)
@transactions_blueprint.route('/transactions/<id>')
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template('/transactions/show.html', transaction = transaction)

# # The route GETS something -- not needed if the form is in the index
# @transactions_blueprint.route('/transactions/new', methods = ['GET'])
# def new_transaction():
#     merchants = merchant_repository.select_all()
#     tags = tag_repository.select_all()
#     return render_template('transactions/new.html', merchants = merchants, tags = tags)

# The route POSTS something to be CREATED
@transactions_blueprint.route('/transactions', methods = ['POST'])
def create_transaction():
    form = request.form
    amount = form['amount']
    merchant = merchant_repository.select(form['merchant_id'])
    tag = tag_repository.select(form['tag_id'])
    when_original = [int(x) for x in form['fecha'].split('-')]
    when = date(when_original[0], when_original[1], when_original[2])
    comments = form['comments']
    transaction = Transaction(amount, tag, merchant, when, comments)
    transaction_repository.save(transaction)
    return redirect('/transactions')

# The route gets something to be EDITED
@transactions_blueprint.route('/transaction/edit/<id>', methods = ['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template('/transactions/edit.html', transaction = transaction, merchants = merchants, tags = tags)

# The route POSTS something to be UPDATED
@transactions_blueprint.route('/transactions/<id>', methods = ['POST'])
def update_transaction(id):
    form = request.form
    amount = form['amount']
    merchant = merchant_repository.select(form['merchant_id'])
    tag = tag_repository.select(form['tag_id'])
    when_original = [int(x) for x in form['fecha'].split('-')]
    when = date(when_original[0], when_original[1], when_original[2])
    comments = form['comments']
    transaction = Transaction(amount, tag, merchant, when, comments, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')

# The route POSTS something to be DELETED
@transactions_blueprint.route('/transactions/delete/<id>', methods = ['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transaction')