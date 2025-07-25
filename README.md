# Pang Game with Python

## 💡 Overview

This Python program implements the classic arcade game "Pang". <br />
In Pang, you control a character who must eliminate all the balls bouncing around the screen using a weapon. The game ends if time runs out or your character is hit by a ball.

파이썬과 Pygame으로 구현된 고전 아케이드 게임 '팡(Pang)'입니다. <br />
캐릭터를 조작해 튀어다니는 공을 무기로 쏘아 제거해야 하며, 공에 맞거나 제한 시간이 지나면 게임이 종료됩니다.

## 🎮 How to Play

- The player can move left/right using arrow keys and fire weapons with the spacebar. <br />
  좌/우 방향키로 캐릭터를 이동시키고, 스페이스바로 무기를 발사합니다.
- Balls bounce and split into smaller ones when hit. <br />
  공은 벽과 바닥에 튕겨다니며, 무기에 맞으면 두 개의 더 작은 공으로 나뉩니다.
- Avoid ball collisions and clear all balls within 100 seconds. <br />
  공에 닿지 않도록 피하면서 제한 시간 100초 내에 모든 공을 제거하세요.

## 🔍 Features

- **Simple controls**: Arrow keys + spacebar <br />
  간단한 조작 (방향키 + 스페이스바)
- **Ball splitting logic**: Four sizes of balls with individual physics <br />
  4단계로 분할되는 크기의 공 구현
- **Collision detection**: Between character, weapon, and balls <br />
  캐릭터·무기·공 간의 충돌 판정 구현
- **Game result messages**: Mission Complete / Game Over / Time Over <br />
  게임 결과(성공, 실패, 시간 초과)에 따른 메시지 표시
- **Responsive timing**: 100-second countdown <br />
  100초 제한 시간 내에 미션 클리어
- **Automatic ending**: Game ends based on result condition <br />
  게임 결과에 따라 자동 종료

## 🛠 Run Instructions

1. Open `pang.py` in VS Code. <br />
   VS Code에서 `pang.py` 파일을 엽니다.
2. Click the "Run Python File" button. (▶️) <br />
   우측 상단의 ▶️ 버튼(“Run Python File”)을 클릭하여 실행합니다.

## 🖼 Screenshots

<details>
<summary>Click to view</summary>

![Attack Scene](/img/attack.gif)
![Mission Complete](/img/mission_complete.gif)
![Game Over](/img/game_over.gif)
![Time Over](/img/time_over.gif)

</details>

## 🧰 Tech Stack

| Category   | Tech               |
| ---------- | ------------------ |
| Language   | Python             |
| Library    | Pygame             |
| IDE        | Visual Studio Code |
| Game Style | 2D Arcade          |
