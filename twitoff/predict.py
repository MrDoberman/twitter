from .models import User
from sklearn.linear_model import LogisticRegression
import numpy as np
from .twitter import vectorize_tweet



def predict_user(user0_username, user1_username, hypo_tweet_text):

    user0 = User.query.filter(User.username==user0_username).one()
    user1 = User.query.filter(User.username==user1_username).one()

 
    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    vects = np.vstack([user0_vects, user1_vects])

    labels = np.concatenate([np.zeros(len(user0.tweets)),
                              np.ones(len(user1.tweets))])


    logreg = LogisticRegression()

    logreg.fit(vects, labels)


    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text)

   
    pred = logreg.predict([hypo_tweet_vect])

    print(pred)

    return pred[0]