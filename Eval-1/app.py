from flask import Flask, render_template, request


app = Flask(__name__)


data = {}



@app.route('/', methods=['GET', 'POST'])
def addPost():
  if request.method == 'POST':
    data['title'] = request.form['title']
    data['content'] = request.form['content']
    return render_template('index.html', data=data)
  return render_template('index.html', data=data)


@app.route('/delete/<int:id>', methods=['DELETE'])
def deletePost():
  if id in data.keys:
    del data[id]
    return "Deleted"
  return "Not found"


if __name__ == '__main__':
  app.run(debug=True)