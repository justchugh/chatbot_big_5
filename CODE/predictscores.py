
import numpy as np
import pandas as pd
import nltk
import pickle

dataframe = pd.read_csv('newanswers.csv', index_col=False, header=None)
x_train = dataframe[0].values

contractions = {
    "ain't": "am not",
    "aren't": "are not",
    "can't": "cannot",
    "could've": "could have",
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
    "it'd": "it would",
    "it'll": "it will",
    "it's": "it is",
    "let's": "let us",
    "might've": "might have",
    "mightn't": "might not",
    "must've": "must have",
    "mustn't": "must not",
    "o'clock": "of the clock",
    "should've": "should have",
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
    "we've": "we have",
    "weren't": "were not",
    "what's": "what is",
    "where's": "where is",
    "who's": "who is",
    "won't": "will not",
    "would've": "would have",
    "wouldn't": "would not",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have"
}

def replace_contractions(text):
    words = text.split()
    replaced_text = [contractions[word] if word in contractions else word for word in words]
    return " ".join(replaced_text)

def preprocess_text(text):
    lemmatizer = nltk.WordNetLemmatizer()
    text = replace_contractions(text)
    tokens = nltk.word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    stop_words = set(nltk.corpus.stopwords.words('english')) - {'no', 'not', 'nor'}
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return lemmatized_tokens

def join_tokens(tokens_list):
    return [" ".join(tokens) for tokens in tokens_list]

def vectorize_text(train_texts, test_texts):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(ngram_range=(1, 2))
    x_train_vec = vectorizer.fit_transform(train_texts).toarray()
    x_test_vec = vectorizer.transform(test_texts).toarray()
    return x_test_vec

def predict_sentiment(test_vectors):
    model_filename = 'finalized_model.sav'
    with open(model_filename, 'rb') as model_file:
        model = pickle.load(model_file)
    predictions = model.predict(test_vectors)
    return predictions

def generate_labels(test_texts):
    clean_train_texts = [preprocess_text(text) for text in x_train]
    clean_train_texts = join_tokens(clean_train_texts)
    
    clean_test_texts = [preprocess_text(text) for text in test_texts]
    clean_test_texts = join_tokens(clean_test_texts)

    test_vectors = vectorize_text(clean_train_texts, clean_test_texts)

    predictions = predict_sentiment(test_vectors)
    return predictions

# Example usage:
# x_test = ['I keep care of not leaving my belongings anywhere',
#           'I try to not leave things anywhere',
#           "I don't think strongly about this",
#           'I am too lazy so I sometimes leave things around',
#           'I always leave things around']
# print(generate_labels(x_test))
