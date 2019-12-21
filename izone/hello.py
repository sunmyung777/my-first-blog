from flask import Flask, render_template,url_for
app=Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/profile')
def profile():
	return render_template('main_profile.html')

@app.route('/image')
def image():
	return render_template('main_image.html')

@app.route('/video')
def video():
	return render_template('main_video.html')
	
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

if __name__ == '__main__':
	app.run(debug=True)