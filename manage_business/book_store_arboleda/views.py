from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def home(request):
    books=Book.objects.all()
    context={'books':books}
 
    return render(request,'book_store_arboleda/home.html',context)
    
def logoutPage(request):
    logout(request)
    return redirect('/')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            print("working")
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'book_store_arboleda/login.html',context)
   
def registerPage(request):
    form = Createuserform()
    cust_form = Createcustomerform()
    
    if request.method == 'POST':
        form = Createuserform(request.POST)
        cust_form = Createcustomerform(request.POST)

        
        if form.is_valid() and cust_form.is_valid():
            print('form data is valid')
            user = form.save()
            customer = cust_form.save(commit=False)
            customer.user = user 
            customer.save()
            
            print(form.cleaned_data)
            print(cust_form.cleaned_data)
            
            return redirect('login')
        else:
            print('form data is not valid')
            for field in form:
                if field.errors:
                    print(f"Error in field {field.name}: {field.errors}")
            for field in cust_form:
                if field.errors:
                    print(f"Error in field {field.name}: {field.errors}")
    context = {
        'form': form,
        'cust_form': cust_form,
    }
    
    return render(request, 'book_store_arboleda/register.html', context)



    
def addbook(request):
    form=Createbookform()
    if request.method=='POST':
        form=Createbookform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
 
    context={'form':form}
    return render(request,'book_store_arboleda/addbook.html',context)

@login_required
def viewcart(request):
    cust = Customer.objects.filter(user=request.user)
    carts = []
    non_empty_cart_found = False
    for c in cust:
        cart_filter = Cart.objects.filter(customer=c)
        if cart_filter.exists():
            carts.append(cart_filter.first())
            non_empty_cart_found = True
    if not non_empty_cart_found:
        return render(request, 'book_store_arboleda/emptycart.html')
    context = {'carts': carts}
    return render(request, 'book_store_arboleda/viewcart.html', context)



@login_required
def addtocart(request,pk):
    book=Book.objects.get(id=pk)
    cust=Customer.objects.filter(user=request.user)
    
    for c in cust:       
        carts=Cart.objects.all()
        reqcart=''
        for cart in carts:
            if(cart.customer==c):
                reqcart=cart
                break
        if(reqcart==''):
            reqcart=Cart.objects.create(
                customer=c,
            )
        reqcart.books.add(book) 
        return redirect('viewcart')   
    return redirect('/')




def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('/')


def removeBookFromCart(request, book_id):
    cart = Cart.objects.filter(customer__user=request.user).first()
    book = Book.objects.get(id=book_id)
    cart.books.remove(book)
    return redirect('viewcart')

def removeBookCustomer(request, pk):
    removeBookFromCart(request, pk)
    return redirect('viewcart')


def updateBook(request, pk):
    
    book = get_object_or_404(Book, pk=pk)
    form = Createbookform(request.POST or None, instance=book)
    if form.is_valid():
        book = form.save() # save the form instance to the book object
        book.save() # save the book object to the database
        return redirect('/', id=pk)
    return render(request, 'book_store_arboleda/updateBook.html', {'form': form})


