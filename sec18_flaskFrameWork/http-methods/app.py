from flask import Flask, render_template, jsonify, request


PORT = 5050

app = Flask(__name__)

sampleData ={
    'name' : 'Item 1',
    'description' : 'Description 1'
}

items = [
    {
        'id' : 1, 
        'name' : 'Item 1', 
        'description' : 'Description 1'
    },
    {
        'id' : 2, 
        'name' : 'Item 2', 
        'description' : 'Description 2'
    },
    {
        'id' : 3, 
        'name' : 'Item 3', 
        'description' : 'Description 3'
    }
]

@app.route('/')
def home():
    return {
        'message' : 'Hello from reck98'
    }
    
@app.route('/items')
def getAllItems():
    return jsonify(items)


@app.route('/item/<id>', methods = ['GET'])
def item(id):
    try:
        idInt = int(id)
    except:
        return {
            'error' : 'Invalid ID'
        }
    
    
    for item in items:
        if item['id'] == int(idInt):
            return jsonify(item)
    
    return {
        'error' : 'Item not found'
    }

@app.route('/item', methods = ['POST'])
def addItem():
    if not request.is_json:
        return {
            'error' : 'Please send the data in the JSON format', 
            'sampleData' : sampleData
        }
    
    data = request.get_json(silent=True)
    print(data)
    
    if data is None or data == {}:
        return {
            'error' : 'Please send the data in the JSON format',
            'sampleData' : sampleData
        }
    
    
    if not 'name' in data or not 'description' in data or len(data) != 2:
        return {
            'error' : 'name and description are the only required fields',
            'sampleData' : sampleData
        }
    
    newItem = {
        'id' : len(items) + 1,
        'name' : request.json['name'],
        'description' : request.json['description']
    }
    
    items.append(newItem)
    return {
        'message' : 'Item added successfully',
        'item' : newItem
    }
    
    


if __name__ == "__main__":
    app.run(debug=True, port=PORT)