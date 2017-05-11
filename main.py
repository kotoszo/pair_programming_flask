from flask import Flask, request, render_template, url_for

app = Flask(__name__)

counted_post = 0
counted_get = 0
counted_delete = 0
counted_put = 0

counts = {
    "get_counts": counted_get,
    "post_counts": counted_post,
    "put_counts": counted_put,
    "delete_counts": counted_delete
}


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    global counts, counted_delete, counted_get, counted_post, counted_put
    if request.method == 'GET':
        counted_get += 1
        counts.update({"get_counts": counted_get})
    elif request.method == 'POST':
        counted_post += 1
        counts.update({"post_counts": counted_post})
    elif request.method == 'PUT':
        counted_put += 1
        counts.update({"put_counts": counted_put})

    elif request.method == 'DELETE':
        counted_delete += 1
        counts.update({"delete_counts": counted_delete})
    print(counts)
    return render_template('index.html', count=counts)


if __name__ == '__main__':
    app.run(debug=True)
