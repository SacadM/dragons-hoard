# Dragons Hoard

Dragons Hoard is a unique and strategic multiplayer card game where players compete to collect and store valuable poker hands. The game involves drawing cards, swapping cards with a shared treasure deck, and challenging opponents to poker hand duels. The ultimate goal is to have the highest value of stored hands once all cards have been discarded.

---

**Number of Players:** 2 or more (multiple decks required for every 3 or more players)

**Objective:** To have the highest value of Stored/Saved poker hands once all cards have been discarded.

---

## Setup
1. **Deck**: Use one standard deck of playing cards for every 3 players.
2. **Deal Cards**: Each player is dealt 7 cards.
3. **Treasure Deck**: Place 9 cards face-up in the center of the table. This is called the treasure deck.
4. **Main Deck**: Place the remaining cards face-down in a pile next to the treasure deck. This is called the main deck.

---

## Gameplay

**Turns**: Players take turns in a clockwise order. On each turn, a player can perform one of the following actions:

1. **Deck**: Draw 1 card from the main deck.
2. **Hoard**: Swap one of your cards with a card from the treasure deck.
3. **Challenge**: Challenge an opponent to a poker hand duel.

### Challenge Rules
- **Initiating a Challenge**:
  - The challenging player selects an opponent and declares the number of cards (minimum 3, maximum 5) they wish to use in the challenge.
  - Both players reveal their hands simultaneously, and the winner is determined based on standard poker hand rankings.
  
- **Winning a Challenge**:
  - The winner gets to draw a number of cards equal to the value of the winning hand (e.g., a pair counts as 2, three-of-a-kind as 3, etc.) from either the treasure deck or the main deck.
  - Cards drawn from the treasure deck must be replaced with cards from the main deck.

### Special Action - Store/Save:
- Players can discard any valid 5-card poker hand to Store/Save it.
- Stored/Saved hands are placed out of the game.
- This action does not count as the player's turn, so they can still perform one of the three main actions.

---

## Winning the Game

The game ends when all cards have been discarded. The player with the highest value of Stored/Saved poker hands is the winner.

---

## Additional Rules

1. **Visibility**: All players can see the cards in the treasure deck.
2. **Replacement of Treasure Deck Cards**: When cards are taken from the treasure deck, they must be replaced by drawing from the main deck.
3. **Card Counts in Challenges**: The challenging player can pick any number of cards to challenge with, as long as the opponent has enough cards to match the challenge.
4. **Max Cards**: Each player is limited to no more than 13 cards in their hand at one time. Subsequent actions must not cause the player to exceed this number (i.e. `Deck` would be an invalid). If the player has `exactly 13` cards, they may swap cards upon a successful `Challenge`, otherwise normal rules apply.
5. **Lock Conditions**: If there are no more cards in the treasure or main deck, and all challenges are looping, each player should create the best 5 poker hand they can to end the game. If there are no valid 5 poker hands that can be made, their value is 0.

---

## Poker Hand Rankings

Use standard poker hand rankings to determine the winner of challenges:
1. **High Card**
2. **Pair**
3. **Two Pair**
4. **Three of a Kind**
5. **Straight**
6. **Flush**
7. **Full House**
8. **Four of a Kind**
9. **Straight Flush**
10. **Royal Flush**

***

## Implementation

This Python implemenation currently only includes a `CLI`, though it can be easily expanded using the `UserInterface` class.
