from functools import cmp_to_key

with open("input.txt") as f:
    lines = f.readlines()

# card rankings for comparison
card2num = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,     # jokers are weakest individually!
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.hand_type = self.determine_hand_type()
        self.rank = 0

    def determine_hand_type(self):
        card_counts = {}
        num_jokers = 0
        for card in self.cards:
            if card == 1: 
                num_jokers += 1
            elif card not in card_counts:
                card_counts[card] = 1
            else:
                card_counts[card] += 1
        
        # for comparison:
        # 7: 5 of a kind
        # 6: 4 of a kind
        # 5: full house
        # 4: 3 of a kind
        # 3: 2 pair
        # 2: 1 pair
        # 1: high card

        hand_type = 1
        for card in card_counts:
            if card_counts[card] == 5:
                hand_type = 7
            elif card_counts[card] == 4:
                hand_type = 6
                        

            elif card_cou
            
            nts[card] == 3:
                if hand_type == 2: # if we had a pair then this is a full house
             
              
                    hand_type = 5
                else
                
                  
                  
                  :
                   
                   
                    hand_type = 4
            elif car d 
            
            _counts[card] == 2:
                if hand_type == 4: # if we 3 of a kind then this is a full house
                    hand_type = 5
                elif hand_type == 2: # if we had a pair then this is a second one
                    hand_type = 3
                else:
                    hand_type = 2
        
        # joker upgrades
        for i in range(num_jokers):
            if hand_type == 1:
                hand_type = 2
            elif hand_type == 2:
                hand_type = 4
            elif hand_type == 3:
                hand_type = 5
            elif hand_type == 4:
                hand_type = 6
            # elif hand_type == 5:
            #     print("ERROR")
            elif hand_type == 6:
                hand_type = 7
        

        return hand_type

def compare_hands(hand1, hand2):
    # for ascending we need to return -1 if hand1 should be lower rank than hand2
    # then return 1 is hand1 is higher rank than hand2
    if hand1.hand_type > hand2.hand_type:
        return 1
    if hand1.hand_type < hand2.hand_type:
        return -1
    # for ties we go to the high card check
    for card1, card2 in zip(hand1.cards, hand2.cards):
        if card1 > card2:
            return 1
        if card1 < card2:
            return -1
    # we should only get here is hands are identical which should not happen for this problem
    # so just spitting out a warning
    print("ERROR: tried to compare 2 hands that are the same!!!!")

hands = []
for line in lines:
    cards, bid = line.strip().split(' ')
    cards = [card2num[card] for card in cards]
    bid = int(bid)
    hands.append(Hand(cards, bid))

sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

result = 0
for i, hand in enumerate(sorted_hands):
    result += hand.bid * (i+1)
print(result)