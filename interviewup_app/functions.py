def handle_uploaded_file(f):  
    with open('D:/EKTA/COMPUTER ENGINEERING/SEM 6/MINI PROJECT/interviewup/static/upload', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  