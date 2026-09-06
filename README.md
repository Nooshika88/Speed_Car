# 🏎️ Speed Racers

**Speed Racers** is a 2D racing and action game built with **Python** and **Pygame**. The player controls a yellow car, avoids enemy vehicles, and shoots a ball at them to earn points while trying to survive.

The main objective is to reach **at least 10 points after surviving for one minute**. If the player's health reaches zero, the game ends and the player can restart.

---

## 🎮 Features

- 🏎️ Player-controlled racing car
- 🚗 Four enemy cars with sequential movement
- ⚽ Ball shooting mechanic
- ❤️ Health system and health bar
- ⭐ Score system
- ⏱️ In-game timer
- 💥 Collision detection
- 🔊 Background music and sound effects
- 🔄 Restart system
- 🏁 Start, Victory, and Game Over screens
- 🎨 Custom images, UI elements, and game assets

---

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **Pygame** | Game window, graphics, input, movement, collision detection, audio, and timing |
| **Random** | Randomized enemy-car positions |

### Imports

```python
import pygame
import random
```

---

# 🧠 Game Algorithm

The game is built around a continuous **Game Loop**. During every frame, the program handles input, updates the game state, checks collisions, draws the scene, and evaluates the win or Game Over conditions.

```text
Start Game
    ↓
Handle Player Input
    ↓
Update Timer
    ↓
Move Background
    ↓
Move Player
    ↓
Move Enemy Cars
    ↓
Move Ball
    ↓
Check Collisions
    ↓
Update Score & Health
    ↓
Draw Game
    ↓
Check Win / Game Over
    ↓
Repeat
```

---

## 1. 🎬 Start Screen

Before the game begins, a custom start screen is displayed.

The player clicks the **START** button to enter the game. The button is implemented using `pygame.Rect`, while `pygame.event.get()` is used to detect mouse input.

---

## 2. 🕹️ Player Controls

The player's yellow car is controlled using the keyboard:

| Key | Action |
|-----|--------|
| `←` | Move left |
| `→` | Move right |
| `↑` | Move forward |
| `SPACE` | Shoot |

Keyboard input is handled with `pygame.key.get_pressed()`.

The player's horizontal position is restricted to the road boundaries:

```python
car_yellow_x = max(390, min(770, car_yellow_x))
```

This prevents the player's car from leaving the playable road area.

---

## 3. 🚗 Enemy Car Algorithm

The game contains four enemy cars. Instead of moving at the same time, they are activated **one after another**.

```text
Car 1 → Car 2 → Car 3 → Car 4 → Car 1 → ...
```

Boolean variables control which car is currently active:

```python
car1_go = True
car2_go = False
car3_go = False
car4_go = False
```

When the active car moves beyond the bottom of the screen, it is reset to the top and the next enemy car becomes active.

This creates a simple **sequential enemy movement algorithm**.

---

# ⚽ Shooting Algorithm

The player can shoot a ball by pressing `SPACE`.

Only one ball can be active at a time. When the player shoots, the ball starts at the player's current position:

```python
ball_x = car_yellow_x + 15
ball_y = car_yellow_y
ball_active = False
```

The ball then moves upward:

```python
ball_y -= ball_speed * dt
```

When the ball leaves the screen, it is reset and becomes available for the next shot.

---

# 💥 Collision Detection

Collision detection is implemented with `pygame.Rect` and the `colliderect()` method.

For example:

```python
if ball_rect.colliderect(car_rect):
```

This checks whether the ball's rectangle intersects with an enemy car's rectangle.

### Ball vs. Enemy Car

When the ball hits an enemy car:

```text
Enemy Hit
   ↓
Score +1
   ↓
Enemy Car Reset
   ↓
Ball Reset
```

A window-smash sound effect is also played.

---

# 🚧 Player Collision

When the player's car collides with an enemy car:

```text
Player Crash
    ↓
Health -10
    ↓
Score -1
    ↓
Enemy Car Reset
```

A crash sound effect is played whenever a collision occurs.

The health value is prevented from becoming negative:

```python
health = max(0, health - damage_per_crash)
```

---

# ❤️ Health System

The player's health starts at **100**.

Each collision with an enemy car causes **10 points of damage**.

The health bar is drawn dynamically according to the current health:

```python
health_width = int(200 * (health / max_health))
```

As the player's health decreases, the visible health bar becomes shorter.

---

# ⭐ Score System

The scoring system is simple:

| Action | Score Change |
|--------|-------------:|
| Hit an enemy car | `+1` |
| Crash into an enemy car | `-1` |

The current score is displayed on the game screen.

---

# ⏱️ Time System

The game timer is calculated using `pygame.time.get_ticks()`.

The elapsed time is converted from milliseconds into minutes and seconds and displayed in the following format:

```text
00:45
01:12
02:30
```

The timer starts when the game begins and is reset when the player restarts the game.

---

# 🏆 Winning Condition

The player wins when **both** of the following conditions are true:

```text
Time >= 60 seconds
AND
Score >= 10
```

In other words, the player must survive for at least one minute and earn at least 10 points.

When the player wins, the background music stops and the custom Victory screen is displayed for a few seconds.

---

# 💀 Game Over

The game ends when the player's health reaches zero:

```python
if health <= 0:
```

The Game Over screen displays:

- Final score
- Total game time
- Restart button

The player can restart by clicking **RESTART** or pressing `ENTER`.

Pressing `ESC` exits from the Game Over screen.

---

# 🔄 Reset System

The `reset_game()` function returns the game to its initial state without closing the program.

It resets values such as:

```text
Score       → 0
Health      → 100
Player      → Initial position
Enemies     → Initial positions
Ball        → Reset
Background  → Reset
Timer       → Restart
```

This allows the player to start a new round immediately after Game Over.

---

# 🎨 Graphics & Audio

The project uses external image and audio assets for the game environment and feedback.

### Images

- Game background
- Player car
- Four enemy cars
- Football / projectile
- Start screen
- Game Over screen
- Victory screen
- Game icon

### Audio

- Background music
- Car crash sound effect
- Car window smash sound effect

The background music is played continuously using:

```python
pygame.mixer.music.play(-1)
```

---

# ⚙️ Frame Rate & Delta Time

The game runs at **60 FPS**:

```python
FPS = 60
```

To make movement more independent from the computer's frame rate, the game uses **Delta Time (`dt`)**:

```python
dt = clock.tick(FPS) / 1000.0
```

Movement is then calculated using the object's speed multiplied by `dt`:

```python
position += speed * dt
```

This helps keep movement more consistent across different systems.

---

# 📚 How the Game Works

The overall execution flow is:

```text
1. Initialize Pygame
        ↓
2. Load Images and Sounds
        ↓
3. Show Start Screen
        ↓
4. Start Timer
        ↓
5. Read Keyboard Input
        ↓
6. Move Player
        ↓
7. Move Enemy Cars
        ↓
8. Move Ball
        ↓
9. Check Collisions
        ↓
10. Update Score and Health
        ↓
11. Draw Game Objects
        ↓
12. Check Win / Game Over
        ↓
13. Repeat Game Loop
```

---

# ▶️ Installation & Run

### 1. Install Python

Make sure Python 3.x is installed on your system.

### 2. Install Pygame

```bash
pip install pygame
```

### 3. Clone the Repository

```bash
git clone https://github.com/USERNAME/speed-racers.git
```

### 4. Open the Project Folder

```bash
cd speed-racers
```

### 5. Run the Game

```bash
python main.py
```

> Make sure the `image` and `sounds` folders keep the same structure and file names used by the code.

---

# 🎮 Controls

| Key | Action |
|-----|--------|
| `←` | Move left |
| `→` | Move right |
| `↑` | Move forward |
| `SPACE` | Shoot |
| `ENTER` | Restart after Game Over |
| `ESC` | Exit from Game Over |

---

# 📁 Project Structure

```text
Speed-Racers/
│
├── main.py
│
├── image/
│   ├── speed_racers.png
│   ├── speed_racers_background.jpg
│   ├── yellow_car.png
│   ├── car1.png
│   ├── car2.png
│   ├── car3.png
│   ├── car4.png
│   ├── football.png
│   ├── photo-output.jpeg
│   ├── photo-output3.jpeg
│   └── 6.jpeg
│
├── sounds/
│   ├── edm-gaming-music-335408.mp3
│   ├── Car-Window-Smash.mp3
│   └── car_crash_sound.mp3
│
└── README.md
```

---

# 🎯 Programming Concepts Used

- Python programming
- Pygame
- Game Loop
- Event Handling
- Keyboard and Mouse Input
- Collision Detection
- Random Number Generation
- Delta Time
- Game State Management
- Score System
- Health System
- Timer System
- Sound Management
- Image Rendering
- Functions
- Conditional Statements
- Loops

---

# 📖 What I Learned

This project helped me practice important concepts in **Python game development**, including Game Loop architecture, keyboard and mouse input, collision detection, timers, score and health systems, audio management, image rendering, and multiple game states such as Start, Playing, Game Over, and Victory.

I also learned how using **Delta Time** can make object movement more consistent across different frame rates.

---

## 👩‍💻 Project

**Speed Racers** — Built with ❤️ using **Python & Pygame**

