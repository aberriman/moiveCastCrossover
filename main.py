import streamlit as st

from utils.imdb_request import get_movie_id, get_cast_list, intersect_of_casts, make_actor_dict


def main():
    st.text_input("Movie 1", key="movie_id1")
    st.text_input("Movie 1", key="movie_id2")
    st.text_input("IMDB API key", key="key")

    movie1 = st.session_state.movie_id1
    movie2 = st.session_state.movie_id2
    key = st.session_state.key

    if st.button("search"):
        movie1_id = get_movie_id(movie1, key)
        movie2_id = get_movie_id(movie2, key)

        cast_list_dict_1, movie_cast_1 = get_cast_list(movie1_id, key)
        cast_list_dict_2, movie_cast_2 = get_cast_list(movie2_id, key)

        intersect = intersect_of_casts(movie_cast_1, movie_cast_2)
        st.write(intersect)

        actor_information = make_actor_dict(intersect, cast_list_dict_1, cast_list_dict_2)
        st.write(actor_information)


if __name__ == '__main__':
    main()
