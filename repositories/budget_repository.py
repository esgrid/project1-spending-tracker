from db.run_sql import run_sql

def delete_all():
    run_sql("DELETE FROM budget")