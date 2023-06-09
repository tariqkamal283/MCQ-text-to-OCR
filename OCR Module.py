from PIL import Image
import pytesseract as tess
import json
tess.pytesseract.tesseract_cmd = r'Add your Tesseract-OCR\tesseract.exe Path here!'

img = Image.open('Add your image path here!')
text = tess.image_to_string(img)

lines = text.split('\n')

mcqs = []
current_mcq = {}
for line in lines:
    if line.strip().endswith('?'):
        if current_mcq:
            mcqs.append(current_mcq)
        current_mcq = {'question': line.strip(), 'options': []}
    elif current_mcq and line.strip():
        current_mcq['options'].append(line.strip())

if current_mcq:
    mcqs.append(current_mcq)

for i, mcq in enumerate(mcqs):
    print(f"Question {i+1}: {mcq['question']}")
    for j, option in enumerate(mcq['options']):
        print(f"Option {chr(ord('A')+j)}: {option}")
    print()
