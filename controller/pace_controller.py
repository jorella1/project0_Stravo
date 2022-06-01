from flask import render_template
from service.pace_calculator import Pacer


def get_pace_page():
    return render_template("pace.html")

def get_results(results):

    pacer = Pacer()
    pace_results = Pacer.paceCalc(pacer,results["distance"],results["timeM"] , results["timeS"])
    return render_template("results.html", results=pace_results)



