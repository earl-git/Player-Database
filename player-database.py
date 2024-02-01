
import sqlite3

def menu():
    print("\nPlayer Manager\n")
    print("\nCOMMAND MENU")
    print("view - View Player")
    print("add - Add a  Player")
    print("update - Update player info")
    print("del - Delete a Player")
    print("exit - Exit Program\n")

def main():
    # Connect to the database
    conn = sqlite3.connect('players_Data.db')
    c = conn.cursor()

    # Create the Player table 
    c.execute('''CREATE TABLE IF NOT EXISTS Player
                 (Name TEXT NOT NULL, Wins INTEGER NOT NULL, Losses INTEGER NOT NULL, Ties INTEGER NOT NULL)''')
    
    menu()
    
    while True:
        command = input("Command: ")
        if command == 'view':
            c.execute("SELECT * FROM Player ORDER BY Wins DESC")
            players = c.fetchall()
            print("Name\tWins\tLosses\tTies\tGames")
            print("-" * 50)
            for player in players:
                games = player[1] + player[2] + player[3]
                print(f"{player[0]}\t{player[1]}\t{player[2]}\t{player[3]}\t{games}")
        elif command == 'add':
            name = input("Name: ")
            wins = int(input("Wins: "))
            losses = int(input("Losses: "))
            ties = int(input("Ties: "))
            c.execute("INSERT INTO Player (Name, Wins, Losses, Ties) VALUES (?, ?, ?, ?)", (name, wins, losses, ties))
            conn.commit()
            print(f"{name} was added to the database")
        elif command == 'del':
            name = input("Name: ")
            c.execute("SELECT * FROM Player WHERE Name= ?", (name,))
            user = c.fetchone()
            if user:
                c.execute("DELETE FROM Player WHERE Name=?", (name,))
                conn.commit()
                print(f"{name} was deleted from the database")
            else:
                print(f"{name} does not exist in the database")
        elif command == 'modify and delete': 
            name = input("Name: ")
            c.execute("SELECT * ")
        elif command == 'update':
            name = input("Name: ")
            c.execute("SELECT * FROM Player WHERE Name=?", (name,))
            user = c.fetchone()
            if user:
                wins = int(input("Wins: "))
                losses = int(input("Losses: "))
                ties = int(input("Ties: "))
                c.execute("UPDATE Player SET Wins=?, Losses=?, Ties=? WHERE Name=?", (wins, losses, ties, name))
                conn.commit()
                print(f"{name}'s data was updated")
            else:
                print(f"{name} does not exist in the database")
        elif command == 'exit':
            break
        else:
            print("Invalid command!")

    # Close the connection
    conn.close()

    print("Bye!")

if __name__ == '__main__':
    main()
