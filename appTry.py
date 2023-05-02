import pickle

import pandas as pd
import requests
import streamlit as st


def fetching_poster(movie_id):
    responses = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=ad1d3de6c4245f70e1200766abe9fba8&language=en-US".format(movie_id))
    data = responses.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity_list[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetching_poster(movie_id))
    return recommended_movie, recommended_movie_posters


movies_list = pickle.load(open("archive/movie_dict_1.pkl", "rb"))
similarity_list = pickle.load(
    open("archive/similarity1.pkl", "rb"))
movies = pd.DataFrame(movies_list)

st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    'Select a movie to find recommendation?',
    movies['title'].values)


if st.button("Recommend"):
    recommended_movie, recommended_movie_posters = Recommend(
        selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_movie_posters[4])
