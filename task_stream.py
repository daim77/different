import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


def read_sql(sql_string):
    with open('/Users/martindanek/Documents/programovani/autent.txt',
              encoding='utf-8') as file:
        autent_list = eval(file.read())['raspberry']['mariadb']

    user = autent_list[0]
    psw = autent_list[2]

    conn_string = f"mysql+pymysql://{user}:{psw}@192.168.0.199/engeto"
    pi_conn = create_engine(conn_string, echo=True)

    return pd.read_sql_query(sql_string, pi_conn)


def recommend_book():
    pass


if __name__ == '__main__':

    basic_sql = """
            WITH b_rate AS (
            SELECT *
            FROM `BX-Book-Ratings`
            WHERE `Book-Rating` <> 0
        ), b_book AS (
            SELECT *
            FROM `BX-Books`
        )
        SELECT b_rate.`User-ID` AS id,
               b_rate.ISBN AS isbn,
               b_rate.`Book-Rating` AS rating,
               b_book.`Book-Title` AS title,
               b_book.`Book-Author` AS author,
               b_book.Publisher AS publisher,
               b_book.`Year-Of-Publication` as year,
               b_book.`Image-URL-M` AS url_image
        FROM b_rate
        JOIN b_book ON b_rate.ISBN = b_book.ISBN
        ;"""

    st.title('BOOK RECOMMENDATION TASK')
    st.balloons()
    st.markdown('__BUY BOOK__')

    df_rated_books = read_sql(basic_sql)

    option = st.selectbox(
        'Choose book:', pd.Series(df_rated_books['title']).unique().tolist()
    )

    sql_string = f"""
        SELECT *
        FROM `BX-Books`
        WHERE `Book-Title` = '{option}'
        AND `Year-Of-Publication` = (
            SELECT MAX(`Year-Of-Publication`) as max_year
            FROM `BX-Books`
            WHERE `Book-Title` = '{option}'
        );"""

    df = read_sql(sql_string)

    st.write(df)
    st.sidebar.image(f"{df['Image-URL-M'][0]}")

    isbn = df['ISBN'][0]
    sql_string = f"""
        SELECT AVG(`Book-Rating`) AS average_rating
        FROM `BX-Book-Ratings`
        WHERE `BX-Book-Ratings`.ISBN = '{isbn}'
    """
    df = read_sql(sql_string)

    st.sidebar.write('RATING')
    st.sidebar.write(f"{df['average_rating'][0]}")

    st.markdown('__Buy recommended books__')



# streamlit run task_stream.py
