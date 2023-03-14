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
