

def use_context(request):
    return {
        'user': request.user,
        'username': ''
    }

class A:
    pass

class B:
    pass

a = A()
b = B()


isinstance(a, A)
isinstance(a, B)