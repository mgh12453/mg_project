import psycopg2
from psycopg2 import Error
from faker import Faker

class cmd:

	class create:
		user =      '''CREATE TABLE people(
					ID    	 INT PRIMARY KEY NOT NULL,
				 	NAME  	 TEXT,
				 	AGE   	 INT,
				 	EMAIL 	 TEXT);'''

		task =      '''CREATE TABLE task(
					ID      INT PRIMARY KEY NOT NULL,
				 	TITLE  	 TEXT,
				 	DEADLINE INT,
				 	PRICE	 INT,
				 	OWNER     TEXT);'''

		friendship= '''CREATE TABLE friendship AS SELECT NAME FROM people;'''

	def insert(self, table=None, id=None, name=None, age=None, email=None, title=None, deadline=None, price=None, user=None):
		user_insert 	  = f"INSERT INTO people (ID,NAME,AGE,EMAIL) VALUES ({id}, '{name}', {age}, '{email}');"
		task_insert 	  = f"INSERT INTO task (ID,TITLE,DEADLINE,PRICE,OWNER) VALUES ({id}, '{title}', {deadline}, {price}, '{user}');"
		friendship_insert = f"ALTER TABLE friendship ADD {name} bit;"
		if table == 'user': return user_insert
		if table == 'task': return task_insert
		if table == 'friendship': return friendship_insert



def main():
	print("Hi")
	
	try:
		f = Faker();
		command = cmd()
		connection = psycopg2.connect(user="postgres",
								   password="m09128360159",
								   host="localhost",
								   port="5432",
								   database="postgre_db")
		cursor = connection.cursor()
		print("Connected succesfuly")
		cursor.execute("DROP SCHEMA public CASCADE;")
		connection.commit()
		cursor.execute("CREATE SCHEMA public;")
		connection.commit()
		print("database cleared succesfuly")

		# Creating user table and cash their name
		cursor.execute(command.create.user)
		connection.commit()
		user_tmp = set()
		while len(user_tmp) < 1000:
			tmp = f.name()
			tmp = tmp.replace(' ','')
			tmp = tmp.replace('.','')
			user_tmp.add(tmp)
		count = 1
		for tmp in user_tmp:
			cursor.execute(command.insert(table='user', id=count, name=tmp, age=f.random_int(min=5, max=70), email=f.email()))
			count += 1
		connection.commit()

		# Creating task table
		cursor.execute(command.create.task)
		connection.commit()

		# Creating friendship table
		cursor.execute(command.create.friendship)
		for st in user_tmp:
			cursor.execute(command.insert(table='friendship', name=st))
		connection.commit()


		if connection:
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

	except Error as error:
		print("Error while connecting to PostgreSQL", error)
	except Exception as error:
		print("Compilation Error: ", error)

main()

