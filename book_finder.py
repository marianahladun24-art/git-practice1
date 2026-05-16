import requests

def search_book():
    print("=== Цифровий пошук книг (Open Library) ===")
    book_title = input("Введіть назву книги (наприклад, Harry Potter): ").strip()
    
    if not book_title:
        print("Назва книги не може бути порожньою!")
        return

    url = "https://openlibrary.org/search.json"
    params = {"title": book_title}
    
    print("\nНадсилання запиту до сервера... Зачекайте...")
    
    try:
        response = requests.get(url, params=params)
        
        # Перевірка статус-коду (успішно — 200)
        if response.status_code == 200:
            data = response.json()
            
            if data.get("numFound", 0) == 0:
                print("На жаль, за таким запитом нічого не знайдено.")
                return
                
            first_book = data["docs"][0]
            
            title = first_book.get("title", "Невідомо")
            authors = first_book.get("author_name", ["Автор не вказаний"])
            publish_year = first_book.get("first_publish_year", "Невідомо")
            pages = first_book.get("number_of_pages_median", "Невідомо")
            
            print("\n--- Результат пошуку від сервера ---")
            print(f"📖 Назва книги: {title}")
            print(f"✍️ Автор(и): {', '.join(authors)}")
            print(f"📅 Рік першої публікації: {publish_year}")
            print(f"📄 Кількість сторінок (середня): {pages}")
            print("-" * 36)
            
        elif response.status_code == 404:
            print("Помилка 404: Сервер не знайдено.")
        else:
            print(f"Помилка сервера! Статус-код: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Помилка мережі: {e}")

if __name__ == "__main__":
    search_book()