# Made by Durwankur
from django.http import HttpResponse
from django.shortcuts import render

# Text utils website
def index(request):
    return render(request, 'index.html')


def analyse(request):
    input_data = str(request.GET.get('inpText', 'default')) # Converting the input type to str so that all the built in string methods can be used by it

    # The values from the checkboxes stored in the below variables
    want_punc_removed = request.GET.get('puncRemover', 'off')
    want_allcaps = request.GET.get('allCaps', 'off')
    want_newline_removed = request.GET.get('newlRemover', 'off')
    want_space_removed = request.GET.get('spaceRemover', 'off')
    charcount = request.GET.get('charCounter', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    params = {}

    if want_punc_removed == 'on':
        punc_remove = ""
        for char in input_data:
            if char not in punctuations:
                punc_remove += char
        params['puncremoved'] = punc_remove

    if want_newline_removed == 'on':
        nl_remove = ""
        for char in input_data:
            if char != '\n':
                nl_remove += char
        params['nlremoved'] = nl_remove

    if want_space_removed == 'on':
        space_remove = ""
        for char in input_data:
            if char != ' ':
                space_remove += char
        params['spaceremoved'] = space_remove

    if want_allcaps == 'on':
        caps_all = input_data.upper()
        params['capsall'] = caps_all

    if charcount == 'on':
        char_count = len(input_data)
        params['charcount'] = char_count

    return render(request, 'analyse.html', params)
