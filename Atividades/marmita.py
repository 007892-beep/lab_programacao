proteina = ['peixe', 'ovo', 'frango']
carboidrato = ['batatadoce', 'arroz', 'quinoa']
salada = ['espinafre', 'alface', 'brocolis']

for pr in proteina:
    for cb in carboidrato:
        for sl in salada:
            if (not (pr == 'peixe' and cb == 'batatadoce')) and \
                ((sl == 'espinafre') == (pr == 'ovo')) and \
                    (pr != cb and cb != sl and pr != sl):        
                print(f"marmita: {pr} + {cb} + {sl}")
         
