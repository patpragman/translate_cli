# Your Command Line Tool Name

## Description

I got tired of always going to google translate when I wanted to translate something, I decided I needed a command line tool.
ArgosTranslate is amazing, but I wanted a wrapper for the tool, I also wanted some custom functionality including the
the ability to detect languages and text-to-speech so I could hear what it sounded like.

## Installation

Requires a little bit of work to install, but it's not crazy.  Not sure if it works in lower versions, but I used Python
3.11.0rc1 when I wrote this.  I imagine it'll probably work back to 3.6.

### Prerequisites

You'll need to be able to clone a repository and navigate to it, that's pretty much it.

### Steps

1. **Clone the Repository **
   
`git clone https://github.com/patpragman/translation_cli.git`

2. **Navigate to the Directory**

`cd <directory where you cloned the repository>`

3. **Install**

- run setup.sh, you will need to use sudo to install espeak globally, if you don't want to, or have some other snag, 
remove sudo from the setup.sh files as appropriate

`setup.sh`

This code does the following:

1. Installs espeak with sudo
2. creates a virtual environment for the project
3. installs the required dependencies
4. runs setup.py which installs the language models and builds the shell script that you'll run
5. makes it executable
6. copies the generated wrapper to `/usr/local/bin/translate`
7. runs the script once

This worked fine on my machine to set it up, if for some reason it isn't working, send me an email and I'll happily take
the time to walk you through the set up, this is something I did while drinking and playing with christmas presents on 
christmas day, so... I guess "sorry" if it doesn't work, but I'll happily try to help you set it up if you're actually 
interested.

## Usage

### Basic Translation

Translate text from a specified source language to a target language:

`python translate.py --from_lang [source_language_code] --to_lang [target_language_code] "Your text here"`

### Automatic Language Detection

If the source language is not specified, the tool will attempt to detect it automatically:

`python translate.py --verbose --to_lang [target_language_code] "Your text here"`

### Text-to-Speech

To hear the translation spoken aloud:

python translate.py --to_lang [target_language_code] --speak "Your text here"

### Options

* `--from_lang` or `-f`: Source language code (e.g., 'es' for Spanish). If omitted, the tool attempts to detect the language.
* `--to_lang` or `-t`: Target language code (default is 'en' for English).
* `--verbose` or `-v`: Enable verbose mode for detailed output.
* `--speak` or `-s`: Activate text-to-speech to hear the translation.

### Example

`python translate.py --to_lang en --speak "Hola, ¿cómo estás?"`


