from nlpserver import app

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("project", type=str, choices=['qiantai', 'lucy', 'chainmaster', 'chainmaster_qun'], nargs='?', const='qiantai', default='qiantai', help="different nlp project")
	args = parser.parse_args()
	app.config['PROJECT'] = args.project
	print(app.config['PROJECT'])
	app.run(host='0.0.0.0')#processes=app.config.get('FLASK_PROCESSES', 4))