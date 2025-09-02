from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello World!")
    params = {'name': "Shubham kumar" , 'age' : 20}
    return render(request, 'index.html', params)

def about(request):
    return HttpResponse("<h2>About Me</h2>")

def links(request):
    return HttpResponse('''
    <h2>Links</h2>
    <a href="https://oranbyte.com/">Oranbtye.com</a><br>
    <a href="https://polybooklib.oranbyte.com/">Polybooklib</a><br>
    <a href="https://sms.oranbyte.com/">School management system</a>
    ''')

def analyse_text(request):
    global param
    text = request.POST.get('text', '')
    removepunc = request.POST.get('remove_punc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    remove_new_line = request.POST.get('remove_new_line', 'off')
    remove_extra_spaces = request.POST.get('remove_extra_spaces', 'off')

    if removepunc == 'on' :
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`.'''
        analysed = ""
        for char in text:
            if char not in punctuations:
                analysed += char

        param = {'analyse_text': analysed, 'purpose' : 'remove punctuation'}
        text = analysed

    if capitalize == 'on' :
        analysed = ""
        for char in text:
           analysed += char.upper()

        param = {'analyse_text': analysed, 'purpose' : 'capitalize'}
        text = analysed
    if remove_new_line == 'on':
        analysed = ""
        for char in text:
            if char != '\n' and char != '\r':
                analysed += char

        param = {'analyse_text': analysed, 'purpose': 'Remove new line'}
        text = analysed
    if remove_extra_spaces == 'on':
        analysed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analysed += text[index]
        param = {'analyse_text': analysed, 'purpose': 'Remove Extra spaces'}


    if removepunc != 'on' and remove_new_line != 'on' and remove_extra_spaces != 'on' and capitalize != 'on':
        return HttpResponse("<p>Error : Please select operation and try again!</p>")

    return render(request, 'analyse_result.html', param)
