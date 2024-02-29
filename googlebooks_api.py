import requests

def search_books(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)

    if response.status_code == 200:
        books_data = response.json()
        for book in books_data ['items']:
            title = book['volumeInfo']['title']
            authors = ', '.join(book['volumeInfo']['authors'])
            print(f"Title: {title}")
            print(f"Authors: {authors}")
            print()
    else:
        print("Failed to fetch book data.")

    search_query = input("Enter search query: ")
    search_books(search_query)