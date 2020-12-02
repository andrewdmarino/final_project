import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, redirect, request 
from flask_cors import CORS
from flask import render_template

engine=create_engine("sqlite:///assets/data/steam_games.db")

app=Flask(__name__)
CORS(app)

#main route is index.html with our input fields
@app.route("/passdata", methods=["GET", "POST"])
#function to run with POST data trigger from submit form
def passdata():
    if request.method == "POST":
       req = request.form

       genre = request.form.get("genre")
       tag = request.form.get("tag")
       low = request.form.get("low")
       high= request.form.get("high")
       print(req)

        #put vars into query (select * from games with score where 
        # genre=genre )

       #results=engine.execute('select * from games_with_score').fetchmany(10)
       #returned_results=[list(result) for result in results]
       #return jsonify(returned_results)

       return redirect(request.url)
    return render_template ("results.html")

@app.route("/api/v1.0/sample")
def sample():
    results=engine.execute('select * from games_with_score').fetchmany(10)
    returned_results=[list(result) for result in results]
    return jsonify(returned_results)

if __name__=="__main__":
    app.run(debug=True)