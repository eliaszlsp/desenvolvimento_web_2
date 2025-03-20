def registrar_info(*args, **kwargs):

    print("Argumentos posicionais (*args):")
    for arg in args:
        print(f"- {arg}")

    print("\nArgumentos nomeados (**kwargs):")
    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")
