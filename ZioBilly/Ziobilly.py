from gtts import gTTS
from gtts.tokenizer import PreProcessorRegex, PreProcessorSub, symbols, RegexBuilder
import PyPDF2

#Name of the files
pdf_file = 'Prova'
mp3_file = 'Ziobilly'

# Insert the path to your PDF file
pdf_path = f'/Users/andrea/Library/Mobile Documents/com~apple~CloudDocs/Python/Ziobilly/{pdf_file}.pdf'

# Create a PdfFileReader object using 'with' statement
with open(pdf_path, 'rb') as file:
    pdfreader = PyPDF2.PdfReader(file)

    # Iterate through the pages using len(reader.pages)
    for page_num in range(len(pdfreader.pages)):
        # Extract text from each page
        text = pdfreader.pages[page_num].extract_text()

        # PyPDF2 Post-processing
        def replace_ligatures(text: str) -> str:
            ligatures ={
                "ﬀ": "ff",
                "ﬁ": "fi",
                "ﬂ": "fl",
                "ﬃ": "ffi",
                "ﬄ": "ffl",
                "ﬅ": "ft",
                "ﬆ": "st",
                # "Ꜳ": "AA",
                # "Æ": "AE",
                "ꜳ": "aa",
            }
            for search, replace in ligatures.items():
                text = text.replace(search, replace)
            return text
        
        # Clean the text
        clean_text = text.strip().replace('\n', ' ')

        # Add Tone marks, commas, colons, other punctuation
        def tone_marks(text):
            return PreProcessorRegex(
                search_args=symbols.TONE_MARKS,
                search_func=lambda x: u"(?<={})".format(x),
                repl="",
            ).run(text)
        def period_comma():
            return RegexBuilder(
                pattern_args=symbols.PERIOD_COMMA,
                pattern_func=lambda x: r"(?<!\.[a-z]){} ".format(x),
            ).regex
        def colon():
            return RegexBuilder(
                pattern_args=symbols.COLON, pattern_func=lambda x: r"(?<!\d){}".format(x)
            ).regex
        def other_punctuation():
            punc = "".join(
                set(symbols.ALL_PUNC)
                - set(symbols.TONE_MARKS)
                - set(symbols.PERIOD_COMMA)
                - set(symbols.COLON)
            )
            return RegexBuilder(pattern_args=punc, pattern_func=lambda x: u"{}".format(x)).regex
        
        # Apply formatting functions
        clean_text = replace_ligatures(clean_text)
        clean_text = tone_marks(clean_text)
        #clean_text = period_comma().sub(" ", clean_text)
        clean_text = colon().sub(" ", clean_text)
        clean_text = other_punctuation().sub("", clean_text)
        print(clean_text)

        # Save each page's text to a separate mp3 file using gTTS
        mp3_file_path = f'/Users/andrea/Library/Mobile Documents/com~apple~CloudDocs/Python/Ziobilly/{mp3_file}_page_{page_num + 1}.mp3'
        tts = gTTS(clean_text, lang='it', tld='it')
        tts.save(mp3_file_path)


    print("Conversion complete.")

