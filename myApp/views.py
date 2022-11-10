from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import User, Expense, Income

# Create your views here.
# def base(request):
#     return render(request, 'base.html')

def LoginPage(request):
    return render(request, 'login.html')

def SignupPage(request):
    return render(request, 'signup.html')

def LogoutPage(request):
    del request.session['name']
    del request.session['uid']
    return redirect('/')

def dashboard(request):
    if 'uid' in request.session:
        name = request.session['name']
        expensesum = Expense.objects.filter(user_id = request.session['uid']).aggregate(Sum('amount'))
        esum = expensesum['amount__sum']
        incomesum = Income.objects.filter(user_id = request.session['uid']).aggregate(Sum('amount'))
        isum = incomesum['amount__sum']
        ibusiness = Income.objects.filter(user_id = request.session['uid']).filter(category='business').aggregate(Sum('amount'))
        isalary = Income.objects.filter(user_id = request.session['uid']).filter(category='salary').aggregate(Sum('amount'))
        ifreelancing = Income.objects.filter(user_id = request.session['uid']).filter(category='freelancing').aggregate(Sum('amount'))
        iother = Income.objects.filter(user_id = request.session['uid']).filter(category='other').aggregate(Sum('amount'))
        if esum==None or isum==None:
            context = {'esum':'0', 'isum':'0','name':name, 'net':'0', 'ib':ibusiness, 'is':isalary, 'if':ifreelancing, 'io':iother}
            return render(request, 'dashboard.html', context)
        elif isum>=esum:
            pbalance = isum - esum
            context = {'esum':esum, 'isum':isum, 'name':name, 'pbalance':pbalance, 'ib':ibusiness, 'is':isalary, 'if':ifreelancing, 'io':iother}
            return render(request, 'dashboard.html', context)
        elif esum>isum:
            nbalance = esum - isum
            context = {'esum':esum, 'isum':isum, 'name':name, 'nbalance':nbalance, 'ib':ibusiness, 'is':isalary, 'if':ifreelancing, 'io':iother}
            return render(request, 'dashboard.html', context)
            
    else:
        return redirect('/')

def about(request):
    if 'uid' in request.session:
        return render(request, 'about.html')
    else:
        return redirect('/')

def signupdata(request):
    obj = User()
    obj.name = request.GET.get('username')
    obj.password = request.GET.get('password')
    obj.phone = request.GET.get('phone')
    obj.email = request.GET.get('email')
    obj.save()
    return redirect('/')

def signindata(request):
    uname = request.GET.get('username')
    pwd = request.GET.get('password')
    user = User.objects.filter(name = uname, password = pwd)

    if user:
        lst = user.values()
        request.session['name'] = lst[0]['name']
        request.session['uid'] = lst[0]['id']
        return redirect('/dashboard/')
    else:
        return render(request, 'login.html', {'error': 'Invalid username or password'})

def saveexpense(request):
    if 'uid' in request.session:
        return render(request, 'expense.html')
    else:
        return redirect('/')

def saveincome(request):
    if 'uid' in request.session:
        return render(request, 'income.html')
    else:
        return redirect('/')

def saveexpensedata(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        obj = Expense()
        obj.date = request.GET.get('date')
        obj.time = request.GET.get('time')
        obj.remark = request.GET.get('remark')
        obj.amount = request.GET.get('amount')
        obj.category = request.GET.get('category')
        obj.user_id = uid
        obj.save()
        return redirect('/dashboard/')
    else:
        return redirect('/')

def saveincomedata(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        obj = Income()
        obj.date = request.GET.get('date')
        obj.time = request.GET.get('time')
        obj.remark = request.GET.get('remark')
        obj.amount = request.GET.get('amount')
        obj.category = request.GET.get('category')
        obj.user_id = uid
        obj.save()
        return redirect('/dashboard/')
    else:
        return redirect('/')

def viewexpense(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        expensedata = Expense.objects.filter(user_id = uid)
        context = {'edata':expensedata}
        return render (request, 'showexpense.html', context)
    else:
        return redirect('/')    

def viewincome(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        incomedata = Income.objects.filter(user_id = uid)
        context = {'idata':incomedata}
        return render (request, 'showincome.html', context)
    else:
        return redirect('/')

def deleteincome(request, id):
    if 'uid' in request.session:
        user_income = Income.objects.get(id=id)
        user_income.delete()
        return redirect('/viewincome/')
    else:
        return redirect('/')

def deleteexpense(request, id):
    if 'uid' in request.session:
        user_expense = Expense.objects.get(id=id)
        user_expense.delete()
        return redirect('/viewexpense/')
    else:
        return redirect('/')

def searchexpensedata(request, id):
    data = Expense.objects.get(id=id)
    return render(request, 'editexpense.html', {'data':data})

def saveeditexpense(request):
    obj = Expense()
    obj.id = request.GET.get('id')
    obj.date = request.GET.get('date')
    obj.time = request.GET.get('time')
    obj.amount = request.GET.get('amount')
    obj.remark = request.GET.get('remark')
    obj.category = request.GET.get('category')
    obj.user_id = request.GET.get('user_id')
    obj.save()
    return redirect('/viewexpense/')

def searchincomedata(request, id):
    data = Income.objects.get(id=id)
    return render(request, 'editincome.html', {'data':data})

def saveeditincome(request):
    obj = Income()
    obj.id = request.GET.get('id')
    obj.date = request.GET.get('date')
    obj.time = request.GET.get('time')
    obj.amount = request.GET.get('amount')
    obj.remark = request.GET.get('remark')
    obj.category = request.GET.get('category')
    obj.user_id = request.GET.get('user_id')
    obj.save()
    return redirect('/viewincome/')

def sortbydate(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        data = Expense.objects.filter(user_id=uid).order_by('date')
        return render(request, 'showexpense.html', {'edata':data})
    else:
        redirect('/')


def sortbydate2(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        data = Expense.objects.filter(user_id=uid).order_by('-date')
        return render(request, 'showexpense.html', {'edata':data})
    else:
        redirect('/')

def sortbyamt(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        data = Expense.objects.filter(user_id=uid).order_by('amount')
        return render(request, 'showexpense.html', {'edata':data})
    else:
        redirect('/')

def sortbyamt2(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        data = Expense.objects.filter(user_id=uid).order_by('-amount')
        return render(request, 'showexpense.html', {'edata':data})
    else:
        redirect('/')


def sortbydateincome(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        data = Income.objects.filter(user_id=uid).order_by('date')
        return render(request, 'showincome.html', {'idata':data})
    else:
        redirect('/')


def sortbydateincome2(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        data = Income.objects.filter(user_id=uid).order_by('-date')
        return render(request, 'showincome.html', {'idata':data})
    else:
        redirect('/')

def sortbyamtincome(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        data = Income.objects.filter(user_id=uid).order_by('amount')
        return render(request, 'showincome.html', {'idata':data})
    else:
        redirect('/')

def sortbyamtincome2(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        data = Income.objects.filter(user_id=uid).order_by('-amount')
        return render(request, 'showincome.html', {'idata':data})
    else:
        redirect('/')

def expensecatfood(request):
    if 'uid' in request.session:
        uid=request.session['uid']
        data = Expense.objects.filter(user_id=uid).filter(category='food')
        return render(request, 'showexpense.html', {'edata': data})
    else:
        redirect('/')

def expensecattravel(request):
    if 'uid' in request.session:
        uid=request.session['uid']
        data = Expense.objects.filter(user_id=uid).filter(category='travel')
        return render(request, 'showexpense.html', {'edata': data})
    else:
        redirect('/')

def expensecatdonation(request):
    if 'uid' in request.session:
        uid=request.session['uid']
        data = Expense.objects.filter(user_id=uid).filter(category='donation')
        return render(request, 'showexpense.html', {'edata': data})
    else:
        redirect('/')

def expensecatother(request):
    if 'uid' in request.session:
        uid=request.session['uid']
        data = Expense.objects.filter(user_id=uid).filter(category='other')
        return render(request, 'showexpense.html', {'edata': data})
    else:
        redirect('/')

def incomecatbuss(request):
    if 'uid' in request.session:
        uid=request.session['uid']
        data = Income.objects.filter(user_id=uid).filter(category='business')
        return render(request, 'showincome.html', {'idata': data})
    else:
        redirect('/')

def incomecatfreela(request):
    if 'uid' in request.session:
        uid=request.session['uid']
        data = Income.objects.filter(user_id=uid).filter(category='freelancing')
        return render(request, 'showincome.html', {'idata': data})
    else:
        redirect('/')

def incomecatsalary(request):
    if 'uid' in request.session:
        uid=request.session['uid']
        data = Income.objects.filter(user_id=uid).filter(category='salary')
        return render(request, 'showincome.html', {'idata': data})
    else:
        redirect('/')

def incomecatother(request):
    if 'uid' in request.session:
        uid=request.session['uid']
        data = Income.objects.filter(user_id=uid).filter(category='other')
        return render(request, 'showincome.html', {'idata': data})
    else:
        redirect('/')