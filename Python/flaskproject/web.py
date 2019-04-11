from flask import Flask
app=Flask(__name__) #special type of variable 
@app.route("/")
def greeting():
	return"<h1 style='color:green'> Hello world! </h1>"
if __name__ == "__main__":
	app.run(host='127.0.0.1',debug=True)
	
