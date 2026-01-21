from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        note = request.form.get("note")

        if note and note.strip():
            notes.append(note)
        else:
            message = "⚠️ Please enter a valid note."

    return render_template("home.html", notes=notes, message=message)

if __name__ == "__main__":
    app.run(port=5002, debug=True)

