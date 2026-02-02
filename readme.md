# Flappy Bird

**Flappy Bird** je 2D arkádová hra, v ktorej hráč ovláda malého vtáčika, ktorý prelieta pomedzi prekážky, aby sa vyhol otrasu mozgu.

![flappy_default.png](assets/images/flappy_default.png)
![flappy_settings.png](assets/images/flappy_settings.png)
![flappy_gameplay.png](assets/images/flappy_gameplay.png)
![flappy_game_over.png](assets/images/flappy_game_over.png)
## Pointa hry
- Hráč ovláda vtáčika.
- Hlavnou úlohou je **vyhýbať sa trubkám**, ktoré su z nejakého dôvodu rozmiestnené z hora aj z dola priamočiaro v meste.
- Získať čo najvyššie skóre.
- Hra končí stavom *Game Over*, keď dôjde ku kolízii.

## Inštalácia

Projekt používa správu závislostí cez `pyproject.toml`.  
Závislosti nainštaluješ príkazom:

```bash
pip install -e
```
## Ovládanie
#### kliknutí myšky na tlačidlo štart spustíme hru

| Klávesa                                    | Akcia |
|:-------------------------------------------| :--- |
| **Medzerník (Space) / Ľavé tlačidlo myši** | Skok |
| **ESC**                                    | Ukončenie celého programu |

## Vlastnosti hry

- **Zvuk:** Zvukové efekty pre lepší zážitok.
- **Počítanie skóre:** Sledovanie úspešnosti hráča.
- **OOP:** Použitie tried a objektov v kóde.
- **Game Over stav:** Jasné ukončenie hry pri neúspechu.
- **Grafika:** Použitie farieb, textu a pixel-art štýlu.

## Rozdelenie práce
**Tomáš Ivan** - engine, vzhľad
 
**Lukáš Červeňák** - menu, vzhľad

**Pavol Lompart** - zvuk, readme :)

## Credits

Projekt využíva hudbu a zvukové efekty z nasledujúcich stránok:

https://mixkit.co/free-sound-effects/

https://uppbeat.io/music/category/game

### prezentácia
https://www.canva.com/design/DAHALEuIo1c/SC7cU0l6MyJnVUZDh2q2kQ/view?utm_content=DAHALEuIo1c&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h987e74622d