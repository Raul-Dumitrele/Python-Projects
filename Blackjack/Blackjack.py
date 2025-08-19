import random

# Funcție pentru a crea un pachet de cărți și a-l amesteca
def create_deck():
    suits = ['Inimă', 'Romb', 'Treflă', 'Pică']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Funcție pentru a calcula valoarea unei mâini
def calculate_hand_value(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
              'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    total_value = 0
    aces = 0

    for card in hand:
        rank = card[0]
        total_value += values[rank]
        if rank == 'A':
            aces += 1
    
    # Ajustăm valoarea dacă avem ași și totalul depășește 21
    while total_value > 21 and aces:
        total_value -= 10
        aces -= 1

    return total_value

# Funcție pentru a verifica dacă jucătorul sau dealerul a câștigat
def check_winner(player_value, dealer_value):
    if player_value > 21:
        print("Ai pierdut! Ai depășit 21.")
    elif dealer_value > 21:
        print("Ai câștigat! Dealerul a depășit 21.")
    elif player_value > dealer_value:
        print("Ai câștigat! Ai un scor mai mare decât dealerul.")
    elif player_value < dealer_value:
        print("Dealerul a câștigat cu un scor mai mare.")
    else:
        print("Este egalitate!")

# Funcție principală pentru jocul de Blackjack
def play_blackjack():
    print("Bun venit la Blackjack!")
    deck = create_deck()
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Afișăm mâna inițială a jucătorului
    print(f"Tu ai: {player_hand[0][0]} de {player_hand[0][1]} și {player_hand[1][0]} de {player_hand[1][1]}")
    print(f"Dealerul are: {dealer_hand[0][0]} de {dealer_hand[0][1]} și o carte ascunsă.")
    
    # Runda jucătorului
    while True:
        player_value = calculate_hand_value(player_hand)
        print(f"Valoarea mâinii tale este: {player_value}")
        
        if player_value > 21:
            break
        
        action = input("Vrei să mai iei o carte (hit) sau să te oprești (stand)? (hit/stand): ").lower()
        if action == 'hit':
            new_card = deck.pop()
            player_hand.append(new_card)
            print(f"Ai primit {new_card[0]} de {new_card[1]}")
        elif action == 'stand':
            break
        else:
            print("Te rog introdu 'hit' sau 'stand'.")

    # Runda dealerului
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"\nDealerul are: {dealer_hand[0][0]} de {dealer_hand[0][1]} și {dealer_hand[1][0]} de {dealer_hand[1][1]}")
    
    while dealer_value < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Dealerul a tras {new_card[0]} de {new_card[1]}")

    print(f"Valoarea mâinii dealerului este: {dealer_value}")
    
    # Verificăm cine a câștigat
    check_winner(player_value, dealer_value)

# Începem jocul
play_blackjack()
