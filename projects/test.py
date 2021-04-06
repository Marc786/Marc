# grille = {
#                 'joueurs': [
#                     {'nom': 'x', 'murs': '1', 'pos': (1, 2)},
#                     {'nom': 'y', 'murs': '2', 'pos': (2, 1)},
#                 ],
#                 'murs': {
#                     'horizontaux': [...],
#                     'verticaux': [...],
#                 }
# }

# print(len(grille['joueurs']))


# # joueurs = ['joueur1', {'nom': 'x', 'murs': 10, 'pos': (1, 2)}]
# etat_de_jeu = {
#             'joueurs': [
#                 #{'nom': self.joueurs[0]['nom'], 'murs': self.joueurs[0]['murs'], 'pos': self.joueurs[0]['pos']},
#                 #{'nom': self.joueurs[1]['nom'], 'murs': self.joueurs[1]['murs'], 'pos': self.joueurs[1]['pos']}
#             ],
#             'murs': {
#                 'horizontaux':[],
#                 'verticaux':[]
#             }
# }
# murs = {
#     "joueurs": 'allo',
#     "murs":{
#         'horizontaux':[[1, 2], [3, 4], [5, 6]],
#         'verticaux':[]
#     }
# }
# for murs in murs['murs']['horizontaux']:
#     etat_de_jeu['murs']['horizontaux'].append(murs)
# print(etat_de_jeu)





# def pri():   
#     print(etat_partie()['murs'])
#     return 7
# def etat_partie():
#     dico = {
#         'joueurs':['x', 'y'],
#         'murs': 6
#     }
#     return dico

# pri()

# murs = {
#     'horizontaux': [],
#     'verticaux': []
# }

# joueurs = [
#     {'nom': 'joueurs1',  'murs': 6, 'pos':['x','y']},
#     {'nom': 'joueurs2',  'murs': 6, 'pos':['x','y']}
# ]

from selenium import webdriver


PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.youtube.com/?hl=fr&gl=CA')
print(driver.title)

search = driver.find_element_by_name('search_query')
search.send_keys('allo')

button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
button.click()
