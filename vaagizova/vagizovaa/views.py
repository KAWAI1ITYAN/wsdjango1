from django.shortcuts import render

from django.http import HttpResponse

def index(requester, name=None, age=None, interes=None):
    return HttpResponse(f"""
        <h3>ФИО: {name}</h3>
        <h3>Возраст: {age}</h3>
        <h3>Интересы: {interes}</h3>
        """)

def about(requester):
    return HttpResponse(f"""
        <h1>Обо мне</h1>
        <h3>Приехала из Казани. Узнав, что поступила в Алабугу, летом переехали с родителями в Набережные Челны.</h3>
        <h3>Закончила 11 классов, была хорошисткой</h3>
        <h3>Очень люблю учиться, узнавать новое</h3>
        """)

def contacts(requester):
    return HttpResponse(f"""
    <h1>Как со мной связаться</h1>
    <h3>GitHub - KAWAI1ITYAN</h3>
    <h3>Telegram - @hideitinmysock22</h3>
    <h3>Вконтакте - https://vk.com/hideitinmysock22</h3>
    <h3>Почта - daisyyt6@gmail.com</h3>
    """)
