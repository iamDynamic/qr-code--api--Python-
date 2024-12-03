import http.client

conn = http.client.HTTPSConnection("qr-code-generator20.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7626dd03femsh15b00c89eeed8cbp185012jsnfa57c8cbd6fe",
    'x-rapidapi-host': "qr-code-generator20.p.rapidapi.com"
}

WebsiteUrl = input("website Url: ")

conn.request("GET", f"/generateadvanceimage?data={WebsiteUrl}&size=500&margin=10&label=a%hg&label_size=20&label_alignment=center&foreground_color=FF2400&background_color=00DBFF", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))