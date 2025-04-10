from django.shortcuts import render
from math import factorial

def fact(n, x):
    return factorial(n)//(factorial(n-x)*factorial(x))

def binomial(n, x, p):
    q = 1 - p
    fatorialC = fact(n, x)
    return fatorialC*(p ** x)*(q ** (n-x))

def binomial_acc(n, x, p):
    i = 0
    acc = 0
    while (i <= x):
        acc += binomial(n, i, p)
        i += 1
    return acc

def binomial_calc(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        x = int(request.POST.get('x'))
        pp = int(request.POST.get('p'))

        p = (pp /100)

        proba = binomial_acc(n, x, p)  # chamando a funcao
        distri = binomial(n, x, p)  # chamando a funcao

        print(proba * 100)
        print(distri* 100 )

        print("\n")
        print(" A probabilidade Acumulativa é:  {:.4f}".format(proba))
        print(" Distruibuição Binomial é : {:.4f} \n".format(distri))
        context = {
            'proba': "{:.4f}".format(proba),
            'distribuicao': "{:.4f}".format(distri),

            "proba_percentual": round(proba * 100, 2),
            "distri_percentual": round(distri * 100, 2)
        }
        return render(request, 'resultado.html', context)

    return render(request, 'formulario.html')
