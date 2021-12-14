import pdb

from models.merchants import Merchant
from models.tags import Tag
from models.budget import Budget
from models.transactions import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.budget_repository as budget_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()
budget_repository.delete_all()


for i in range(3):
    merchant_repository.save(Merchant('Merchant ' + str(i), True if i % 2 == 0 else False))

tags = ['groceries', 'travel', 'entertainment', 'books', 'take aways', 'gadgets']

for t in tags:
    tag_repository.save(Tag(t.capitalize, True if tags.index(i) % 2 == 2 else False))