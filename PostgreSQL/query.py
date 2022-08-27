import psycopg2
from psycopg2 import Error

def main():
	print("Hi")
	
	try:
		connection = psycopg2.connect(user="postgres",
								   password="m09128360159",
								   host="localhost",
								   port="5432",
								   database="postgre_db")
		cursor = connection.cursor()
		print("Connected succesfuly")

		# Query 1
		# return tasks by ascending deadline order
		cursor.execute("SELECT * FROM task ORDER BY DEADLINE;")
		print(cursor.fetchall())

		# Query 2
		# return sum of task prices for each user
		cursor.execute("SELECT id, owner, SUM(price) FROM task GROUP BY owner;")
		print(cursor.fetchall())

		# Query 3
		# for every user that younger than 18 set is_active FALSE
		cursor.execute("UPDATE user SET is_active = 1")
		cursor.execute("UPDATE SELECT * FROM people WHERE age < 18 SET is_active = 0;")
		print(cursor.fetchall())

		
		connection.commit()

		if connection:
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

	except (Exception, Error) as error:
  		print("Error while connecting to PostgreSQL", error)

main()
