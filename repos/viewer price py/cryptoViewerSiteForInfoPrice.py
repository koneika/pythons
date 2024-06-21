import requests

while(True):
    def download_and_print(url):
        try:

            

            response = requests.get(url)
            if response.status_code == 200:  # Успешный запрос
                text = response.text
                # print(len(text))  # Выводим содержимое страницы
                # Ваш огромный текст
                findIt = '<span class="sc-f70bb44c-0 jxpCgO base-text">$'
                findIt2 = '</span>'
                # Используем метод find() для поиска слова "space"
                index = text.find(findIt)

                # Проверяем, найдено ли слово
                if index != -1:
                    # Проверяем, достаточно ли символов после index
                    if len(text) >= index + 4:
                        # Отображаем символы на позициях index+1, index+2 и index+3
                        print(text[index + 46:index + 53])
                    else:
                        # Если символов менее трех, отображаем все символы после index
                        print(text[index + 1:])
                else:
                    print("Слово 'space' не найдено в тексте.")

            else:

                print("Ошибка при загрузке страницы:", response.status_code)

        except requests.exceptions.RequestException as e:

            print("Ошибка при выполнении запроса:", e)

    # <span class="sc-f70bb44c-0 jxpCgO base-text">$4.81</span>
    # Пример использования
    url = "https://coinmarketcap.com/currencies/toncoin/"  # Замените на нужный URL
    download_and_print(url)

    # text1 = '<span class="sc-f70bb44c-0 jxpCgO base-text">$'
    # text2 = '</span>'

    # start_index = url.find(text1)
    # end_index = url.find(text2)

    
