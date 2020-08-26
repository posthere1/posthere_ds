from flask import Flask
import json
from pred import upvote_predictor

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = 
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # db.init_app(app)

    @app.route('/')
    def root():
        return 'Where should you post that on reddit?'

    @app.route('/submit', methods=['GET'])
    def submit():

        return 'Enter your post here'

    @app.route('/suggestions', methods=['POST'])
    def suggestions():
        title_input = request.values['title']
        text_input = request.values['text']
        results_input = request.values['results']
        

        filename = 'Models\post_here_model.pkl'
        load_model = pickle.load(open(filename, 'rb'))
                
        # with open('Models\post_here_model.pkl', 'rb') as g:
        #     model_ph = pickle.load(g)
        # predictor_ph = post_here_predictor(model_ph)
        # predictor_ph.predict(text_input, results_input)

        # with open("Models\up_vote_model.pickle", "rb") as f:
        #     model_uv = pickle.load(f)
        # predictor_uv = upvote_predictor(model_uv)
        # predictor_uv.predict(title_input, text_input, "r/AskReddit")

        with open("model.pickle", "rb") as f:
            model = pickle.load(f)
        predictor = upvote_predictor(model)
        predictor.predict("This is a dumb title", "Text here", "r/AskReddit")

        return 'not sure how we want it displayed yet'

    return app
