'''

Straight-flush
Four-of-a-kind
Full house
Flush
Straight
Three-of-a-kind
Two pair
Pair
Nothing.

'''
def values_check(cards):
    card_values = [card[:-1] for card in cards]
    values_count_dict = {value: card_values.count(value) for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] if value in card_values}
    values_count = [card_values.count(value) for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] if value in card_values]
    values_count.sort(reverse=True)
    if values_count[0] >= 4:                              # 4 of a kind
        for x,y in values_count_dict.items():
            if y == 4:
                return 4, [x]
    elif values_count[0] == 3 and values_count[1] == 1:   # 3 of a kind
        for x,y in values_count_dict.items():
            if y == 3:
                return 3, [x]
    elif values_count[0] == 3 and (values_count[1] == 2 or values_count[1] == 3):   # full house
        s = []
        ordered_by_values_dict = dict(sorted(values_count_dict.items(), key=lambda item: item[1], reverse=True))
        for x, y in ordered_by_values_dict.items():
            if y == 3 or y == 2:
                s.append(x)
        return 'fh', s
    elif values_count[0] == 2 and values_count[1] == 2:     # two pair
        s = []
        for x, y in values_count_dict.items():
            if y == 2:
                s.append(x)
        return 22, s
    elif values_count[0] == 2:
        for x,y in values_count_dict.items():
            if y == 2:
                return 2, [x]
    else:
        return 0, []

def flush_check(cards):
    card_suits_dict = {suit: [card[:-1] for card in cards if suit == card[-1]] for suit in ['♠', '♦', '♣', '♥']}
    for suit, cards in card_suits_dict.items():
        if len(cards) >= 5:
            return True, cards

    return False, []


def straight_check(cards):
    right_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    right_order_str = ''.join(right_order)
    card_values = [card[:-1] for card in cards]
    card_values.sort(key=right_order.index)
    no_dub = []
    [no_dub.append(i) for i in card_values if i not in no_dub]
    if len(no_dub) == 7:
        v1 = ''.join(no_dub[:5])
        v2 = ''.join(no_dub[1:6])
        v3 = ''.join(no_dub[2:])
        if v3 in right_order_str:
            return True, no_dub[2:]
        elif v2 in right_order_str:
            return True, no_dub[1:6]
        elif v1 in right_order_str:
            return True, no_dub[:5]
    elif len(no_dub) == 6:
        v1 = ''.join(no_dub[:5])
        v2 = ''.join(no_dub[1:])
        if v2 in right_order_str:
            return True, no_dub[1:]
        elif v1 in right_order_str:
            return True, no_dub[:-1]
    else:
        v = ''.join(no_dub)
        if v in right_order_str:
            return True, no_dub

    return False, []


def straight_flush_check(cards):        # ["K♠", "J♥", "J♣", "Q♥", "9♥", "8♥", "10♥"]
    x, y = flush_check(cards)
    if not x:
        return False, []
    else:
        right_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        right_order_str = ''.join(right_order)
        used_cards = [i for i in right_order if i in y]
        if len(used_cards) == 7:
            if ''.join(used_cards[2:]) in right_order_str:
                return True, used_cards[2:][::-1]
            elif ''.join(used_cards[1:6]) in right_order_str:
                return True, used_cards[1:6][::-1]
            if ''.join(used_cards[:5]) in right_order_str:
                return True, used_cards[:5][::-1]
        elif len(used_cards) == 6:
            if ''.join(used_cards[1:]) in right_order_str:
                return True, used_cards[1:][::-1]
            elif ''.join(used_cards[:5]) in right_order_str:
                return True, used_cards[:5][::-1]
        else:
            if ''.join(used_cards) in right_order_str:
                return True, used_cards[::-1]
    return False, []



def form_output(cards, s, k):
    cards = [x[:-1] for x in cards]
    order = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    res = sorted(s, key=order.index)
    l = 5 - k
    sp = [x for x in order if x not in res]
    second_part = [x for x in sp if x in cards][:l]
    ls = res + second_part
    if len(ls) > 5:
        ls = ls[:5]
    return ls


def hand(hole_cards, community_cards):
    if straight_flush_check(hole_cards + community_cards)[0]:
        return "straight-flush", form_output(hole_cards + community_cards, straight_flush_check(hole_cards + community_cards)[1], 5)
    if values_check(hole_cards + community_cards)[0] == 4:
        return "four-of-a-kind", form_output(hole_cards + community_cards, values_check(hole_cards + community_cards)[1], 4)
    if values_check(hole_cards + community_cards)[0] == 'fh':
        #return "full house", form_output(hole_cards + community_cards, values_check(hole_cards + community_cards)[1], 5)
        return "full house", values_check(hole_cards + community_cards)[1]
    if flush_check(hole_cards + community_cards)[0]:
        return "flush", form_output(hole_cards + community_cards, flush_check(hole_cards + community_cards)[1], 5)
    if straight_check(hole_cards + community_cards)[0]:
        return "straight", form_output(hole_cards + community_cards, straight_check(hole_cards + community_cards)[1], 5)
    if values_check(hole_cards + community_cards)[0] == 3:
        return "three-of-a-kind", form_output(hole_cards + community_cards, values_check(hole_cards + community_cards)[1], 3)
    if values_check(hole_cards + community_cards)[0] == 22:
        return "two pair", form_output(hole_cards + community_cards, values_check(hole_cards + community_cards)[1], 4)
    if values_check(hole_cards + community_cards)[0] == 2:
        print(values_check(hole_cards + community_cards)[1])
        return "pair", form_output(hole_cards + community_cards, values_check(hole_cards + community_cards)[1], 2)
    else:
        return "nothing", form_output(hole_cards + community_cards, [], 0)



#hand1(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])
cards = ["K♠", "A♦", "J♣", "Q♥", "9♥", "2♥", "3♦"]
cards1 = (["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"])    # straight flush
cards2 = (["5♠", "5♥"], ["5♣", "Q♥", "9♥", "5♦", "3♥"])     # 4 of a kind           +++
cards3 = (["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"])    # full house          +++
cards4 = (["K♠", "A♥"], ["J♣", "Q♥", "9♥", "10♥", "3♥"])    # flush                 +++
cards5 = (['9♠', 'Q♥'], ['A♥', '3♦', '10♣', '8♣', 'J♦'])    # straight              +++
cards6 = (["2♠", "A♣"], ["2♣", "Q♥", "9♥", "10♥", "2♥"])    # 3 of a kind           +++
cards7 = (['2♠', '5♥'], ['6♦', '7♥', '5♣', '2♣', '3♥'])    # 2 pair               +++
cards8 = (["2♠", "A♣"], ["K♣", "Q♥", "5♥", "10♥", "2♥"])    # pair                  +++
cards9 = (["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])    # nothing

#print(flush_check(cards2))
#print(straight_check(cards2))
#print(straight_flush_check(cards1))
#print(hand(["K♠", "A♦"], ["6♣", "K♥", "9♥", "2♥", "3♦"]))
print(hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]))
