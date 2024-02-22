<h1 align="center">AYT Automater 😎 (Ass Youtube Automater)</h4>

<h4 align="center">AYTautomater (AssYT automater) | A youtube automater program made in less than 2 hours... 🥴🥴</h4>


## About AYT automater
A simple program I made for a youtube video. It allows you to turn a script into a video using the PixaBay API for images and a text-to-speech library (pyttsx3). You can also use it for Instagram and Tiktok if you'd like. I may/may not maintain this and this will most probably be archived but if you want to remix this and share it, Feel free to do so! Just please credit the original work to me :)



## Getting Started

How to setup and run AYT automater 1.0 :)

### Prerequisites

List of things needed for AYT automater
* Python (3.9 or above)
  
  ```sh
  https://python.org (official website)
  ```
* PIP (Python dependency installer)
  
  ```sh
  usage: pip install [dependency]
  ```
* MoviePy
  
  ```sh
  pip install moviepy
  ```
  
### Installation

_AYT Automater uses Pixabay Api, so get yourself one_

1. Get a free Pixabay API Key at  [https://pixabay.com/api/docs](https://pixabay.com/api/docs/)
2. Clone or download this github repo:
   
   ```sh
   git clone https://github.com/FlippantDev/AYTautomater/
   ```
4. Extract the Zip file (if you downloaded it)
   ```sh
   or you can use winrar to extract it
   ```
5. Install Dependencies with [requirements.bat] or open cmd in the directory and install with Pip
   ```sh
   pip install -r requirements.txt
   ```
6. Open `videomaker.py` with your preferred code editor
7. Enter your API key on line 16
   ```python
   url = f'https://pixabay.com/api/?key=(YOUR API KEY GOES HERE)&q={search_term}&image_type=photo&pretty=true&per_page=20'';
   ```
6. Save changes by using command `CRTL + S`
7. Open `script.txt`
8. in script.txt you have to put in the script that the video will say
9. Open `stocktopic.txt`
10. Type in the topic of what your script is about, it has to be 1 word (ex. space)



> **Note**
> This project was made for a video I was planning to make, so I may not update it



## My other projects : 

[wmapper-web](https://wmapperweb.web.app) - Wmapper (keymap all across windows) (maintainance : active)

## License

Apache 2.0
