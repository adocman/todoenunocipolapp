from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

def nube(palabras):
    nube = WordCloud().generate(palabras)

    plt.imshow(nube, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    imagen = nube.to_image()

    return imagen

    