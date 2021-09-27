print ('Welkom bij het sollicitatie van Cluedo')

Geslacht = input ('Ben je een Man of Vrouw?')
Leeftijd = int(input ('Hoe oud ben je?'))
Lengte = int(input ('Hoe lang ben je?'))
Gewicht = input ('Wat is je gewicht?')
print ('Tactisch,Knap,Intiem,Charmant,Slim en Vanzelfsprekend') 
Persoonlijkheid = input ('Welke van de bovenste woorden passen het best bij je?')


if Geslacht == 'Man' and  Leeftijd >= 18 and Lengte >= 180 and Persoonlijkheid == 'Tactisch':
    print ('Je mag op auditie voor de rol van Kolonel van Geelen')

if Geslacht == 'Man' and  Leeftijd >= 18 and Lengte >= 180 and Persoonlijkheid == 'Intiem': 
    print ('Je mag op auditie voor de rol van Dominee Groenewoud')

if Geslacht == 'Man' and  Leeftijd >= 18 and Lengte >= 180 and Persoonlijkheid == 'Slim': 
    print ('Je mag op auditie voor de rol van Professor Pimpel')

if Geslacht == 'Vrouw' and  Leeftijd >= 18 and Lengte >= 160 and Persoonlijkheid == 'Knap': 
    print ('Je mag op auditie voor de rol van Rosa Roodhart')

if Geslacht == 'Vrouw' and  Leeftijd >= 18 and Lengte >= 160 and Persoonlijkheid == 'Charmant': 
    print ('Je mag op auditie voor de rol van Mevrouw Blaauw van Draet')

if Geslacht == 'Vrouw' and  Leeftijd >= 18 and Lengte >= 160 and Persoonlijkheid == 'Vanzelfsprekend': 
    print ('Je mag op auditie voor de rol van Mevrouw de Wit')



elif Leeftijd < 18 or  Lengte < 160:
    print ('Je mag helaas niet op auditie.')
