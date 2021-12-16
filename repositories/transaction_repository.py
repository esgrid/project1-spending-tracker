# importing all the repositories and models (clases) to connect the front end with the database

from db.run_sql import run_sql
from models.transactions import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id, fecha, description) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id, transaction.fecha, transaction.comments]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    results = run_sql("SELECT * FROM transactions")
    return [Transaction(r['amount'], tag_repository.select(r['tag_id']), merchant_repository.select(r['merchant_id']), r['fecha'], r['description'], r['id']) for r in results]

def select(id):
    transaction = None
    result = run_sql("SELECT * FROM transactions WHERE id = %s", [id])[0]
    if result is not None:
        transaction = Transaction(result['amount'], tag_repository.select(result['tag_id']), merchant_repository.select(result['merchant_id']), result['fecha'], result['description'], result['id'])
    return transaction

def update(transaction):
    sql = 'UPDATE transactions SET (amount, merchant_id, tag_id, fecha, description) = (%s, %s, %s, %s, %s) WHERE id = %s'
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id, transaction.fecha, transaction.comments, transaction.id]
    run_sql(sql, values)

def delete_all():
    run_sql("DELETE FROM transactions")

def delete(id):
    run_sql("DELETE FROM transactions WHERE id = %s", [id])