import docx 
x = 0
doc = docx.Document(r"C:\Users\AN515-52\Downloads\Wordflash2.docx")

DocParag = (doc.paragraphs) 

print(len(DocParag))

#for para in DocParag:
   # x = x + 1
   # print(para.text)
   # if x == 5:
   #     break
   # else:
   #     pass


# for para in DocParag:
#     x = x + 1
#     if x == 1:
#         print('q.text="{}";'.format(para.text))
#     elif x == 2:
#         print("c0.text='{}';".format(para.text))
#     elif x == 3:
#         print("c1.text='{}';".format(para.text))
#     elif x == 4:
#        print("c2.text='{}';".format(para.text))
#     elif x == 5:
#         print("c3.text='{}';".format(para.text))
#     else:
#         x = 0



for para in DocParag:
    text = para.text
    text = text.strip()
    if text == "":
        print('')
    elif text[0] == "ก":
        print("c0.text='{}';".format(para.text))
    elif text[0] == "ข":
        print("c1.text='{}';".format(para.text))
    elif text[0] == "ค":
        print("c2.text='{}';".format(para.text))
    elif text[0] == "ง":
        print("c3.text='{}';".format(para.text))
    else:
        print('q.text="{}";'.format(para.text))











