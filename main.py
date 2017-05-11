from flask import Flask, request, render_template, url_for

app = Flask(__name__)

count = 0

counts = {
    get_counts: 0,
    post_counts: 0,
    put_counts: 0,
    delete_counts: 0
}


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    global counts

    if request.methods == 'GET':
        counts.update(get_counts, count)
    elif request.methods == 'POST':
        pass
    elif request.methods == 'PUT':
        pass

    elif request.methods == 'DELETE':
        pass

    return render_template('index.html', count=count)


if __name__ == '__main__':
    app.run(debug=True)
