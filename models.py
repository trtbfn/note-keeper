import sqlite3
import logging
from typing import Dict, Tuple, List

#Wrapper for notes db
class DB:
            
    def __init__(self, name:str='notes') -> None:
        try: 
            self.conn = sqlite3.connect(name)
        except sqlite3.Error as e:
            logging.error("Connection have not established")
            raise e

        self._create_table()


    def _exec_handler(self, query: str, sqlite3_error: sqlite3.Error,
                      err_message: str):
        crsr = self.conn.cursor()

        try:
            crsr.execute(query)
        except sqlite3_error as e:
            logging.error(err_message, e)
        finally: 
            crsr.close()
            self.conn.commit()


    def _create_table(self):
        self._exec_handler("""
                CREATE TABLE IF NOT EXIST notes (
                    id INTEGER PRIMARY KEY NOT NULL,
                    title TEXT CHECK(length(title) <= 256)
                    body TEXT CHECK(length(body) <= 1024)
                );
            """,
            sqlite3.InterfaceError,
            "Table haven't been created"
        )


    def drop_table(self):
        self._exec_handler("""
                DROP TABLE IF NOT EXIST notes
            """,
            sqlite3.InterfaceError,
            "Table haven't been droped"
        )

    def write(self, data: Dict[int: Tuple[str, str]]):
        for index, values in data:
            self._exec_handler("""
                    INSERT INTO notes
                    VALUES ({0}, {1}, {0})
                """.format(index, *values),
                sqlite3.InterfaceError,
                f"Values haven't been inserted. Strat with {index=}."
            )

        
    def delete(self, indexes: List[int]):
        for index in indexes:
            self._exec_handler(f"""
                    DELETE FROM notes WHERE id={index}
                """,
                sqlite3.InterfaceError,
                f"Values haven't been deleted. Strat with {index=}."
            )

    def get(self, indexes: List[int]):
        self._exec_handler(f"""
                        DELETE FROM notes WHERE id={index}
                    """,
                    sqlite3.InterfaceError,
                    f"Values haven't been deleted. Strat with {index=}."
        )

        
        
        
        


            
