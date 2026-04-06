import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        player_name = input("What is your name, adventurer? ")
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        player_details = {
            "name": player_name,
            "health": 10,
            "inventory": []
        }
        # TODO: Return the dictionary
        return player_details


    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasures = {
            "gold coin": 5,
            "ruby": 10,
            "ancient scroll": 7,
            "emerald": 9,
            "silver ring": 4,
            "polished chipped sword": 8
        }

        traps = {
            "spike trap": 3,
            "poison trap": 1,
            "flame trap": 2,
            "bomb trap": 5,
            "crushing room trap": 10
        }
        # TODO: Return the dictionary
        return treasures, traps


    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
        print(f"""
              
            You are in room {room_number}.

            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game

        """)


    def search_room(player, treasures, traps):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        outcome = random.choice(["treasure", "treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened
        if outcome == "treasure":
            found_treasure = random.choice(list(treasures))
            player["inventory"].append(found_treasure)
            print(f"You found a {found_treasure}!")
        else:
            found_trap = random.choice(list(traps))
            player["health"] -= traps[found_trap]
            print(f"You stumbled onto a {found_trap} and got hurt! Lost {traps[found_trap]} health points...")
            


    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        print(f"Your current health: {player['health']}")
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”
        if len(player["inventory"]) == 0:
            print("You have no items yet")
        else:
            print("Your current inventory: " + ", ".join(player["inventory"]))


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        total_value = 0
        for item in player["inventory"]:
            total_value += treasures[item]
        # TODO: Print final health, items, and total value
        print(f"""
              Final health: {"0" if player["health"] < 0 else player["health"]},
              Final inventory: {"no items collected"if len(player["inventory"]) == 0 else ", ".join(player["inventory"])},
              Inventory value: {total_value}
              """)
        # TODO: End with a message like "Game Over! Thanks for playing."
        print("Game Over! Thanks for playing.")


    def run_game_loop(player, treasures, traps):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        for room in range(1, 6):
            room_searched = False
        # TODO: Inside each room, prompt player choice using input()
            while True:
                display_options(room)
                choice = input("Enter your choice: ")
        # TODO: Use if/elif to handle each choice (1–4)
                if choice == "1":
                    if not room_searched:
                        search_room(player, treasures, traps)
                        room_searched = True
                        if player["health"] <= 0:
                            print("Your health has reached 0, and you soon became another skeleton within the dungeon...")
                            end_game(player, treasures)
                            return
                    else:
                        print("You have already searched this room, you only find the same cobwebs.")
                    # break
                elif choice == "2":
                    break
                elif choice == "3":
                    check_status(player)
                    # break
                elif choice == "4":
                    end_game(player, treasures)
                    return
                else:
                    print("That is an invalid option, please choose an option between 1 and 4: ")
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored
            if room >= 5:
                end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures, traps = create_treasures()
    run_game_loop(player, treasures, traps)

if __name__ == "__main__":
    main()
