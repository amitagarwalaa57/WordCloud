import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud,STOPWORDS

x=str(input("Enter the title: "))
title = wikipedia.search(x)[0]
page=wikipedia.page(title)
text=page.content
print(text)
background=np.array(Image.open("black.jpg"))
stopwords=set(STOPWORDS)
wcld=WordCloud(background_color="white",max_words=200,mask=background,stopwords=stopwords)
wcld.generate(text)
wcld.to_file("6.jpg")

