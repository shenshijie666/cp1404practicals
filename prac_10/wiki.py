import wikipedia


def main():
    # Set the language to English, which can be changed as needed
    wikipedia.set_lang("en")

    while True:
        user_input = input("Please enter a page title or search phrase (Enter blank to exit): ")

        if not user_input:
            break

        try:
            # Obtain page abstract
            page_summary = wikipedia.summary(user_input)
            print("Abstract:", page_summary)

            # Obtain specific details of page
            page = wikipedia.page(user_input, autosuggest=False)
            print("Title:", page.title)
            print("URL:", page.url)
        except wikipedia.DisambiguationError as e:
            print(f"Discovering polysemous words：{e.options}. Please provide more specific search phrases.")
        except wikipedia.PageError:
            print("Unable to find the relevant page, please provide a valid page title or search phrase.")


if __name__ == "__main__":
    main()