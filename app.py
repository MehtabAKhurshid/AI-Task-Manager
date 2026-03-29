from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Read the task from the submitted form
        task_text = request.form.get("task", "").strip()
        if task_text:
            tasks.append(task_text)
        return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)