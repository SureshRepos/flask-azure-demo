from flask import Flask, render_template, request

app = Flask('app')

QUOTES = {
  "a":"That has sort of an oak-y afterbirth.",
  "b": "Wikipedia is the best thing ever. Anyone in the world can write anything they want about any subject so you know you are getting the best possible information.",
  "c": "I learned a while back that if I do not text 911, people do not return my calls. Um, but people always return my calls because they think that something horrible has happened.",
  "d": "I’m an early bird and I’m a night owl so I’m wise and I have worms."
}


@app.route("/")
def home():
  name = request.args.get("name")
  return render_template("index.html", name=name)

@app.route("/scott")
def scott():
  context = {}
  name = request.args.get("name")
  context["name"] = name
  context["words"] = get_words(name)
  return render_template("scott.html", context=context)

def get_words(name):
  words = []
  for letter in name:
    # words.append(QUOTES[letter])
    if letter in QUOTES:
      words.append(QUOTES[letter])
  return words

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8000)