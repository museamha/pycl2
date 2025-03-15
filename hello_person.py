def hello(name, lang):
    greetings = {
        "English": "hello",
        "spanish": "hola",
        "german": "hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="the name of the person to greet."
    )
    
    parser.add_argument(
        "-l" , "--lang", metavar="language",
        required=True, choices=["English","spanish","german"],
        help="the language of the greeting"
    )

    args = parser.parse_args()

    msg = f"hello {args.name}!"

    hello(args.name, args.lang)