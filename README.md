
# Project Overview

## Introduction

This project involves the adaptation of the video game *The Talos Principle* into a text-based experience for an AI using Python 3.11.7. The game has been converted into a sequence of textual scripts that describe various scenarios, decisions, and interactions within the game. The AI engages with this textual environment by choosing from predefined options, leading to different outcomes and simulating the gameplay through a text-based interface.

### Example Scenario

For instance, during gameplay, the AI might encounter the following scenario:
```
You go ahead and enter the second circle of light, which should bring you to the next level. As the light dissipates, you find yourself in another setting made of ancient ruins resembling Mediterranean culture. You find a functioning IAN terminal. Do you want to use it?
```
The AI is then presented with the following options:
1. Yes
2. No

The AI selects an option through an API, which influences the narrative's progression and the game’s outcomes. This setup allows the AI to navigate *The Talos Principle* through a purely text-based interface, enabling observation of its decision-making process.

We have strived to ensure accuracy based on our gameplay experiences and the available game files.

## Instructions

### Running the Code

To execute the project, run the main script:
```
python main.py
```

### Configuration

- By default, the `self.bot` variable in the `Game` class within `main.py` is set to `False`, allowing manual gameplay via the terminal for testing purposes.
- Setting `self.bot` to `True` enables the `get_input()` function to automatically receive input from the `interaction(prompt)` function defined in `API.py`.

The code is currently configured for the Gemini 1.5 Flash API. To use a different API, modify `API.py` and adjust the `interaction(prompt)` function as necessary.

### Saving Progress

Progress is saved in text files (`A.txt`, `B.txt`, or `C.txt`) at the end of each game section (buildings A, B, and C). These files store the game history up to that point to prevent data loss. After completing the game, an `output.txt` file will be created containing the entire game history, allowing you to safely delete the `A.txt`, `B.txt`, and `C.txt` files.

## Sources

The information used in the project comes from:
1. **Conversations with the Terminal:** `.dlg` files in the `ComputerTerminalDialogs` folder.
2. **Terminal Booklet Texts:** `Talos_Terminal_Booklet.pdf` included in the game files.
3. **QR Codes:** Referenced from [Steam Community](https://steamcommunity.com/sharedfiles/filedetails/?id=652167581).
4. **Time Capsule Locations:** Referenced from [Steam Community](https://steamcommunity.com/sharedfiles/filedetails/?id=356003215).
5. **Time Capsule Content:** Referenced from [Steam Community](https://steamcommunity.com/sharedfiles/filedetails/?id=2378756869).
6. **Additional Information:** Derived from gameplay.

These sources are integrated into the `sources.py` file and organized in the [flow diagram](https://github.com/marcoseverini/talos-principle-ai-simulation/blob/main/FlowDiagram.drawio).


## Puzzles

The puzzle element, crucial to the game's experience, has been retained. Several math and logic puzzles are included in the `enigma_list[]` within the `sources.py` file. Currently, only the first puzzle in the list is used repeatedly, as other puzzles have not yet been tested with the AI or ordered by increasing difficulty. This limitation is planned to be addressed in future updates.

## Additional Notes

The AI is designed to have maximum freedom of choice to enhance realism. It can decide whether to interact with elements such as terminals, QR codes, and time capsules. Additionally, the AI has the option to generate a custom QR code (a message to display on the wall) at each level.

## Tests Performed

[tests](https://github.com/marcoseverini/talos-principle-ai-simulation/tree/main/tests) folder includes two test cases conducted with the Gemini 1.5 Flash AI. Review these tests to observe the AI's performance in those scenarios. In one, the AI ​​got the tower ending. In the other, the ending of paradise. Draw your own conclusions, and enjoy reading them.

## Team

- **Marco Severini:** Code Development
- **Davide Rozmarynowski:** Transformation of the game into textual scripts

##

                                ...',;;:cccccccc:;,..
                            ..,;:cccc::::ccccclloooolc;'.
                         .',;:::;;;;:loodxk0kkxxkxxdocccc;;'..
                       .,;;;,,;:coxldKNWWWMMMMWNNWWNNKkdolcccc:,.
                    .',;;,',;lxo:...dXWMMMMMMMMNkloOXNNNX0koc:coo;.
                 ..,;:;,,,:ldl'   .kWMMMWXXNWMMMMXd..':d0XWWN0d:;lkd,
               ..,;;,,'':loc.     lKMMMNl. .c0KNWNK:  ..';lx00X0l,cxo,.
             ..''....'cooc.       c0NMMX;   .l0XWN0;       ,ddx00occl:.
           ..'..  .':odc.         .x0KKKkolcld000xc.       .cxxxkkdl:,..
         ..''..   ;dxolc;'         .lxx000kkxx00kc.      .;looolllol:'..
        ..'..    .':lloolc:,..       'lxkkkkk0kd,   ..':clc:::;,,;:;,'..
        ......   ....',;;;:ccc::;;,''',:loddol:,,;:clllolc:;;,'........
            .     ....'''',,,;;:cccccclllloooollllccc:c:::;,'..
                    .......'',,,,,,,,;;::::ccccc::::;;;,,''...
                      ...............''',,,;;;,,''''''......
                           ............................

