import pyttsx3,PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open('/Users/andreapassetti/Documents/Python/book.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#name mp3 file whatever you would like
speaker.save_to_file(clean_text, '/Users/andreapassetti/Documents/Python/story.mp3')
speaker.runAndWait()

speaker.stop()
