# app2.py
# from tutorial: https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

from flask import Flask, request

app = Flask(__name__)

@app.route("/query-example")
def query_example():
	language = request.args.get('language')
	framework = request.args.get('framework')
	website = request.args.get('website')

	return '''<h1>The language is: {} </h1>
			<h1>The framework is: {} </h1>
			<h1>The website is {} </h1>'''.format(language, framework, website)




@app.route("/form-example", methods=['GET', 'POST'])
def form_example():
	if request.method == 'POST':
		language = request.form.get('language')
		framework = request.form['framework']


		return '''<h1>The language value is: {}</h1>
				<h1>The framework value is {}</h1>'''.format(language, framework)


	return '''<form method="POST">
		Language: <input type="text" name="language"><br>
		Framework: <input type="text" name="framework"><br>
		<input type="submit" value="Submit"><br>
	</form>'''

@app.route("/json-example")
def json_example():
	return "To do.."

if __name__ == "__main__":
	app.run(debug=True, port=5000)