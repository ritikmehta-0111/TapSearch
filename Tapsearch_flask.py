from flask import Flask, request, jsonify

app = Flask(__name__)

indexed_document = {}
word_inverted_index = {}

@app.route('/')
def start():
    return "Hey There"

@app.route('/index',methods=['POST'])
def index():
    all_documents = request.form['paragraph_data']
    all_documents = all_documents.lower().split('\n')

    index = 1

    for document in all_documents:
        print(document)
        indexed_document[index] = document
        
        words = document.split(' ')
        unique_words = list(set(words))
        for word in unique_words:
            if word not in word_inverted_index:
                word_inverted_index[word] = list()
            word_inverted_index[word].append(index)
            
        index = index + 1

    #print(indexed_document)
    #print(word_inverted_index)
    return "Index created"

@app.route('/search',methods=['POST'])
def search():
    query_word = request.form['query'].lower()
    if query_word in word_inverted_index:
        result = word_inverted_index[query_word]
        return "Word found in paragraph " + ' , '.join([str(elem) for elem in result[:10]])
        
    return "word not found"

@app.route('/clear',methods=['POST'])
def clear():
    indexed_document.clear()
    word_inverted_index.clear()
    return "Index deleted"

if __name__ == '__main__':
    app.run()