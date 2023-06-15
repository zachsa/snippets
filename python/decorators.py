def perf(fn):
    def wrapper(*args, **kwargs):
        print("Log performance start")
        r = fn(*args, **kwargs)
        print("Log performance end")
        return r
    
    return wrapper

@perf
def hello_world():
    print('hello world')

hello_world()