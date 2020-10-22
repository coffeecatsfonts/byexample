from flask import Flask, render_template, request
from once_upon_a_project.config import return_database_connection, add_example, fetchall_examples

app = Flask(__name__)
conn, cur = return_database_connection()
app.config.update(dict(SECRET_KEY="powerful secretkey", WTF_CSRF_SECRET_KEY="a csrf secret key"))
app.config.from_object('once_upon_a_project.config')


def markdownify(text):
  for i in text:
    print(i)
  return text
  

@app.route('/index', methods=['GET', 'POST'])
def view_examples(): # rename me, here and in index.html
  if request.method == 'POST':
    title = '{}'.format(request.form['title'])
    text = '{}'.format(request.form['text'])
    text_md = markdownify(request.form['text'])
    add_example(conn, cur, title, text)
  examples = fetchall_examples(cur)
  return render_template('index.html', examples=examples)
  
if __name__== '__main__':
  app.run()
