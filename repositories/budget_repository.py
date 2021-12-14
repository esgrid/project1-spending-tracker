from db.run_sql import run_sql

from models.budget import Budget

def save(budget):
    results = run_sql('INSERT INTO budget (alloted) VALUES (%s) RETURNING id', [budget.alloted])
    budget.id = results[0]['id']
    return budget

def select_all():
    results = run_sql("SELECT * FROM budget")
    return [Budget(r['alloted'], r['id']) for r in results]

def select(id):
    budget = None
    result = run_sql("SELECT * FROM budget WHERE id = %s", [id])[0]
    if result is not None:
        budget = Budget(result['alloted'], result['id'])
    return budget

# def transactions(merchant):
#     results = run_sql('SELECT * FROM transactions WHERE tag_id = %s', [merchant.id])
#     return [Transaction(r['amount'], tag_repository.select(r['tag_id']), merchant.id, r['fecha'], r['comments'], r['id']) for r in results]

def update(budget):
    sql = 'UPDATE budget SET alloted = %s WHERE id = %s'
    values = [budget.alloted, budget.id]
    run_sql(sql, values)

def delete(id):
    run_sql("DELETE FROM budget WHERE id = %s", [id])

def delete_all():
    run_sql("DELETE FROM budget")