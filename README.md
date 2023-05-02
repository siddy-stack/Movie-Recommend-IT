# Movie-recommendation
You can set up the file via :

mkdir -p  ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

To run the app :
web: sh setup.sh && streamlit run app.py

You can get dataset from here :
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
