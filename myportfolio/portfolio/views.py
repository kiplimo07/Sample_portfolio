from django.shortcuts import render
from .models import PortfolioItem, ContactSubmission
from .forms import ContactForm

def home(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def services(request):
    return render(request, 'portfolio/services.html')

def experience(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'portfolio/experience.html', {'portfolio_items': portfolio_items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactSubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'portfolio/contact.html', {'success': True})
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})