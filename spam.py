import pickle

classifier = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("cv-transform.pkl", "rb"))

def predict_spam(text):
    data = [text]
    vect = cv.transform(data).toarray()
    prediction = classifier.predict(vect)

    if prediction[0] == 1:
        return {
            "result": "🚫 Spam Email",
            "quote": "⚠️ Think before you click. Not everything that shines is gold.",
            "gif": "spam.gif"
        }
    else:
        return {
            "result": "✅ Not Spam",
            "quote": "😊 You’re safe! This message looks genuine.",
            "gif": "ham.gif"
        }



