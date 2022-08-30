from flask import render_template, request
from backend import make_link, get_result

def result_get():
    sl = request.args.get('sl', default='en', type=str)
    tl = request.args.get('tl', default='ko', type=str)
    text = request.args.get('text', default='hello', type=str)

    google_link, papago_link = make_link(sl, tl, text)
    google_translator = get_result(google_link)
    papago = get_result(papago_link)

    return render_template('result.html', google_translator=google_translator, papago=papago)
