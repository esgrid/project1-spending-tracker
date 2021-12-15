from flask import Flask, Blueprint, render_template, request, redirect
import repositories.tag_repository as tag_repository
from models.tags import Tag

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route('/tags')
def tags():
    tags = tag_repository.select_all()
    return render_template('tags/index.html', tags = tags)


# To be able to show all the transactions with this tag besides the details of the tag
@tags_blueprint.route('/tags/<id>')
def show_tag(id):
    tag = tag_repository.select(id)
    transactions = tag_repository.transactions(tag)
    return render_template('tags/show.html', tag = tag, transactions = transactions)

@tags_blueprint.route('/tags', methods = ['POST'])
def create_tag():
    form = request.form
    active = True if 'active' in form else False
    tag_repository.save(Tag(form['name'], active))
    return redirect('/tags')