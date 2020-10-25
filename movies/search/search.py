from flask import Blueprint
from flask import request, render_template, redirect, url_for, session, flash

from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, Form, StringField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

import movies.adapters.repository as repo
import movies.movie_library.movie_library as movie_library
import movies.search.services as services

search_blueprint = Blueprint(
    'search_bp', __name__)


@search_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    search = MovieSearchForm(request.form)
    if request.method != 'POST':
        pass
    else:
        return search_results(search.data['search'], search.data['select'])
    return render_template('search/search.html', form=search, title="Search Movies", description="Search movies by actor, genre or director")


@search_blueprint.route('/results')
def search_results(search, select):
    search_title = search.title()
    if services.search_exists(search_title, select, repo.repo_instance):
        if select == "Actor":
            return redirect(url_for('movie_library_bp.movies_by_actor', actor=search_title))
        elif select == "Genre":
            return redirect(url_for('movie_library_bp.movies_by_genre', genre=search_title))
        elif select == "Director":
            return redirect(url_for('movie_library_bp.movies_by_director', director=search_title))
    else:
        flash('No results found!')
        return redirect(url_for('search_bp.search'))



class MovieSearchForm(Form):
    choices = [('Actor', 'Actor'),
               ('Director', 'Director'),
               ('Genre', 'Genre')]
    select = SelectField('Search for movie:', choices=choices)
    search = StringField('')

