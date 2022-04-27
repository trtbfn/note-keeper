import sqlite3
import logging
from typing import Tuple, List
import uuid

#Wrapper for database
class DBManager:
	def __init__(self, name: str='notes.db') -> None:
		self.name = name

		#Create table and start note if there not notes
		self._create_table()
		self._create_start_note()
		
	def _create_start_note(self):
		notes = self.get_all()
		if len(notes) == 0:
			self.write(
				'Welcome!',
				'You can sketch your ideas right here!'
			)
			

	#Wrapper for some functions
	def _exec_handler(self, query: str, 
				params: Tuple,
				err_message: str=''):

		try:
			with sqlite3.connect(self.name) as conn:
				crsr = conn.cursor()
				crsr.execute(query, params)
				conn.commit()

		except sqlite3.Error as e:
				logging.error(err_message, e)



	def drop_table(self):
		self._exec_handler("""
      			DROP TABLE IF NOT EXISTS notes
			""",
			(),
			"Table haven't been droped"
    	)

	
	def write(self, title: str, text: str):

		#Using string image of uuid.uuid4 instance as id
		self._exec_handler("""
      			INSERT INTO notes(id, title, text)
				VALUES (?, ?, ?)
			""",
			(str(uuid.uuid4()), title, text),
			"Table haven't been droped",
    	)


	def delete(self, id: str):
		print('trying to delte')
		self._exec_handler(f"""
      	DELETE FROM notes WHERE {id=}
			""",
			(),
			"Value hasn't been deleated."
    	)


	def get(self, id: str) -> Tuple[str, str, str] | None:

		note = None

		try:
			with sqlite3.connect(self.name) as conn:
				crsr = conn.cursor()

				crsr.execute(f"""
					SELECT * FROM notes WHERE {id=}
				""")

				conn.commit()

				note = crsr.fetchone()

		except sqlite3.Error as e:
			logging.error("Value hasn't been got.", e)

		#return (id, title, text)
		return note


	def get_all(self) -> List[Tuple[str, str, str]] | None:

		note = None

		try:
			with sqlite3.connect(self.name) as conn:
				
				crsr = conn.cursor()

				crsr.execute(f"""
					SELECT * FROM notes 
				""")

				conn.commit()

				note = crsr.fetchall()

		except sqlite3.Error as e:
			logging.error("Values have't been got.", e)

		return note


	def _create_table(self):

		self._exec_handler("""
				CREATE TABLE IF NOT EXISTS notes (
				id TEXT PRIMARY KEY NOT NULL,
				title TEXT CHECK(length(title) <= 256),
				text TEXT CHECK(length(text) <= 1024)			
      		);
    	""",
		(),
      "Table haven't been created"
    )


	def drop_table(self):

		self._exec_handler("""
				DROP TABLE IF NOT EXISTS notes
			""",
			(),
			"Table hasn't been droped"
    	)

	
	def update(self, id: str, title: str, text: str):
		
		self._exec_handler("""
				UPDATE notes
				SET title = ?,
					text = ?
				WHERE id = ?
			""",
			(title, text, id),
			"Note haven't been udpated"
    	)

# db = DBManager()
# db.write("asdfasdkfllsdfjl", "kasjdflksdjflad;kfasdkflladfj")
# db.write("asdfasdkfllsdfjl", "kasjdflksdjflad;kfasdkflladfj")
# db.write("asdfasdkfllsdfjl", "kasjdflksdjflad;kfasdkflladfj")
# db.write("asdfasdkfllsdfjl", "kasjdflksdjflad;kfasdkflladfj")
# db.write("asdfasdkfllsdfjl", "kasjdflksdjflad;kfasdkflladfj")
# db.write("asdfasdkfllsdfjl", "kasjdflksdjflad;kfasdkflladfj")