![treeio](img/treeio_textlogo.png)

# Tree.io
Tree.io is a app that can create a network visualization of pairwise relations between various topics.  The app currently scrapes Wikipedia to build its lists, so there must be a wikipedia page about the topic for the program to work! In the future, I hope to increase the available topics!

Tree.io can be used to see the relationship one topic has to with another.  Starting with the "origin" topic, the tree.io app will find topics related to the origin topic, called edges.  From these edges, more edges will be created until the app hits its depth limit. (the max amount of "levels" from the origin topic)

## How to use:

Currently, there is no UI for this.  You must go into tree.py and edit create_tree('topic', 1, 50) --- replacing 'topic' with whatever you wish to find a topic on.

You can then run create_newtwork.py, this will create a matplotlib plot.

Currently working on a plotly solution, which will make things smoother as plotly can handle many more datapoints!
