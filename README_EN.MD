# Instagram Blocker

A simple Python application that allows you to block Instagram accounts in bulk.

## Table of Contents
- [Instagram Blocker](#instagram-blocker)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Important Notes](#important-notes)
  - [Usage](#usage)
  - [Security](#security)
  - [Developer Notes](#developer-notes)
    - [Requirements](#requirements)
    - [Setup](#setup)
    - [Contributing](#contributing)
  - [Bug Reports](#bug-reports)
  - [License](#license)

## Installation

1. Download the latest release from the [Releases](https://github.com/0baris/instagram-blocker/releases) page
2. Extract the downloaded .zip file
3. Open `block_list.txt` and add the accounts you want to block (one account per line)
4. Run `instagram-blocker.exe`

## Important Notes

- You must temporarily disable Two-Factor Authentication before running the program
- Do not attempt to block more than 100 accounts at once
- Wait approximately 3-3.5 hours after blocking 100 accounts
- You can review all the code, it poses no risk to your account

## Usage

1. Run the program
2. Enter your Instagram username and password
3. The program will automatically start blocking accounts listed in `block_list.txt`

## Security

- Your username and password are only used to log in to Instagram
- No data is stored or shared with third parties
- All operations are performed locally on your computer

## Developer Notes

### Requirements
- Python 3.8+

### Setup
```bash
# Clone the repository
git clone https://github.com/0baris/instagram-blocker.git

# Install required packages
pip install -r requirements.txt

# Start script
python main.py
```

### Contributing
1. Fork this repository
2. Create a new branch (`git checkout -b feature/newFeature`)
3. Commit your changes (`git commit -am 'Add new feature: Description'`)
4. Push to the branch (`git push origin feature/newFeature`)
5. Create a Pull Request

## Bug Reports

If you encounter any bugs or issues, please open an issue on GitHub.

## License

MIT License