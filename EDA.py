import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv('cleaned_data.csv')
df['Tweet'] = df['Tweet'].str.replace('user', '')

# menghitung jumlah tweet yang mengandung setiap label
hs_count = df['HS'].value_counts()
print(hs_count)

# Check data quality
print(df.isnull().sum())

# mengecek grafik bar untuk menampilkan jumlah tweet yang mengandung label "HS menggunakan matplotlib
plt.bar(hs_count.index, hs_count.values)
plt.title('Jumlah Tweet yang Mengandung Label HS')
plt.xlabel('HS Label')
plt.ylabel('Jumlah Tweet')
plt.show()

# mengecek grafik bar untuk menampilkan jumlah tweet yang mengandung label "HS menggunakan seaborn
sns.countplot(x='HS', data=df)
plt.title('Jumlah Tweet yang Mengandung Label HS')
plt.xlabel('HS Label')
plt.ylabel('Jumlah Tweet')
plt.ylim(0, 10000) # menyesuaikan nilai pada sumbu y agar sesuai
plt.show()

# Plot wordcloud for each label

def plot_wordcloud(label):
    words = ' '.join(df[df['HS']==label]['Tweet'].astype(str))
    wordcloud = WordCloud(width=800, height=500, random_state=42, max_font_size=100).generate(words)
    plt.figure(figsize=(10,7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.title(str(label).capitalize() + ' Wordcloud')
    plt.show()

plot_wordcloud(1) # 'hate'
plot_wordcloud(0) # 'not hate'
