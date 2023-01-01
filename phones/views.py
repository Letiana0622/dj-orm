from django.shortcuts import render
from django.http import HttpResponse
from phones.models import Phone

def show_catalog(request):
    sort = request.GET.get('sort',1)
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    if sort == 1:
        phones = phone_objects
        # phones = [f'{c.name}, {c.image}, {c.price}' for c in phone_objects]
    elif sort == 'name':
        phones = phone_objects.order_by('name')
        # phones = [f'{c.name}, {c.image}, {c.price}|{c.name.order_by()}' for c in phone_objects]
    elif sort == 'min_price':
        phones = phone_objects.order_by('price')
        # phones = [f'{c.name}, {c.image}, {c.price}|{c.price.order_by()}' for c in phone_objects]
    # msg = '<br>'.join(phones)
    print(phones)
    context = {
        'phones': phones
    }
    return render(request, template, context)

# Для реализации сортировки можно к урлу добавить параметр sort и получать его через `request.GET`. Например:
#  * `<имя_сайта>/catalog?sort=name` - сортировка по названию
#  * `<имя_сайта>/catalog?sort=min_price` - сначала отображать дешевые

def show_product(request, slug):
    phone_objects = Phone.objects.all()
    # for line in phone_objects:
    #     if {line.slug} == slug:
    #         phone = line
    phone = [f'{c.name}, {c.image}, {c.price},{c.release_date},{c.lte_exists}' for c in phone_objects if c.slug==slug]
    template = 'product.html'
    print(phone)
    context = {
        'phone': phone
    }
    return render(request, template, context)

# def list_car(request):
#     car_objects = Car.objects.all()
#     cars = [f'{c.id}: {c.brand}, {c.model}: {c.color} | {c.owners.count()}' for c in car_objects]
#     return HttpResponse('<br>'.join(cars))
#
# def list_person(request):
#     person_objects = Person.objects.all()
#     people = [f'{p.name}: {p.car}' for p in person_objects]
#     return HttpResponse('<br>'.join(people))


# def home_view(request):
#     template_name = 'home.html'
#     # впишите правильные адреса страниц, используя
#     # функцию `reverse`
#     pages = {
#         'Главная страница': reverse('home'),
#         'Показать рецепт омлета': reverse('omlet'),
#         'Показать рецепт пасты': reverse('pasta'),
#         'Показать рецепт сендвича': reverse('buter'),
#     }
#
#     # context и параметры render менять не нужно
#     # подбробнее о них мы поговорим на следующих лекциях
#     context = {
#         'pages': pages
#     }
#     return render(request, template_name, context)
#
# def omlet_view(request):
#     DATA_omlet = DATA['omlet']
#     msg = {}
#     template_name = 'recipe.html'
#     name = 'омлета'
#     servings = int(request.GET.get('servings',1))
#     for k, v in DATA_omlet.items():
#         v_servings = v * servings
#         msg[k] = v_servings
#     context = {
#         'msg': msg
#     }
#     return render(request, template_name, context)
