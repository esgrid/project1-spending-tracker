# project1-spending-tracker
A spending tracker app. It asks for a budget from the user and it tracks the remaining budget when transactions are added. 
Transactions need a tag and a merchant, and the user can add merchants and tags and edit them and mark them as active or inactive, 
meaning that they can't be selected when adding a transaction. Transactions can be edited and deleted.

Commands to initialise:

createdb spending_tracker
psql -d spending_tracker -f db/spending_tracker.sql

Run console.py
