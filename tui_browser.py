import urwid
import requests

# Функция для получения HTML-кода веб-страницы
def get_html(url):
    response = requests.get(url)
    return response.text

# Функция для отображения HTML-кода в TUI
def display_html(html):
    # Просто выводим HTML как текст
    return urwid.Text(html)

# Главная функция
def main():
    # URL веб-страницы, которую вы хотите отобразить
    url = "https://www.geckoterminal.com/ton/pools/EQCCsJOGdUdSGq0ambJFgSptdHfDPkaQlKlLIKTqtazhhcps"
    
    # Получаем HTML-код веб-страницы
    html = get_html(url)
    
    # Создаем виджет для отображения HTML-кода в TUI
    widget = display_html(html)
    
    # Создаем виджет для запуска TUI
    top = urwid.Filler(widget)
    
    # Создаем главный петле urwid
    urwid.MainLoop(top).run()

if __name__ == "__main__":
    main()