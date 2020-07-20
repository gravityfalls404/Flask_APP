from app import app

from flask import Flask, request,redirect, render_template

@app.route("/calculator",methods = ["POST","GET"])
def myCalc():
    if request.method == "POST":
        req = request.form  
        
        num1 = int(req.get('num1'))
        num2 = int(req.get('num2'))

        if req.get("operator")=="Multiply":
          res = num1*num2
        elif req.get("operator")=="Divide":
          res = num1/num2
        elif req.get("operator")=="Substract":
          res = num1-num2
        else:
          res = num1+num2

        return render_template("/public/calc.html", result=res)    
        

    return render_template("/public/calc.html")