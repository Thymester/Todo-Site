from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form.get('task')
    if task_description:
        task = Task(task_description)
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_index>')
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

@app.route('/toggle_task/<int:task_index>')
def toggle_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index].completed = not tasks[task_index].completed
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
