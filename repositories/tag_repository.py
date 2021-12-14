from db.run_sql import run_sql

from models.tags import Tag
from models.transactions import Transaction
import repositories.merchant_repository as merchant_repository

def save(tag):
    results = run_sql('INSERT INTO tags (name, active) VALUES (%s, %s) RETURNING id', [tag.name, tag.active])
    tag.id = results[0]['id']
    return tag

def select_all():
    results = run_sql("SELECT * FROM tags")
    return [Tag(r['name'], r['active'], r['id']) for r in results]

def select(id):
    tag = None
    result = run_sql("SELECT * FROM tags WHERE id = %s", [id])[0]
    if result is not None:
        tag = Tag(result['name'], result['active'], result['id'])
    return tag

def transactions(tag):
    results = run_sql('SELECT * FROM transactions WHERE tag_id = %s', [tag.id])
    return [Transaction(r['amount'], tag, merchant_repository.select(r['merchant_id']), r['fecha'], r['comments'], r['id']) for r in results]

def update(tag):
    sql = 'UPDATE tags SET (name, active) = (%s, %s) WHERE id = %s'
    values = [tag.name, tag.active, tag.id]
    run_sql(sql, values)

def delete_all():
    run_sql("DELETE FROM tags")

def delete(id):
    run_sql("DELETE FROM tags WHERE id = %s", [id])