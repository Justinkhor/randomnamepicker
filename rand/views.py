from django.shortcuts import render
from .forms import TrialForm
from .models import Trial
import random

# Create your views here.
def main(request):
    form = TrialForm()
    if request.method == "POST":
        form = TrialForm(request.POST)
        this = form.save(commit=False)
        this.save()
        lst = this.text.split()
        if len(lst) != 0:
            index = random.randint(0,len(lst)-1)
            this.choice = lst[index]
        else:
            this.choice = "LIST IS EMPTY"
        return render(request, 'rand/choice.html', {'this': this})
    return render(request, 'rand/main.html', {'form': form})
