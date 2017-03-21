Flappy Bird Bot using Reinforcement Learning in Python
===================
![4000+ scored](http://i.imgur.com/00Mf320.png)

A Flappy Bird bot in Python, that learns from each game played via Q-Learning.

[Youtube Link](https://www.youtube.com/watch?v=79BWQUN_Njc) 

### How it works

With every game played, the bird observes the states it has been in, and the actions it took. With regards to their outcomes, it punishes or rewards the state-action pairs. After playing the game numerous times, the bird is able to consistently obtain high scores. 

A reinforcement learning algorithm called [Q-learning](https://en.wikipedia.org/wiki/Q-learning) is utilized. This project is heavily influenced by the [awesome work of sarvagyavaish](http://sarvagyavaish.github.io/FlappyBirdRL/),  but I changed the state space and the algorithm to some extent. The bot is built to operate on a modifed version of the [Flappy Bird pygame clone of sourabhv](https://github.com/sourabhv/FlapPyBird).

----------
We define the state space and action set, and the bird uses its experiences to give rewards to various state-action pairs.

I defined the states a little different from sarvagyavaish. In his version **horizontal and vertical distances from the next pipe** define the state of the bird. When I wrote the program to work like this, I found that convergence takes a very long time. So I instead discretized the distances to **10x10 grids**, which greatly reduces the state space. Moreover, I added **vertical velocity of the bird** to the state space.

I also changed the algorithm a bit. Instead of updating Q-values with each experience observed, I went backward  after each game played. So, **Q-values are calculated going backwards from the last experience to first**. I figured this would help propagate the “bad state” information faster. In addition if the bird dies by **collapsing to the top-section of a pipe**, the **state where bird jumped** gets flagged and is punished additionally. This works nice, since dying to the top-section of the pipe is almost always the result of a bad jump. The flagging helps propagating the information to this ‘bad’ [s,a] pair quickly.

![Learning Graph](http://i.imgur.com/Xm8WPYk.png)

As it can be seen, after around 1500 game iterations, the bot learns to play quite well, averaging about 150 score, and also occasionally hitting very good max scores.

----------
### Update

With **5x5 grids** instead of 10x10 (and also **y velocity** still in the state space), the convergence takes longer, but it converges to around 675 score, significantly beating the 150 score of the previous run. Also, the bird is able reach very high scores (3000+) quite many times.

![Learning Graph II](http://i.imgur.com/E3Vy0OR.png)


**Credits**

https://github.com/sourabhv/FlapPyBird

http://sarvagyavaish.github.io/FlappyBirdRL/

https://github.com/mihaibivol/Q-learning-tic-tac-toe
