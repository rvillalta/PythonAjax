from app import app

@app.route('/addtask', methods=['POST'])
def create_task():
    title       = request.json['title']
    description = request.json['description']
    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()
    print(request.json)
    return task_schema.jsonify(new_task)
    
    #return 'Recibido'

@app.route('/gettasks', methods=['GET'])
def getTasks():
    tasks = Task.query.all()
    return jsonify(tasks_schema.dump(tasks))

@app.route('/gettask/<id>', methods=['GET'])
def getTask(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)

@app.route('/', methods=['GET'])
def index():
    return "HELLO FLASK\n"