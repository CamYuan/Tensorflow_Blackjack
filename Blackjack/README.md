BLACKJACK
PreGame:
  - Set up a cardShoe with 6-8 decks.
  - Put a cutCard in the deck somewhere in the back of the shoe (last 30%)


1. Players place bets
    - Players can bet between the table min and max
    - Players cannot bet more money than they have
    - Immediately remove their bet from their bankroll
    - Players may place side bets
        - Bottom 3 bet
        - Top 3 bet cannot be placed if bottom 3 is not placed
2. Deal 2 cards to each player and the dealer.
    - Deal 1 card to each person rotating clockwise.
    - Deal the first dealer card face down.
    - 2nd dealer card is face up
    - All player cards are face up
    - Each player and dealer should all have only 1 hand each
3. Check the dealer's hand for blackjack
    - If the dealer has blackjack, all players who do not also have blackjack lose and the dealer takes their bet
4. Check players hands for blackjack (2 cards with value 21. Only on initial hand)
    - If the player has blackjack, they win immediately for 1.5x their bets
    - Players cannot hit more cards if they have blackjack
5. Clockwise, each player makes some choices about their hand(s)
    - A player may Stand (take no more cards and pass priority to the next player)
    - A Player may hit (get an additional card)
        - If the cutCard is drawn, this will be the last hand played and the shoe will be shuffled
        - After taking a hit, check the value of the players hand
            - If their hand value is over 21, they BUST and immediately lose their bet to the dealer
            - They may no longer split or double down
    - A player may split (their hand becomes two hands)
        - Their cards must be the same rank to split
        - After splitting, they will be dealt 1 card on their first hand, play through that hand, then they will be dealt another card on their second hand
        - Splitting Aces may only be done once (An AA hand that was created from an already split AA hand cannot be split again)
        - Getting 21 on a split hand is not a natural blackjack, so it will only payout 1x their bet
        - Splitting Aces will only bet dealt 1 card on split aces (they cannot hit any more cards)
    - A player may double down (Make an additional bet, take a single additional card, then stand)
        - Players may only double down on their initial two cards
6. After all players have made decisions, show the dealer's hand and act accordingly
    - Dealer must hit on anything under 17
    - Dealer stays on a soft 17. (Some Casinos still hit)
    - If the dealer BUSTS, all remaining players win
7. Calculate the values of all hands for everyone who has not BUST and not BLACKJACK
    - If the player has more value than the dealer, they WIN and get 1x their bet
    - If the player has the same value as the dealer, they PUSH and keep their bet
    - If the player has less than the dealer, they LOSE and the dealer takes their bet
8. At this point, all players should have paid up or been paid out. Discard all hands and get ready for the next round



TODO: Convert to Json... why wasn't I doing this to begin with?
TODO: implement double down betting
-TODO: implement payouts
TODO: write better unit tests






TODO: Generate Test data for basic Feed Forward Neural Net
    -Feed forward networks have no 'memory' so each hand state
    will act like an independent hand
TODO: Train Neural Net on test data
TODO: Train Neural Net based on Win/Loss to see if it comes up with the same basic strategy
TODO: Add logic for double downs and splits
TODO: Re-do Neural Net with new information
TODO: Implement Hi-Lo Card Count and other card counting systems
TODO: Test Nueral net efficiency with new information
TODO: Implement RNN with all information.
TODO: Test different training strategies and see what is best
TODO: Build Neural Net for betting strategies
TODO: Throw it all together in a DQRNN maybe
