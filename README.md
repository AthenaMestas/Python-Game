# 
Language: 

## 💡Overview
- 

## 🗝️Key Features
- Comprehensive Analysis
  - 
- Code Quality Highlights
  - 
- Technical Achievements
  - 

## ⚙️Technologies Used
- Language: 
- Tools: 

## 📈Future Improvements
- 






# Python Game Program
# What were the primary components of the interactive game?
In the interactive Martha Stewart Kitchen Escape game, players navigate a house to collect absurd items/tools needed to defeat Martha, such as nunchucks and spoiled milk. While collecting these items and blindly navigating the text-based world, users must avoid entering the Kitchen - where Ms. Martha resides - until fully prepared (by collecting all items). Once fully prepared and entering the Kitchen, a battle commenses and all items collected are strategically used. Primarily, the user can naigate between rooms with directional inputs north, south, east, and west. If there is an un-obtained item in a room, the user may enter the item's name to pick it up and put it in their inventory.
# What were the program's strengths?
The organization of the code structure, creative problem-solving, and user-friendly design were core strengths of the game. The separated dictionaries for rooms, storyline and UI elements made for an easy-to-read script and functions such as show_status centralize game status checks. Within creative problem-solving, to appropriately model room connections, nested dictionaries were implemented. In addition, to carefully track items, global variables (room_item) were employed. To enhance the user-friendly design, clear instructions were given with show_instructions() and input validations loops were used to prevent crashes.
# What are the main areas for improvement in the application?
Regarding areas of improvement, the game could have benefitted from additional error handling and architecture modifications for scalability. In addition to more robust validations for room transitions, try-except blocks for file I/O would help if the user saves progress. Aiming for scalability, the code could approach the idea differently by using classes for rooms/players to reduce the global variables used. Also, the data used for rooms could be moved to JSON for easier level editing.
