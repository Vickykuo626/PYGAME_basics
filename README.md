# Python_Game: 利用PYGAME module 自己創造的小遊戲

**_1. References_**
   1. Pygame Page: http://pygame.org
   2. documentation: http://pygame.org/docs/ref/
   3. Icon Archive: https://iconarchive.com/  (download game charactors)
   4. Leshy SFMaker: https://www.leshylabs.com/apps/sfMaker/ <br><br>
------

**_2. What is PYGAME_**:
   * Pygame provides "Display,Sound,Image,Text,Event" to create games
   * Pygame can create 2-D games
   * Pygame detects users using "Keyboard, jjoystick,mouse" to control the games
   * Pygame provides lots of built-in game objects to create the games <br><br>

**_3.PYGame Basics_**:
| code | Description |
|:-----:|:----------:|
| _1.py_ | Create my game surface, game loop and drawing.|
| _2.py_ | Blit text, font, sound and image objects.   |
| _3.py_ | Getting uuser keyboard and collision dection.|

**_4. Code snippet_**
```python
#Create game display
import pygame#遊戲模組 載入pygame module
pygame.init()#遊戲模組啟動
WINDOW_WIDTH,WINDOW_HEIGHT=800,600
displayscreen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))#產生畫布
pygame.display.set_caption("My first pygame!")

```
   
