import os
from bs4 import BeautifulSoup

ligues = {
	"Brasileirão A": "https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-a/325#id:58766",
	"Brasileirão B": "https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-b/390#id:59015",
	"Liga Inglesa": "https://www.sofascore.com/pt/torneio/futebol/england/premier-league/17#id:61627",
	"Liga Espanhola": "https://www.sofascore.com/pt/torneio/futebol/spain/laliga/8#id:61643",
	"Liga Alemã": "https://www.sofascore.com/pt/torneio/futebol/germany/bundesliga/35#id:63516",
	"Liga Italiana": "https://www.sofascore.com/pt/torneio/futebol/italy/serie-a/23#id:63515",
	"Liga Francesa": "https://www.sofascore.com/pt/torneio/futebol/france/ligue-1/34#id:61736",
	"Liga Holandesa": "https://www.sofascore.com/pt/torneio/futebol/netherlands/eredivisie/37#id:61666",
	"Liga Portuguesa": "https://www.sofascore.com/pt/torneio/futebol/portugal/liga-portugal-betclic/238#id:63670",
	"UEFA Champions League": "https://www.sofascore.com/pt/torneio/futebol/europe/uefa-champions-league/7#id:61644",
	"UEFA Europa League": "https://www.sofascore.com/pt/torneio/futebol/europe/uefa-europa-league/679#id:61645",
	"Libertadores": "https://www.sofascore.com/pt/torneio/futebol/south-america/conmebol-libertadores/384#id:57296",
	"Sulamericana": "https://www.sofascore.com/pt/torneio/futebol/south-america/conmebol-sudamericana/480#id:57297"
}

command = "curl " + ligues["Brasileirão A"]
actual_home = os.popen(command).read()
soup = BeautifulSoup(actual_home, "html.parser")

print(soup.title)
