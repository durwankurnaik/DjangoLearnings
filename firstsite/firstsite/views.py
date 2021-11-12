# Made by Durwankur
from django.http import HttpResponse
from django.shortcuts import render


# Text utils website
def index(request):
    return render(request, 'index.html')


def analyse(request):
    # Converting the input type to str so that all the built in string methods can be used by it
    input_data = str(request.POST.get('inpText', 'default'))

    # The values from the checkboxes stored in the below variables
    want_punc_removed = request.POST.get('puncRemover', 'off')
    want_allcaps = request.POST.get('allCaps', 'off')
    want_newline_removed = request.POST.get('newlRemover', 'off')
    want_space_removed = request.POST.get('spaceRemover', 'off')
    charcount = request.POST.get('charCounter', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analysed = input_data
    params = {}

    if want_punc_removed == 'on':
        analysed = ""
        for char in input_data:
            if char not in punctuations:
                analysed += char
        params = {'analysed_text': analysed}

    if want_newline_removed == 'on':
        temp = analysed
        analysed = ""
        for char in temp:
            if char != '\n' and char != '\r':
                analysed += char
        params = {'analysed_text': analysed}

    if want_space_removed == 'on':
        temp = analysed
        analysed = ""
        for char in temp:
            if char != ' ':
                analysed += char
        params = {'analysed_text': analysed}

    if want_allcaps == 'on':
        temp = analysed
        analysed = temp.upper()
        params = {'analysed_text': analysed}

    return render(request, 'analyse.html', params)


def pricing(request):
    return render(request, 'pricing.html')
