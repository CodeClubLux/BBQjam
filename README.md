#Installing py-game for python3

##OSX

* http://florian-berger.de/en/articles/installing-pygame-for-python-3-on-os-x/

###Install HomeBrew

```
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

###Install dependencies

```
brew install python3 mercurial git sdl sdl_image sdl_mixer sdl_ttf portmidi
brew tap homebrew/headonly
brew install --HEAD smpeg
/usr/local/bin/pip3 install hg+http://bitbucket.org/pygame/pygame
```


##Linux (with >= libstdc++6-4.9)
```
sudo apt-get install mercurial
hg clone https://bitbucket.org/pygame/pygamecd pygame
sudo apt-get install python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
python3 setup.py build
sudo python3 setup.py install
```


##Windows

* https://www.python.org/downloads/ (3.4.x)
* http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame (3.4 compatible)

#Testing it all out

```
python3
>>> import pygame
>>> pygame.init()
(6, 0)
>>> pygame.display.set_mode((800, 600))
<Surface(800x600x32 SW)>
>>> raise SystemExit
```

#IDE (Integrated Development Environments)

* https://www.eclipse.org/downloads/ (Standard)
* http://pydev.org/download.html (Copy Paste Install plugin URL)

OR a standalone py-dev version called LiClipse (Beta as of August 2014)

* http://brainwy.github.io/liclipse/

#CodeEditors


* http://www.sublimetext.com
* http://www.barebones.com/products/textwrangler/ (*OSX*)

