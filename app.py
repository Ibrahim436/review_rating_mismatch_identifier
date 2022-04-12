from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from werkzeug.utils import secure_filename
import pandas as pd
import csv
import os

from core.model import Predict

predicter=Predict()

app=Flask(__name__)
app.config['SECRET_KEY']='supersecretkey'
app.config['UPLOAD_FOLDER']='static/files'

class UploadFileForm(FlaskForm):
    file=FileField("File")
    submit=SubmitField("Upload File")

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def index():
    form=UploadFileForm()
    if form.validate_on_submit():
        file=form.file.data
        save_path=os.path.join(os.path.abspath(''),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
        file.save(save_path)
        result=predicter.predict(save_path)
        return render_template('data.html',data=result.to_html())
    return render_template('index.html',form=form)

if __name__=='__main__':
    app.run(debug=False)
