from typing import List, Tuple
from urllib import response
from app import app
from flask import jsonify, request
from models import DBManager

#Assets 
dbm = DBManager()


def fill_response(body: List[Tuple[str, str, str]] | None  =  None, 
				  status:int = 200, 
				  message:str = None):
	
	return {
		'message': message, 
		'status': status, 
		'body': body
	}


@app.route('/api/notes', methods=['GET', 'POST'])
def notes():

	response = None
	
	if request.method == 'GET':
		try: 
			response = fill_response(body=dbm.get_all(),
								status=200,
								message='Notes have been got.')

		except Exception as e:

			response = fill_response(status=500,
									message=f"Database haven't got notes. ERROR:{e}")

	elif request.method == 'POST':

		post_data = request.get_json()

		try: 
			dbm.write(
				post_data.get('title'),
				post_data.get('text')
			)

			response = fill_response(status=200, message='Ok.')

		except Exception as e:
			response = fill_response(status=500, 
									 message=f"Database haven't inserted notes. ERROR:{e}")
	
	return jsonify(response)


@app.route('/api/notes/<note_id>', methods=['PUT', 'DELETE', 'GET'])
def note(note_id):

	response = None

	try: 
		notes = dbm.get_all()

	except Exception as e:
		response = fill_response(status=500, 
								 message=f"Database haven't got notes when trying to update them. ERROR:{e}")

	if request.method == 'PUT':

		post_data = request.get_json()
	
		try: 
			dbm.update(
				note_id,
				post_data.get('title'),
				post_data.get('text')
			)

			response = fill_response(status=200, 
						 message=f'Note have been updated.')

		except Exception as e:

			response = fill_response(status=500, 
						message=f"Database have couldn't udpate note. ERROR:{e}")

			
	
	elif request.method == 'DELETE':
		for i in range(0, len(notes)):

			# 0 in tuple identifies note id
			if notes[i][0] == note_id:
				try: 
					dbm.delete(note_id)

					response = fill_response(status=200, 
								 message='Note have been deleated.')

				except Exception as e:
					response = fill_response(status=500, 
								 message=f"Database have couldn't delete note. ERROR:{e}")

	elif request.method == 'GET':
		
		try: 
			note = dbm.get(note_id)
			
			response = fill_response(body=note,
									status=200, 
									message=f"Ok!")

		except Exception as e:
			response = fill_response(status=500, 
								 message=f"Database have couldn't udpate note. ERROR:{e}")


	return jsonify(response)

