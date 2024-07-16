class bind:
    bound_methods = {}

    def __init__(self,name):
        self.name= name
    def __call__(self,func):
        def wrapper(wrapped_self,*args, **kwargs):
            return self.bound_methods[(func.__qualname__,wrapped_self.name)](wrapped_self,*args, **kwargs)
        self.bound_methods[(func.__qualname__,self.name)] = func
        return wrapper
        
