from flask import Flask, jsonify
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import render_template_string
from markupsafe import escape
import json
from flask_cors import CORS
from datasci.py import * 

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/map/precipitat",methods=['POST','GET'])
def interactive_map_p():
    # link datasci.py here

    m = precipit() 
    m.get_root().width = "800px" #pls change accordingly 
    m.get_root().height = "600px"#pls change accordingly 
    iframe = m.get_root()._repr_html_()
    return render_template_string(
        iframe=iframe,
    )

@app.route("/map/temper",methods=['POST','GET'])
def interactive_map_t():
    m = temper() #add the latitude and logntiude like: (lat,long)
    m.get_root().width= "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()
    return render_template_string(iframe=iframe)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Cheese is a dairy product produced in wide ranges of flavors, textures, and forms by coagulation of the milk protein casein. It comprises proteins and fat from milk (usually the milk of cows, buffalo, goats, or sheep). During production, milk is usually acidified and either the enzymes of rennet or bacterial enzymes with similar activity are added to cause the casein to coagulate. The solid curds are then separated from the liquid whey and pressed into finished cheese.[1] Some cheeses have aromatic molds on the rind, the outer layer, or throughout. Over a thousand types of cheese exist and are produced in various countries. Their styles, textures and flavors depend on the origin of the milk (including the animal"s diet), whether they have been pasteurized, the butterfat content, the bacteria and mold, the processing, and how long they have been aged. Herbs, spices, or wood smoke may be used as flavoring agents. The yellow to red color of many cheeses is produced by adding annatto. Other ingredients may be added to some cheeses, such as black pepper, garlic, chives, or cranberries. A cheesemonger, or specialist seller of cheeses, may have expertise with selecting, purchasing, receiving, storing and ripening cheeses.[2]')

#when you add the lat long and description, add it to the disasters.csv file 

if __name__ == '__main__':
    app.run()
