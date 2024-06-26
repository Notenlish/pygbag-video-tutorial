# pygbag-video-tutorial

A sample project on how to add web export to your pygame games using [pygbag](https://pypi.org/project/pygbag/)

## Steps

`pip install pygbag`
`pygbag .`
`pygbag --archive .` --> to package for itch.io

if it says that pygbag isnt installed even though you have it installed try using: `py -m pygbag {yourProjectRoot}`

## Getting Help
[Pygame Community discord server](https://discord.com/invite/pygame) 

[Pygame Web Documentation](https://pygame-web.github.io/)

## Assets Used

Ground and Player sprites from: [Kenney platformer Pack Redux](https://kenney.nl/assets/platformer-pack-redux)

jump sound made with: [ChipTone](https://sfbgames.itch.io/chiptone)

Font from: [dafont.com](https://www.dafont.com/renogare.font)

NOTE: if you minimize your browser while testing your game for web and then wait some time and come back, it will register the time where the browser wasnt active as time elapsed so you will get a really big delta time value for a single frame which CAN mess some stuff up, I recommend you limit your deltatime variable.
