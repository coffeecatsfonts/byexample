from flask import Flask, render_template, request
from once_upon_a_project.config import return_database_connection, add_example, fetchall_examples

app = Flask(__name__)
conn, cur = return_database_connection()
app.config.update(dict(SECRET_KEY="powerful secretkey", WTF_CSRF_SECRET_KEY="a csrf secret key"))
app.config.from_object('once_upon_a_project.config')


def rowify(text):
    rowed_text = []
    while (text.partition('\r\n')[1]) != '':
        line, partition, text = text.partition('\r\n')
        rowed_text.append('{}{}'.format(line, partition))
    rowed_text.append(text)
    return rowed_text


def translate_hashtags(rowed_text_v1):
    for index, content in enumerate(rowed_text_v1):
        if content.strip() == '#':
            rowed_text_v1[index] = '<hr>'
        elif content.startswith('#####'):
            rowed_text_v1[index] = '<h5>' + content + '</h5><br><hr><br>'
        elif content.startswith('####'):
            rowed_text_v1[index] = '<h4>' + content + '</h4>'
        elif content.startswith('###'):
            rowed_text_v1[index] = '<h3>' + content + '</h3>'
        elif content.startswith('##'):
            rowed_text_v1[index] = '<h2>' + content + '</h2>'
        elif content.startswith('#'):
            rowed_text_v1[index] = '<h1>' + content + '</h1>'
        return rowed_text_v1


def turn_into_code_sections(rowed_text_v2):
    for index, content in enumerate(rowed_text_v2):
        if content.strip() == '':
            next_index = index + 1
            if rowed_text_v2[next_index].startswith('\t') or rowed_text_v2[next_index].startswith('    '):
                rowed_text_v2[next_index] = '<div class=\'code_me\'>{}'.format(rowed_text_v2[next_index])
                end_codeblock(next_index + 1, rowed_text_v2)


def end_codeblock(next_index, rowed_text_v2):
    for index, content in enumerate(rowed_text_v2[next_index:]):
        if (rowed_text_v2[next_index].startswith('\t') or rowed_text_v2[next_index].startswith('    ')) is False:
            rowed_text_v2[index] = '{}</div>'.format(rowed_text_v2[index])
            return rowed_text_v2


def derowify(rowed_text_md):
    text = ''
    for row in rowed_text_md:
        text = text + row
    return text


@app.route('/add_example', methods=['GET', 'POST'])
def add_example_frontend():
    return render_template('example_form.html')


@app.route('/index', methods=['GET', 'POST'])
def view_examples():
    if request.method == 'POST':
        rowed_text = rowify(request.form['text'])
        rowed_text_md_pt_one = translate_hashtags(rowed_text)
        rowed_text_md_pt_two = translate_empty lines(rowed_text_md_pt_one)
        text_md = derowify(rowed_text_md_pt_one)
        add_example(conn, cur, request.form['title'], text_md)
    examples = fetchall_examples(cur)
    return render_template('index.html', examples=examples)


if __name__ == "__main__":
    app.run()
