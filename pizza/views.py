from django.shortcuts import render

from .forms import MultiplePizzaForm, PizzaForm

from django.contrib import messages

from django.forms import formset_factory

from .models import Pizza

# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()

            size = filled_form.cleaned_data.get('size')
            topping1 = filled_form.cleaned_data.get('topping1')
            topping2 = filled_form.cleaned_data.get('topping2')

            messages.success(request, f'Thanks for ordering! Your {size} {topping1} and {topping2} pizza is on its way')

            filled_form = PizzaForm()

        else:
            created_pizza_pk = None
            messages.warning(request, 'Pizza order failed, try again!')

        return render(request, 'pizza/order.html', {'created_pizza_pk':created_pizza_pk, 'pizzaform':filled_form,
        'multiple_form':multiple_form})


    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform':form,
        'multiple_form':multiple_form})



def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)

    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data.get('number')

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            messages.success(request, 'Pizzas have been orderd')    
        else:
            messages.warning(request, 'Order was not created, please try again')
        
        return render(request, 'pizza/pizzas.html', {'formset': formset})

    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})



def edit_order(request, pk):
    pizza = Pizza.objects.get(id=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            messages.success(request, 'Order has been updated')
            return render(request, 'pizza/edit_order.html',{'pizzaform':form,'pizza':pizza})
   
    return render(request, 'pizza/edit_order.html',{'pizzaform':form,'pizza':pizza})