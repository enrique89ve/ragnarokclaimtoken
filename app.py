from ast import Not
from flask import Flask, render_template, jsonify, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from form import consulta
import json
import requests 
import re
import json
import time 
from valid import username_is_valid, username_ready

import configparser, os

node = 'https://inconceivable.hivehoneycomb.com/'



app = Flask(__name__)



def accountapi(ac):

    
    urlapi = node+"@"+ac
    reponse = requests.get(urlapi)
    data = reponse.json()


    return data




@app.route('/', methods=["GET", "POST"])
def claim():


    


    try:

        if request.method == 'POST':
            time.sleep(30)
            return render_template( "base.html")
            

            

        

        else:
            


            

        
        

            

            return render_template( "base.html")

           

    
        

        
    except (UnboundLocalError):

        return render_template("base.html")



@app.route('/stats', methods=["GET", "POST"])
def stats():

    try:
        form = consulta(request.form)


            
        
        if request.method == 'POST' and form.validate():

            

            userconsulta = request.form['username']

        


            if userconsulta is None:
                pass
            
            else:
                ac = userconsulta.isnumeric()

                
            
            if ac is False:

            
                ac = userconsulta


                if not username_is_valid(ac):

                    return render_template("statsext.html", error = "invalid user" ) 

                    

                    

                else:


                    if not username_is_valid(ac) and not username_ready:


                        

                        pass
                        

            
                    else: 
                        data = accountapi(ac)


                        balance = data['balance']

                        tokens = balance/1000

                        drop = data['drop']

                        snap = drop['availible']





                        cantidad = snap['amount']/1000

                        if cantidad == 0:

                            reclamados = "Already claimed"

                            datos  = (" @%s your balance %s DUAT / %s" % (ac, tokens, reclamados,  ))

                        else: 
                            reclamados = cantidad
                    

                            datos  = (" @%s your balance: %s DUAT / Pending to claim %s Tokens" % (ac, tokens, reclamados,  ))

                        datos = datos

            return render_template("statsext.html", datos = datos)

        return render_template("stats.html")
    except (UnboundLocalError):

        return render_template("stats.html", form = form)
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('base.html'), 404
        






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)