import requests
import json
import psycopg2
from pprint import pprint

db_params = {
    'database': 'oy_5_exam',
    'user': 'postgres',
    'password': 'google_0330',
    'host': 'localhost',
    'port': 5432}




# -- DBS '6_savol'
class DBConnect:
    def __init__(self, db_params):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**db_params)

        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

        if self.cur:
            self.cur.close()





# -- Create Table '1_savol'

# with DBConnect(db_params) as (conn, cur):
#     create_table_products_query = """create table products(
#     id bigserial primary key,
#     name varchar(150) not null,
#     price varchar(150) not null,
#     color varchar(200) not null,
#     image varchar(200))"""
#
#     cur.execute(create_table_products_query)
#     conn.commit()





# -- insert_product '2_savol'

# with DBConnect(db_params) as (conn, cur):
#     insert_product_query = '''insert into products(name, price, color, image)
#     values('Macbook', '$1200.00', 'Grey', 'https://')'''
#     cur.execute(insert_product_query)
#     conn.commit()


# -- select_all_products '2_savol'

# with DBConnect(db_params) as (conn, cur):
#     select_data_query = '''select * from products'''
#     cur.execute(select_data_query)
#     products_info = cur.fetchall()
#     pprint(products_info)
#     conn.commit()


# -- update_product '2_savol'

# with DBConnect(db_params) as (conn, cur):
#     update_query = '''update products set price = '$1300.00' where id = 1;'''
#     cur.execute(update_query)
#     conn.commit()


# -- delete_product '2_savol'

# with DBConnect(db_params) as (conn, cur):
#         delete_query = f"""delete from products where id = 1"""
#         cur.execute(delete_query)
#         conn.commit()





# -- save() '5_savol'

# class Products:

#     def save(name, price , color, image):

#         with DBConnect(db_params) as (conn, cur):
#             insert_product_query = '''insert into products(name, price, color, image)
#             values(%s, %s, %s, %s)'''
#             values = (name, price, color, image)
#             cur.execute(insert_product_query, values)
#             conn.commit()
#
# Products.save('Samsung', '$300.00', 'White', 'https://.')






# -- save from url '7_savol'


# -- Create Table

# with DBConnect(db_params) as (conn, cur):
#     create_table_book_query = """create table products_2(
#     id int not null,
#     title varchar(500) not null unique,
#     description varchar(500) not null unique,
#     category varchar(500) not null,
#     price float,
#     weight int);"""
#     cur.execute(create_table_book_query)
#     conn.commit()






# -- save from url to json file

# def download_file(url, filename):
#     response = requests.get(url)
#     with open(filename, 'w') as f:
#         json.dump(response.json(), f, indent=4)
# download_file("https://dummyjson.com/products/", "main.json")


# -- Get Data from json

# with open('main.json', 'r') as f:
#     data = json.load(f)
#     products_info = data['products']


# -- insert data

# with DBConnect(db_params) as (conn, cur):
#
#     insert = f"""insert into products_2(id, title, description, category, price,weight)
#             values (%s, %s, %s, %s, %s, %s)"""
#
#     for products in products_info:
#         values = (products['id'], products['title'], products['description'],
#                products['category'], products['price'], products['weight'])
#
#         cur.execute(insert, values)
#         conn.commit()