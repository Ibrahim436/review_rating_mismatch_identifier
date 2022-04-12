# review_rating_mismatch_identifier
An app where a csv will be uploaded and it will detect if the reviews in "Text" column does not match the rating given  in "Star"

### Please find the colab link which was used to train BERT model for for chrome app reviews for sentiment classification :
  https://colab.research.google.com/drive/1RtDjTsGCX9uanlgFmNv2ITjsXZQ-PKsT?usp=sharing
  
### Running on your local

1. Clone the repository : git clone https://github.com/Ibrahim436/review_rating_mismatch_identifier.git
2. install modules by running : pip install -r requirements.txt (file contains tensorflow-cpu which was added to reduce the slug size for the app to run on Heroku.Replace it with tesnorflow when you run on local )
3. Go to the repo folder in your local and run : python app.py

