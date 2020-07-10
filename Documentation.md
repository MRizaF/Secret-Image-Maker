Motives & Background
-----
This is actually my old project in "Game Maker 8" (you can find it [here](https://gmindo.forumid.net/t1267-secret-image-maker)). I think the motive at that time was, I really wanted to make an application, and right then, I just learned something interesting, namely steganography. therefore, this application was born.

And the motive for now is, I want to challenge myself to make my old application in "Python", learn to understand the new GUI API so that I can design the application, and of course to hone my coding skills.

Project Duration
-----
I started on June 24, 2020 and finished on July 5, 2020

but I think, the time really used to make this application is about 3-4 days (if I really focus on it)

Code Structures
-----
```bash
Secret Image Maker
├── assets
│   ├── Secret Image Maker - Icon.png
│   ├── Secret Image Maker - Banner.png
│   └── gui_sim.py
├── 7za.exe
└── Secret Image Maker.py
```
- Secret Image Maker.py = Main class / starting point
- 7za.exe = To archive files
- gui_sim.py = GUI code

Class and Function Interface
-----
File : Secret Image Maker.py
Function Name | Access Level | Parameter | Return
--------------|--------------|-----------|-------
OnDropFiles | Public | x: int; y: int; filenames: path| None
ShowAbout | Public | event: event | None
ChooseImage | Public | event: event | None
AddFiles | Public | event: event | None
DeleteSelection | Public | event: event | None
ClearFiles | Public | event: event | None
CreateImage | Public | event: event | None
convert_bytes | Public | bytes_number: int | str
set_files | Public | pathfiles: list | None
set_status | Public | status: str; gauge: int | None

Statistics
-----
- Secret Image Maker.py => 172 lines (163 lines by me)
- gui_sim.py => 162 lines (19 lines by me, the rest generated from wxformbuilder)
