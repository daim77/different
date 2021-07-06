from sqlalchemy import create_engine, insert, engine
import pandas as pd


with open('/Users/martindanek/Documents/programovani/autent.txt',
          encoding='utf-8') as file:
    autent_list = eval(file.read())['raspberry']['mariadb']

user = autent_list[0]
psw = autent_list[2]

conn_string = f"mysql+pymysql://{user}:{psw}@192.168.0.199/engeto"
pi_conn = create_engine(conn_string, echo=True)

# df = pd.read_sql_query("SELECT * FROM `BX-Book-Ratings` LIMIT 5", pi_conn)
# print(df.head())

with open('/Users/martindanek/Documents/NEW_JOB_IT/DataSentics/TASK/'
          'BX-SQL-Dump/BX-Books.sql', encoding="ISO-8859-1") as sql_file:
    sql_dump = sql_file.readlines()
    for dump_line in sql_dump:
        if dump_line.strip() == '':
            continue
        # else:
        #     dump_values = dump_line.split('(')[1].split(')')[0].split("'")
        #     clean_data = []
        #     for item in dump_values:
        #         clean_data.append(item.strip(","))
        #
        #     load_dict = {
        #         'User-ID': clean_data[0],
        #         'Location': clean_data[1],
        #         'Age': clean_data[2]
        #     }
        # with engine.connect() as conn:
        #     result = conn.execute(
        #         insert('BX-Users'), [load_dict]
        #     )
        #     conn.commit()
        try:
            pi_conn.execute("dump_line")
        except:
            print(dump_line)
