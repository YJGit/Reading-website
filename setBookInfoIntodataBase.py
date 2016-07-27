# -*-coding: utf-8 -*-
from books.models import book
file_obj = open('book_info.txt', 'r', encoding = 'utf-8')
try:
    book_id1 = 0
    while True:
        lineContent = file_obj.readline()
        if lineContent:
            title1 = ''
            cover_url1 = ''
            score1 = ''
            author1 = ''
            publisher1 = ''
            translator1 = ''
            publisher_date1 = ''
            page1 = ''
            price1 = ''
            binding1 = ''
            Isbn1 = ''
            label1 = ''
            content_intro1 = ''
            directory1 = ''
            while lineContent != '\n' and lineContent:
                if title1 == '':
                    title1 = lineContent
                    if title1[len(title1) - 1] == '\n':
                        title1 = title1[:-1]
                    print(title1)
                elif cover_url1 == '':
                    cover_url1 = lineContent
                    if cover_url1[len(cover_url1) - 1] == '\n':
                        cover_url1 = cover_url1[:-1]
                    #print(cover_url1)
                elif score1 == '':
                    score1 = lineContent
                    if score1[len(score1) - 1] == '\n':
                        score1 = float(score1[:-1])
                    else:
                        score1 = float(score1)
                    #print(score1)
                elif author1 == '':
                    author1 = lineContent
                    if author1[len(author1) - 1] == '\n':
                        author1 = author1[:-1]
                    #print(author1)
                elif publisher1 == '':
                    publisher1 = lineContent
                    if publisher1[len(publisher1) - 1] == '\n':
                        publisher1 = publisher1[:-1]
                    #print(publisher1)
                elif translator1 == '':
                    translator1 = lineContent
                    if translator1[len(translator1) - 1] == '\n':
                        translator1 = translator1[:-1]
                    #print(translator1)
                elif publisher_date1 == '':
                    publisher_date1 = lineContent
                    if publisher_date1[len(publisher_date1) - 1] == '\n':
                        publisher_date1 = publisher_date1[:-1]
                    #print(publisher_date1)
                elif page1 == '':
                    page1 = lineContent
                    if page1[len(page1) - 1] == '\n':
                        page1 = page1[:-1]
                    #print(page1)
                elif price1 == '':
                    price1 = lineContent
                    if price1[len(price1) - 1] == '\n':
                        price1 = price1[:-1]
                    #print(price1)
                elif binding1 == '':
                    binding1 = lineContent
                    if binding1[len(binding1) - 1] == '\n':
                        binding1 = binding1[:-1]
                    #print(binding1)
                elif Isbn1 == '':
                    Isbn1 = lineContent
                    if Isbn1[len(Isbn1) - 1] == '\n':
                        Isbn1 = Isbn1[:-1]
                    #print(Isbn1)
                elif label1 == '':
                    label1 = lineContent
                    if label1[len(label1) - 1] == '\n':
                        label1 = label1[:-1]
                    #print(label1)
                elif content_intro1 == '':
                    content_intro1 = lineContent
                    if content_intro1[len(content_intro1) - 1] == '\n':
                        content_intro1 = content_intro1[:-1]
                    #print(content_intro1)
                elif directory1 == '':
                    directory1 = lineContent
                    if directory1[len(directory1) - 1] == '\n':
                        directory1 = directory1[:-1]
                    #print(directory1)
                lineContent = file_obj.readline()
            book_id1 += 1
            print(book_id1)
            #加入数据库
            book.objects.get_or_create(title = title1, cover_url = cover_url1, score = score1, author = author1,
                                publisher = publisher1, translator = translator1, publisher_date = publisher_date1,
                                page = page1, price = price1, binding = binding1, Isbn = Isbn1,
                                label = label1, content_intro = content_intro1, directory = directory1,
                                book_id = book_id1)
        else:
            break

finally:
    file_obj.close()