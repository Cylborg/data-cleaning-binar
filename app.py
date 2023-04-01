#import library yang dibutuhkan
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import pandas as pd
import re
import sqlite3
import json

#buat instance dari flask
app = Flask(__name__)

#konfigurasi untuk swagger-ui
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Documentation"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# endpoint 1 untuk membersihkan file
@app.route('/api/clean_file', methods=['POST'])
def clean_file()-> dict:
    file = request.files['file']
    df = pd.read_csv(file, encoding='latin-1')
    df = df.apply(lambda x: x.str.lower() if x.dtype == 'object' else x)
    df = df.apply(lambda x: x.str.replace('[^a-zA-Z\s]', '') if x.dtype == 'object' else x)
    df = df.apply(lambda x: x.str.replace(r'\b\w{1,3}\b', '') if x.dtype == 'object' else x)
    df = df.apply(lambda x: x.str.replace(r'\b\w{15,}\b', '') if x.dtype == 'object' else x)
    df = df.apply(lambda x: x.str.replace(r'\s+', ' ') if x.dtype == 'object' else x)
    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    if 'tweet' in df.columns:
        # normalisasi kolom teks
        df['tweet'] = df['tweet'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', ' ', x))
        
        # menghapus kata 'user' pada teks
        df = df.apply(lambda x: x.str.replace('user', '') if x.dtype == 'object' else x)

        
        # membaca kamus kata kasar
        with open('abusive.csv', 'r', encoding='latin-1') as f:
            abusive_dict = {line.strip():'' for line in f}
    
        # normalisasi teks dan menghapus kata kasar
        with open('new_kamusalay.csv', 'r', encoding='latin-1') as f:
            kamus_dict = {}
            for line in f:
                line = line.strip()
                if not line:
                    continue
                split_line = line.split(':')
                if len(split_line) != 2:
                    continue
                kamus_dict[split_line[0]] = split_line[1]

        
        df['tweet'] = df['tweet'].apply(lambda x: ' '.join([kamus_dict[word] if word in kamus_dict else word for word in x.split() if word not in abusive_dict]))
    
 
        # simpan output ke dalam file CSV
        df.to_csv('cleaned_data.csv', index=False)

        # simpan output ke dalam database SQLite
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        
        # check jika tabel sudah ada sebelumnya
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cleaned_texts'")
        table_exists = c.fetchone()
        
        # buat tabel jika tidak ada
        if not table_exists:
            c.execute('''CREATE TABLE cleaned_texts (text text)''')
        
        # memasukkan hasil cleansing kedalam database SQlite
        for text in df['tweet']:
            c.execute("INSERT INTO cleaned_texts (text) VALUES (?)", (text,))
        conn.commit()
        conn.close()
        

    return {'status': 'success', 'message': 'Data telah berhasil dibersihkan dan disimpan di database dan file CSV.', 'file_path': '/path/to/cleaned_file.csv'}



 
# endpoint 2 untuk membersihkan text
@app.route('/api/clean_text', methods=['POST'])
def clean_text():
    # cek apakah request mengirimkan data teks
    if request.content_type == 'application/x-www-form-urlencoded':
        text = request.form.get('text')
    else:
        return jsonify({'error': 'Invalid content type.'}), 400
        
    if not text:
        return jsonify({'error': 'No text provided.'}), 400

    
    # membaca kamus kata kasar
    with open('abusive.csv', 'r', encoding='latin-1') as f:
        abusive_dict = {line.strip():'' for line in f}
    
    # membaca kamus kata normalisasi
    with open('new_kamusalay.csv', 'r', encoding='latin-1') as f:
        kamus_dict = {}
        for line in f:
            line = line.strip()
            if not line:
                continue
            split_line = line.split(':')
            if len(split_line) != 2:
                continue
            kamus_dict[split_line[0]] = split_line[1]
    
    # membersihkan teks
    text = text.lower()
    text = re.sub(r'RT', '', text) # menghapus RT
    text = re.sub(r'@\S+', '', text) # menghapus username
    text = re.sub(r'http\S+', '', text) # menghapus URL
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) # menghapus punctuation
    text = re.sub(r'\d+', '', text) # menghapus angka
    words = text.split()
    new_words = []
    for word in words:
        # abaikan kata-kata kasar
        if word in abusive_dict:
            continue
        # ganti kata-kata dalam kamus
        if word in kamus_dict:
            new_words.append(kamus_dict[word])
        else:
            new_words.append(word)
    
    # gabungkan kembali kata-kata menjadi teks baru
    new_text = ' '.join(new_words)
    
    # simpan hasil ke dalam database SQLite
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    
    # check jika tabel sudah ada sebelumnya
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cleaned_texts'")
    table_exists = c.fetchone()
    
    # buat tabel jika tidak ada
    if not table_exists:
        c.execute('''CREATE TABLE cleaned_texts (text text)''')
    
    # memasukkan hasil cleansing kedalam database SQlite
    c.execute("INSERT INTO cleaned_texts (text) VALUES (?)", (new_text,))
    conn.commit()
    conn.close()
    
    return jsonify({'clean_text': new_text})

if __name__ == '__main__':
    app.debug = True
    app.run()