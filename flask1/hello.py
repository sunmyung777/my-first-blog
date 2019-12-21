from flask import Flask, render_template, url_for
import matplotlib.pyplot as plt
import mpld3

app = Flask(__name__)

@app.route('/')
def Main():
	f = plt.figure()
	plt.plot([1,2,3], [4,5,6])
	graph = mpld3.fig_to_html(f, figid='THIS_IS_FIGID')
	g=open("templates/new.html",'w')
	g.write(graph)
	g.close()
	return render_template('main.html')

@app.route('/graph')
def graph():
	return render_template('new.html')

	
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)