from app import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, name, users):
        self.name = name
        self.users = users

    def __repr__(self):
        return '<Role % r>' % self.name


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User % r>' % self.username


class TaxonomicTerm(db.Model):
    """docstring for TaxonomicTerm"""
    __tablename__ = 'taxonomic_terms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    iucn_category_id = db.Column(db.Integer, db.ForeignKey('iucn_categories.id'))

    def __repr__(self):
        return '<TaxonomicTerm %r>' % self.name


class IucnCategory(db.Model):
    """docstring for IucnCategory"""
    __tablename__ = 'iucn_categories'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(), unique=True)
    taxonomic_terms = db.relationship('TaxonomicTerm', backref='iucn_category', lazy='dynamic')

    def __repr__(self):
        return '<IucnCategory %r>' % self.category


class ScientificName(db.Model):
    __tablename__ = 'scientific_names'

    id = db.Column(db.Integer, primary_key=True)
    name_code = db.Column(db.String(), primary_key=True)
    web_site = db.Column(db.Text())
    genus = db.Column(db.String())
    genus_c = db.Column(db.String())
    species = db.Column(db.String())
    species_c = db.Column(db.String())
    infraspecies = db.Column(db.String())
    infraspecies2 = db.Column(db.String())
    infraspecies_c = db.Column(db.String())
    infraspecies_c2 = db.Column(db.String())
    infraspecies_marker = db.Column(db.String())
    infraspecies_marker2 = db.Column(db.String())
    author = db.Column(db.String())
    author2 = db.Column(db.String())
    accepted_name_code = db.Column(db.String())
    comment = db.Column(db.Text())
    scrutiny_date = db.Column(db.Text())
    sp2000_status_id = db.Column(db.Integer())
    databases_id = db.Column(db.String())
    specialist_id = db.Column(db.String())
    family_id = db.Column(db.String())
    is_accepted_name = db.Column(db.Integer())
    genus_c_py = db.Column(db.String())
    species_c_py = db.Column(db.String())
    infraspecies_c_py = db.Column(db.String())
    infraspecies_c_py2 = db.Column(db.String())
    genuswithsubgenus = db.Column(db.String())
    specialist_code = db.Column(db.String())
    family_code = db.Column(db.String())
    canonical_name = db.Column(db.String())
    comments = db.Column(db.String())

    def __repr__(self):
        return '<ScientificName %r>' % self.canonical_name


class CommonName(db.Model):
    """docstring for CommonName"""

    __tablename__ = 'common_names'

    id = db.Column('record_id', db.String, primary_key=True)
    name_code = db.Column(db.String())
    common_name = db.Column(db.String())
    language = db.Column(db.String())
    country = db.Column(db.String())
    database_id = db.Column(db.String())
    is_infraspecies = db.Column(db.Integer)
    common_name_py = db.Column(db.String())
    reference_code = db.Column(db.String())

    def __repr__(self):
        return '<CommonName %r>' % self.common_name
