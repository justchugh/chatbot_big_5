
import numpy as np
import pandas as pd
import nltk
import pickle
from sklearn.feature_extraction.text import CountVectorizer

dataframe = pd.read_csv('newanswers.csv', index_col=False, header=None)
x_train = dataframe[0].values

contractions = {
    "ain't": "am not",
    "aren't": "are not",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'll": "he will",
    "he's": "he is",
    "I'd": "I would",
    "I'll": "I will",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it's": "it is",
    "let's": "let us",
    "shouldn't": "should not",
    "that's": "that is",
    "there's": "there is",
    "they'd": "they would",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'll": "we will",
    "we're": "we are",
    "weren't": "were not",
    "what's": "what is",
    "where's": "where is",
    "who's": "who is",
    "won't": "will not",
    "wouldn't": "would not",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are"
}

def expand_contractions(text):
    words = text.split()
    expanded_text = [contractions[word] if word in contractions else word for word in words]
    return " ".join(expanded_text)

def clean_text(text):
    lemmatizer = nltk.WordNetLemmatizer()
    text = expand_contractions(text)
    tokens = nltk.word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    stop_words = set(nltk.corpus.stopwords.words('english')) - {'no', 'not', 'nor'}
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return " ".join(lemmatized_tokens)

def prepare_texts(texts):
    return [clean_text(text) for text in texts]

def vectorize_texts(train_texts, test_texts):
    vectorizer = CountVectorizer(ngram_range=(1, 2))
    train_vec = vectorizer.fit_transform(train_texts).toarray()
    test_vec = vectorizer.transform(test_texts).toarray()
    return test_vec

def load_model(filename='finalized_model.sav'):
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    return model

def predict_labels(test_vec):
    model = load_model()
    return model.predict(test_vec)

def generate_labels(test_texts):
    clean_train_texts = prepare_texts(x_train)
    clean_test_texts = prepare_texts(test_texts)
    test_vectors = vectorize_texts(clean_train_texts, clean_test_texts)
    predictions = predict_labels(test_vectors)
    return predictions

# Example usage:
# x_test = ['I keep care of not leaving my belongings anywhere',
#           'I try to not leave things anywhere',
#           "I don't think strongly about this",
#           'I am too lazy so I sometimes leave things around',
#           'I always leave things around']
# print(generate_labels(x_test))
