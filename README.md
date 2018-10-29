# Turtle Project

## Tools used
- Sublime Text 3
- Python 3
- Turtle
- Terminal (Ubuntu Subsystem for Windows)

## Objective
- Make a simple bar chart program using turtle library.
- Barchart is able to scale appropriately

## Windows Setup
- Enable Linux Subsystem if not already done
	- Search for 'Turn Windows Features On or Off' in start menu
	- Search for 'Linux Subsystem'
	- Enable it
- Go to Windows store and get Ubuntu 18.01 LTS
	- Install it
- Run Ubuntu and setup
	- Give it awhile to 'install'
	- You will be prompt for a username and password for the 'Ubuntu Subsystem'
		- This is different from your Windows account
	- Type `sudo apt update`
		- Enter your ubuntu password
		- Wait till it finishes
	- Type `sudo apt upgrade`
		- Wait till it finishes
	- Type `sudo apt-get install python3`
		- Wait till it finishes
	- Type `sudo apt-get install python3-tk`
		- Used by python's turtle library
		- Wait till it finishes
- Install Xming for windows
	- Google Xming
	- Install it
- Setup screen for ubuntu subsystem
	- Type `nano .bash_profile`
	- Add the line `export DISPLAY=localhost:0.0`
	- Press the key combination for write
	- Press Enter to save the file
	- Press the key combination for exit
