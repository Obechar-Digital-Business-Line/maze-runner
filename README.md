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