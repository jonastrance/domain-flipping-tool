# 🚀 Space Shooter - Galactic Defense

A fun, fast-paced browser-based space shooter game built with HTML5 Canvas and JavaScript.

## Features

### Core Gameplay
- **Player Controls**: Smooth spaceship movement using Arrow Keys or WASD
- **Shooting Mechanics**: Fire colorful laser bullets with SPACE key
- **Enemy Waves**: Multiple enemy types that spawn from the top and move down
- **Collision Detection**: Precise hit detection for bullets and enemies

### Game Systems
- **Score Tracking**: Earn points for each enemy destroyed (multiplied by level)
- **Health System**: Visual health bar that depletes when hit by enemies
- **Level Progression**: Infinite levels with increasing difficulty
- **Multiple Enemy Types**: Three different enemy designs with varying behaviors
- **Enemy Health**: Tougher enemies appear in higher levels with health bars

### Visual Effects
- **Animated Star Field**: Parallax scrolling background
- **Particle Explosions**: Colorful particle effects when enemies are destroyed
- **Colorful Graphics**: Vibrant neon-style spaceships and enemies
- **Smooth Animations**: 60 FPS gameplay with canvas rendering
- **Health Bar**: Dynamic health visualization
- **UI Overlay**: Real-time score, level, and health display

### Difficulty Progression
- Enemy spawn rate increases each level
- Enemy speed increases with level
- Enemies gain more health in higher levels
- More points awarded per kill in higher levels

## How to Play

### Starting the Game
1. Open `index.html` in any modern web browser
2. Click "START GAME" button
3. Defend the galaxy!

### Controls
- **Movement**:
  - Arrow Keys (← →) or A/D keys to move left and right
- **Shooting**:
  - SPACE bar to fire bullets
- **Restart**:
  - Click "PLAY AGAIN" after game over

### Gameplay Tips
- Keep moving to avoid enemy collisions
- Don't let enemies reach the bottom of the screen (health penalty)
- Direct hits from enemies deal more damage than missed enemies
- Higher levels = more points per kill
- Watch your health bar!

### Enemy Types
1. **Red Triangles**: Fast and aggressive
2. **Orange Squares**: Balanced speed and durability
3. **Pink Circles**: Varied patterns

## Technical Details

### Technologies Used
- HTML5 Canvas for rendering
- Vanilla JavaScript (ES6+)
- CSS3 for UI styling
- No external dependencies required

### Game Architecture
- **Object-Oriented Design**: Separate classes for Player, Enemy, Bullet, Particle, and Star
- **Game Loop**: RequestAnimationFrame for smooth 60 FPS
- **Collision Detection**: AABB (Axis-Aligned Bounding Box) algorithm
- **Particle System**: Dynamic particle effects for explosions
- **State Management**: Clean game state with restart functionality

### Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Any modern browser with HTML5 Canvas support

## File Structure
```
space-shooter-game/
├── index.html          # Complete game in a single file
└── README.md          # This file
```

## Customization

The game is easy to customize! All code is in a single HTML file:

- **Difficulty**: Adjust `enemySpawnRate`, `player.speed`, or `enemy.speed`
- **Colors**: Modify the color arrays in Enemy and Bullet classes
- **Health**: Change `player.maxHealth` or damage values
- **Shooting**: Adjust `shootCooldown` for fire rate
- **Canvas Size**: Modify canvas width/height attributes

## Future Enhancement Ideas
- Power-ups (shield, rapid fire, multi-shot)
- Boss battles every 5 levels
- Sound effects and music
- High score persistence (localStorage)
- Mobile touch controls
- Different weapon types
- Player ship upgrades

## Credits
Created as a fun browser-based space shooter game demonstrating HTML5 Canvas capabilities.

Enjoy defending the galaxy! 🌌
