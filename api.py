from app import app
from flask import jsonify, request

notes = [{'id': 3,
         'text': 'Make a cake'},
         {'id': 5,
         'text': 'Make a cake'},
]


@app.route('/api/get_notes', methods=['GET'])
def get_notes() -> str:
	return jsonify(notes)


@app.route('/api/add_note', methods=['POST'])
def add_note() -> str:
	post_data = request.get_json()
	notes.append({
		'id': 4,
		'text': post_data.get('text')
	})
	return jsonify('Note have been added!')


@app.route('/api/update_note', methods=['PUT'])
def update_note(note_id) -> str:
	post_data = request.get_json()
	notes.index(id)
	for note in notes:
		if note['id'] == note_id:
			note.text = post_data.get('text')
			break

	return jsonify('Note have been updated!')
