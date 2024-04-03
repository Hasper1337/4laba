def limit_calls(max_calls=1):

    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise Exception(f"Функция {func.__name__} превысила максимальное количество вызовов ({max_calls})")
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@limit_calls(3)
def test_func():
    print("Вызов функции")


for i in range(5):
    try:
        test_func()
    except Exception as e:
        print(e)
