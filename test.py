base_url = 'https://myanimelist.net/anime/genre/1/Action?page='
urls = [base_url+str(i) for i in range(30)]
print(urls)