# Maze Runner
First project in Digital Business Line Training at Obechar 2023. The project aims to support everyone to get used to with popular tools in software development, a basic workflow of a website and SCRUM.

## Prerequisites
Before working on the project, you need to have a good understanding about git. Belows are the things you need to do first:
- Fork this repo to your team's repository.
- Learn to use basic commands of git including `git clone`, `git add`, `git commit`, `git push`.
- Learn the basic workflow of a git (especialy common branches and their usages) and supported commands for this. The commands are `git checkout`, `git merge`, `git rebase`, `git branch`.
- Learn to track and control your commits with `git status`, `git reset --hard`, `git reset --soft`, `git diff`.

Next, download an IDE to support your coding. The recommended is VSCode. If you select VSCode, try to install some popular extensions to support your development with Python and git.

## Let's start your first step with Maze Runner
In Maze Runner, your team will try to develop a bot which try to find the shortest path in a maze to collect coins. At the end of the project, we will host a battle between two bots of two teams to find the winner. Try your best!

### maze_metadata.json
The map of the maze is respresented in a simple .json file. This file contains the metadata (well, if you don't know what is this, search it!) and from this file, all other components can understand and interact with the maze. The format of the file is like this example:
```json
{
    "width": 10,
    "height": 10,
    "obstacles": [[0, 1], [1, 1], [2, 1]],
    "bot": [5, 8],
    "coin": [0, 0]
}
```

Here, the `width` and `height` represent the size of the map, `obstacles` is a list of coordinate (row_index, column_index) of cells that are occluded, `bot` is the position (like obstacles) of the bot, and `coin` is the position (the same with bot) of the coin.

So, from the above example, a maze may looks like:
```
************
*o*        *
* *        *
* *        *
*          *
*          *
*        X *
*          *
*          *
*          *
*          *
************
```
REMEMBER, this is just a simple example. The real one is very challenging!

### bot.py

Let's develop bot.py which represents as your bot. What it does is to read the **maze_metadata.json** and write the next action to a file named `action.txt` iteratively. The command line to run bot.py in terminal must follow this:

```
python bot.py -i maze_metadata.json -o action.txt
```
Here, the `-i` is an argument which defines the input file, and `-o` defines the output file.

The bot must only send 1 action for each step, after only when the position of the bot in **maze_metadata.json** is changed. The action must be either `left`, `right`, `up` or `down`. The output action is represented by an **action.txt** file. For example, with the given metadata, the bot might plan a path to go left, up, left, down, right and so on. The action.txt in this case will be like:

``` txt
  left
  up
  left
  down
  right
```
Each line is equivalent to an action at each step.

Try your best to minimize the number of actions required to reach the coin in a short inference time!

*Keywords*: **argparse** , **BFS**, **DFS**, **Dijkstra**   

### maze_updater.py

This component receives the **action.txt** file and commits the action by update the `bot` in **maze_metadata.json** file. The command line to run **maze_updater.py** in terminal must follow this:
```
python maze_updater.py -i action.txt -o maze_metadata.json
```
Here, the `-i` is an argument which defines the input file, and `-o` defines the output file.

The loop of reading metadata, indicating action and updating metadata keeps the bot moving continuously in the maze until the bot get the coin. For instance, in the first step, with the given **maze_metadata.json** and **action.txt**, **maze_metadata.json** is updated like follow:
```json
{
    "width": 10,
    "height": 10,
    "obstacles": [[0, 1], [1, 1], [2, 1]],
    "bot": [5, 7],
    "coin": [0, 0]
}
```
But the game does not end there, this function will also update the new position of the coin in the maze when the last coin disappear by generating the `coin`'s position randomly. So continue with the example, when the `bot` reach `[0;0]` then `coin` could be:
```json
{
    "width": 10,
    "height": 10,
    "obstacles": [[0, 1], [1, 1], [2, 1]],
    "bot": [0, 0],
    "coin": [7, 4]
}
```

And the game goes on and on.

### maze_displayer.py
We can not just run our software without any validation. One of the best way is to develop a user-friendly UI for it. Design your own UI for maze runner and implement it withih **maze_displayer.py**. A good UI should have following:
- Show the structure of the map.
- Show the position of the coin and the bot.
- Show the current step of the process.

For example, a simple UI could be like this:
```
Step 0
************
*o*        *
* *        *
* *        *
*          *
*          *
*        X *
*          *
*          *
*          *
*          *
************
Step 1
************
*o*        *
* *        *
* *        *
*          *
*          *
*       X  *
*          *
*          *
*          *
*          *
************
Step 2
************
*o*        *
* *        *
* *        *
*          *
*          *
*      X   *
*          *
*          *
*          *
*          *
************
```
*Keywords*: **pygame**, **tkinter**

### Multi-agent
Playing alone can not be as fun as playing with friends. Let's transform our maze into a playground so everyone can join. 
#### Protocols
In this part, we will update our ,json and .txt files to enable competitive mode for multiple bots. Initially, we need to work on field `bot` in **maze_metadata.json**. Because there could be more than 1 bot, and some bots can faster than the other, we need to change the format of `bot` to a better representative version. Thus, the `bot` needs to be `bots` which is a list of dictionary of each bot like the followings:

**maze_metadata.json**
```json
{
    "width": 10,
    "height": 10,
    "obstacles": [[0, 1], [1, 1], [2, 1]],
    "bots": [
    {
      "name": "could be any name",  # NEW. Yeah, so now we can name our bot
      "pos": [5, 7],
      "status": "stop",  # NEW
      "score": 10  # NEW
    },
    {
      "name": "other any name",
      "pos": [3, 3],
      "status": "move",
      "score": 4
    }],
    "coin": [0, 0],
    "screen": true  # NEW
}
```
Here, "status" is like a green and red light for the bot, it tells which bot when to move and stop. So, **IMPORTANT** here, the `bot.py` only update their `action.txt` when all of the bots are allowed to move!!!

The "screen" 's usage will be explained in the Back-end and Front-end. And for the "score", well, you know what it should be.

For the `action.txt`, because each bot has different action. So now the `action.txt` should represent the bot individually by name the file by the name of the bot (Exp: conan.txt and songoku.txt). And the format should follow:

```
left 123.12
up 50.34
left 49.50
down 49.45
right 45.50
```
The value next to action is the inference time (in milliseconds) is calculated FROM the time before the bot read the map TO the time after it decides the next action.

#### Back-end (maze_updater.py) and Front-end (maze_displayer.py)
*maze_updater.py* now needs to be able to read multiple *action.txt*, hence, the command line should be updated like this:
```bash
python maze_updater.py -i conan.txt -i songoku.txt -o maze_metadata.json
```
A new rule to update metadata now is prioritizing the bot which has least inference time at a step to move first, and apply this rule for the rest. 

So for example, in this case:

**conan.txt**
```
left 123.12
```
**songoku.txt**
```
up 1.00  # Yeah, of course, he's Songoku.
```
**maze_updater.py** should update the position of the songoku first, and then the conan.

One more thing, to let **maze_updater.py** aware if the **maze_displayer.py** already displayed the new position or not, **maze_displayer.py** now will need to update the "screen" in metadata to true or false. If "screen" is True, new position is updated on the screen and now the **maze_updater.py** can update the new position of the other bots.

In summary, for the above expample, a whole workflow would look like this:
1. Bots update their action.
2. BE read action files, set all the status of the bot to "stop" and start to update metadata in the order of inference time of each bot.
```
# Order of update
songuku > conan
```
3. When update metadata for a bot, besides update their position, we also switch the "screen" to false.
4. **maze_displayer.py** reads metadata and update the new screen, whereas **updater** wait until **displayer** finish by checking the "screen" in metadata. If "screen" is True, the BE now can update to the next bot.

5. When all bot are already updated, switch the status of all bots to move to allow them to update their next action.

**NEW RULE: BLOODY WAR**

A bot can not move to an occupied slot if the slot is occupied by another bot. If the bot move to that slot, it will be killed and **updater** switch the "status" of that bot to "eliminated" and never care about that bot anymore.

#### Front-end
Besides to display multiple bot in a map (each bot should have different shape or color), now the map should also show the score of each bot on the screen. Because the bot can be eliminated, FE should display a dummy effect to eliminated bot. 

#### AI
**IMPORTANT** YOU CAN NOT STEP ON THE OCCUPIED SLOT. If you move to a slot where is occupied by other bot, you will be ELIMINATED OUT OF THE GAME!!!
In this competition, luck is very important, but we can reduce our dependency on the luck by a good strategy. Don't just close your eyes and only move to where the coin is. Knowing where the enemy is could give you good strategy.

---
We look forward to seeing not only your amzing results and a thrilling race but also your development through this very first project. Good luck!
