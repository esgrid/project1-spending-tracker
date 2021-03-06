from db.run_sql import run_sql

from models.merchants import Merchant
from models.transactions import Transaction
import repositories.tag_repository as tag_repository

def save(merchant):
    results = run_sql('INSERT INTO merchants (name, active) VALUES (%s, %s) RETURNING id', [merchant.name, merchant.active])
    merchant.id = results[0]['id']
    return merchant

def select_all():
    results = run_sql("SELECT * FROM merchants")
    return [Merchant(r['name'], r['active'], r['id']) for r in results]

def select(id):
    merchant = None
    result = run_sql("SELECT * FROM merchants WHERE id = %s", [id])[0]
    if result is not None:
        merchant = Merchant(result['name'], result['active'], result['id'])
    return merchant

def transactions(merchant):
    results = run_sql('SELECT * FROM transactions WHERE merchant_id = %s', [merchant.id])
    return [Transaction(r['amount'], tag_repository.select(r['tag_id']), merchant, r['fecha'], r['description'], r['id']) for r in results]

def update(merchant):
    sql = 'UPDATE merchants SET (name, active) = (%s, %s) WHERE id = %s'
    values = [merchant.name, merchant.active, merchant.id]
    run_sql(sql, values)

def delete_all():
    run_sql("DELETE FROM merchants")

def delete(id):
    run_sql("DELETE FROM merchants WHERE id = %s", [id])