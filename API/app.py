from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud_example.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/items', methods=['GET', 'POST'])
def items():
    with app.app_context():
        if request.method == 'GET':
            items = Item.query.all()
            items_list = [{'id': item.id, 'name': item.name} for item in items]
            return jsonify(items_list)
        elif request.method == 'POST':
            data = request.json
            new_item = Item(name=data['name'])
            db.session.add(new_item)
            db.session.commit()
            return jsonify({'message': 'Item created successfully'})

@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def item(item_id):
    with app.app_context():
        item = Item.query.get_or_404(item_id)

        if request.method == 'GET':
            return jsonify({'id': item.id, 'name': item.name})
        elif request.method == 'PUT':
            data = request.json
            item.name = data['name']
            db.session.commit()
            return jsonify({'message': 'Item updated successfully'})
        elif request.method == 'DELETE':
            db.session.delete(item)
            db.session.commit()
            return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
