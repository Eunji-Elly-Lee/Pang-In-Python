## Pang Game with Python

<div style="text-align:center">
    <img src="./img/attack.gif" width="48%">    
    <img src="./img/mission_complete.gif" width="48%">
</div>
<div style="text-align:center">
    <img src="./img/game_over.gif" width="48%">    
    <img src="./img/time_over.gif" width="48%">
</div>

### Description

This Python program implements the classic arcade game "Pang". In Pang, you control a character who must eliminate all the balls bouncing around the screen using a weapon.

- The player can move left and right using the arrow keys and launch weapons using the space key.
- At the start of the game, a large ball moves across the screen, splitting into smaller balls when hit by a weapon.
- The game ends if time runs out or your character is hit by a ball.

<br />

This Pang game is implemented using Pygame and can be run in Visual Studio Code.

### Features

- **Simple game play**: 화살표 키와 스페이스 키로 쉬운 컨드롤
- **Error handling**: 다른 키가 입력되었을 때 무시됨
- **다양한 공 조건**: 4가지 사이즈의 공이 있고 사이즈에 따라 공의 움직임 반경이 다름
- **좀 더 도전적**: 제일 작은 공을 맞춰야만 사라지지만 그것은 맞추기 어려움
- **Time limit**: Eliminate all balls before the 100-second timer runs out
- **자동 종료**: 미션을 완료하거나 게임에서 지면 프로그램이 자동 종료 됩니다

### Running the Game in VS Code

1. Open `pang.py`
2. Click the "Run Python File" icon (triangle) to start the game

### Additional Information

This project was created using Pygame with Visual Studio Code. <br />
Feel free to report any bugs or issues on the GitHub repository. <br />

<br />

**Have fun playing Pang!**
