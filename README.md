# Maze Runner
First project in Digital Business Line Training at Obechar 2023. The project aims to support everyone to get used to with popular tools in software development, a basic workflow of a website and SCRUM.

## Prerequisites
Before working on the project, you need to have a good understanding about git. Belows are the things you need to do first:
- Fork this repo to your personal repositories.
- Learn to use basic commands of git including `git clone`, `git add`, `git commit`, `git push`.
- Learn the basic workflow of a git (especialy common branches and their usages) and supported commands for this. The commands are `git checkout`, `git merge`, `git rebase`, `git branch`.
- Learn to track and control your commits with `git status`, `git reset --hard`, `git reset --soft`, `git diff`.

Next, download an IDE to support your coding. The recommended is VSCode. If you select VSCode, try to install some popular extensions to support your development with Python and git.

## Let's start your first step with Maze Runner
In Maze Runner, your team will try to develop a bot which try to find the shortest path in a maze to collect coins. At the end of the project, we will host a battle between two bots of two teams to find the winner. Try your best!

### maze_metadata.json
The map of the maze will be respresent in a simple .json file. This file will contain the metadata (well, if you don't know what is this, search it!) and from this file, all other components can understand and interact with the maze. The format of the file is like this example:
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

After having the map represented in .json file; here comes the interesting part, this component (called bot.py) will read the metadata and indicate the next action. Here is an example of the function:

```
python bot.py -i maze_metadata.json
```

The bot must only send 1 action for each step and this action must be either `left`, `right`, `up` or `down`. The output action is represented by an **action.txt** file. For example, with the given metadata, the bot might want to go left and the action.txt will be like:

``` txt
  left
```

The goal of this project is to minimize the number of action required to reach the coin. So try your best with the algorithms!

Here are some hints for building this component: **BFS**, **DFS**, **Dijkstra**    

### maze_updater.py

This component will receive the **action.txt** file and commit the action by adjust the `bot` parameter in **maze_metadata.json** file. The function format is like this example:
```
python maze_updater.py -i action.txt
```

The loop of reading metadata, indicating action and updating metadata keeps the bot moving continuously in the maze until the bot eats the coin. For instance, with the given metadata and action, the output of this function is like follow:
```json
{
    "width": 10,
    "height": 10,
    "obstacles": [[0, 1], [1, 1], [2, 1]],
    "bot": [5, 7],
    "coin": [0, 0]
}
```
But the game does not end there, this function will also update the new position of the coin in the maze when the last coin disappear by adjusting the `coin` parameter. So continue with the example, when the `bot` reach `[0;0]` then `coin` will be adjusted randomly:
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

We look forward to seeing not only your amzing results and a thrilling race but also your development through this very first project. Good luck!

**_DO YOUR BEST, THE REST WILL COME!_**
