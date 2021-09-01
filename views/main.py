import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import random

class MainView(object):
    def __init__(self):
        self.load_data()

    def load_data(self):
        movies_df = pd.read_csv(
            'movies.csv',
            encoding='latin-1',
            skiprows=1,
            index_col=0,
            sep='\t',
            names=['movie_id', 'title', 'genres']
        )

        self.movies_list = movies_df['title'].to_list()
        self.movies_list.sort()

        users_df = pd.read_csv(
            'users.csv',
            encoding='latin-1',
            skiprows=0,
            index_col=0,
            sep='\t'
            
        )
        self.user_list = users_df['user_id'].to_list()
        self.user_list.sort()

    def render(self):
        st.title('MovieRecommender App')

        form = st.form(key='my-form')
        form.markdown('Please choose a user from the list below')
        hint_text = 'Select or type to search'
        user = form.selectbox(
            'User', 
            [ hint_text, *self.user_list ]
        )

        submit = form.form_submit_button('Submit')
        self.user_recommendations = st.empty()

        if submit:
            if hint_text in [user]:
                st.write('Please choose a user')
            else:
                self.show_prior_ratings(user)

    def show_prior_ratings(self,user):   

        random_movies = random.choices(self.movies_list, k=10)
        movie_titles = ""
        for movie_title in random_movies:
            if len(movie_titles) > 0:
                movie_titles += "\n"
            movie_titles += movie_title

        self.user_recommendations.text(movie_titles)

       