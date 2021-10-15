from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JkeggCQMJd0jIeJbhyCifd9u18oWxVLHDbGQcTf1Ft9gBnQ6xwJ7YK9nEmQEoyhNn6nDz9u9WWWP0jcUzGJ5dOy00icFUh4cI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)