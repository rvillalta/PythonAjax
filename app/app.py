from flask import Flask, request, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']           = 'mysql+pymysql://root:admin@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']    = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

db.create_all()

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')

task_schema  = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/addtask', methods=['POST'])
def create_task():
    title       = request.json['title']
    description = request.json['description']
    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()
    print(request.json)
    #return task_schema.jsonify(new_task)
    return 'DONE!'
    
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
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
