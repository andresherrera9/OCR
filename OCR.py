from PIL import Image
import pytesseract

#Funcion elemental para el desarrolo de la aplicacion por medio de Django.


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

print(ocr_core(<"Path to file">)

