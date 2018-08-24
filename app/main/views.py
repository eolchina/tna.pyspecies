from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .forms import NameForm, TaxonForm, DisForm, IucnForm
from .. import db
from ..models import User, Role, TaxonomicTerm, IucnCategory, ScientificName, CommonName

# from flask_boostrap import Bootstrap


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    return render_template('index.html', form=form, current_time=datetime.utcnow())
    # form = NameForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('.index'))
    #     return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())
    #

@main.route('/taxon', methods=['GET', 'POST'])
def list():
    form = TaxonForm()
    taxa = TaxonomicTerm.query.all()
    return render_template('taxon.html', form=form, taxa=taxa)

@main.route('/browse/scientific_name', methods=['GET', 'POST'])
def scientific_name_list():
    form = TaxonForm()
    scientific_names = ScientificName.query.all()
    return render_template('scientific_names_list.html', form=form, scientific_names=scientific_names)

@main.route('/browse/common_name', methods=['GET', 'POST'])
def common_name_list():
    page = request.args.get('page', 1, type=int)
    pagination = CommonName.query.order_by(CommonName.common_name.asc()).paginate(page, per_page=30, error_out=False)
    common_names = pagination.items
    return render_template('common_names_list.html', common_names=common_names, pagination=pagination)

@main.route('/dis', methods=['GET', 'POST'])
def dis():
    form = DisForm()
    return render_template('distribution.html', form=form)


@main.route('/iucn', methods=['GET', 'POST'])
def iucn():
    form = T=IucnForm()
    return render_template('iucn.html', form=form)
