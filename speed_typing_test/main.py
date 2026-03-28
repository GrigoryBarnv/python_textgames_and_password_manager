import curses
from curses import wrapper
import time
import random


# Shows the welcome screen before the test starts.
def start_screen(stdscr):
	stdscr.clear()
	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
	stdscr.refresh()
	stdscr.getkey()

# Draws the target text, the typed text on top of it, and the WPM counter.
def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)  # show the full target sentence
	stdscr.addstr(1, 0, f"WPM: {wpm}")  # show the current words per minute below the text

	# Compare each typed character to the target and color it green or red.
	for i, char in enumerate(current):
		correct_char = target[i]  # expected character at this position
		color = curses.color_pair(1)  # green means correct
		if char != correct_char:
			color = curses.color_pair(2)  # red means wrong

		stdscr.addstr(0, i, char, color)  # draw the typed character over the original text

# Loads one random line from text.txt to use as the typing sentence.
def load_text():
	with open("text.txt", "r") as f:
		lines = f.readlines()
		return random.choice(lines).strip()

# Runs one typing round.
def wpm_test(stdscr):
	target_text = load_text()  # get a random sentence for this round
	current_text = []  # stores what the user has typed so far
	wpm = 0  # starting WPM value
	start_time = time.time()  # save when the round begins
	stdscr.nodelay(True)  # do not block forever while waiting for a key

	while True:
		time_elapsed = max(time.time() - start_time, 1)  # avoid division by zero
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)  # basic WPM formula

		stdscr.clear()  # clear the old frame before redrawing
		display_text(stdscr, target_text, current_text, wpm)  # draw text and WPM
		stdscr.refresh()  # update the visible screen

		# If the user finished the sentence, stop this round.
		if "".join(current_text) == target_text:
			stdscr.nodelay(False)  # restore normal blocking input mode
			break

		# Try to read a key. If no key is available yet, loop again.
		try:
			key = stdscr.getkey()
		except:
			continue

		# ESC ends the current round.
		if ord(key) == 27:
			break

		# Backspace removes the last typed character.
		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		# Any normal key is added until the sentence length is reached.
		elif len(current_text) < len(target_text):
			current_text.append(key)


# Sets up colors and runs the program loop.
def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # correct letters
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # wrong letters
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # extra default color

	start_screen(stdscr)  # show the intro screen once
	while True:
		wpm_test(stdscr)  # run one typing test
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()  # wait after the round ends
		
		# ESC from this screen closes the whole program.
		if ord(key) == 27:
			break

wrapper(main)  # start curses and call main(stdscr)
