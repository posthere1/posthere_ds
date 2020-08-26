
import basilica
import pandas as pd
import category_encoders

def predict_subreddit(text, num_pred):
    proba = pd.Series(rand_search.predict_proba(text)[0])
    proba = subreddit_df['Subreddit'].unique()
    prediction = (pd.Series(proba).sort_values(ascending=False)).reset_index(drop=True)
    if num_pred > 1:
        return prediction[:num_pred]
    else:
        return prediction[:1]

class upvote_predictor:
    def __init__(self, model,):
        self.model = model
    def prepare_string(self, string, pca):
        embedding = None
        with basilica.Connection('370a60d1-2938-b1bf-d813-0cb6954f5a0e') as c:
            embedding = c.embed_sentence(
                string,
                model='reddit',
                timeout=120
                )
        df = pd.Series(embedding)
        df = pd.DataFrame(df).T
        df = pd.Series(df)
        df = pd.DataFrame(df).T
        return df
    def predict(self, title, text, subreddit):
        title = self.prepare_string(title, self.title_pca)
        text = self.prepare_string(text, self.text_pca)
        embeddings = pd.concat([title, text], axis = 1)
        embeddings.columns = [i for i in range(1536)]
        df = pd.concat([subreddit, embeddings], axis=1)
        return int(self.model.predict(df)[0])

