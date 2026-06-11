import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext("sample_receipt.jpg")

for item in result:
    print(item[1])