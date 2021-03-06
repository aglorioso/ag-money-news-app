import sys
import io
import csv
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)

#The next two lines help me get around encoding errors
reload(sys)
sys.setdefaultencoding('utf-8')


def get_csv():
    csv_path = './static/AG_money/caldwell_consolidates_base/final_upload/pac_contrib_aug_15_17_geo_for_upload_17_only.csv'
    csv_file = io.open(csv_path, 'rU', encoding='utf-8', errors='ignore')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    abort(404)

if __name__ == '__main__':
    #first up the Flask test server
    app.run(debug=True, use_reloader=True)