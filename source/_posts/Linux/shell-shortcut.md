---
title: shell keyboard shortcut
date: 2020-07-08 00:09:01
---

<!-- toc -->

1. [tecmint](https://www.tecmint.com/linux-command-line-bash-shortcut-keys/)
2. [ostechnix](https://www.ostechnix.com/list-useful-bash-keyboard-shortcuts/)
3. [github help]()



# Move Cursor on The Command Line

- `Ctrl+A` or `Home` – moves the cursor to the start of a line.
- `Ctrl+E` or `End` – moves the cursor to the end of the line.
- `Ctrl+B` or `Left Arrow` – moves the cursor back **one character** at a time.
- `Ctrl+F` or `Right Arrow` – moves the cursor forward **one character** at a time.
- `Ctrl+Left Arrow` or `Esc\Alt` and then `B` – moves the cursor back **one word** at a time.
- `Ctrl+Right Arrow` or `Esc\Alt` and then `F` – moves the cursor forward **one word** at a time.

- `Alt+C` or `Esc+C` – **to capitalize the first letter of each word** and **moves the cursor forward one word**  at a time
- `CTRL+H` – Delete the characters before the cursor, same as `BASKSPACE`.
- `CTRL+X` – Lists the possible filename completions of the current word.

- `CTRL+XX` – Move between start of command line and current cursor position (and back again).

# Alt Commands

- **ALT+.** (note the **dot** at the end) – Use the last word of the previous command.
- **ALT+R** – Undo any changes to a command that you have brought from the history if you’ve edited it.

# Ctrl Commands

- `CTRL+J` – Same as ENTER/RETURN key.

  ​     ENTER key is not working? No problem! **CTRL+J** or **CTRL+M** can be used as an alternative to ENTER key.

- `CTRL+M` – Same as CTRL+J or RETURN.

- `CTRL+N` – Display next line in command history.

  You can also use `DOWN arrow`.

- `CTRL+P` – Displays the previous line in command history.

  You can also use `UP arrow`.

- `CTRL+[` – Equivalent to ESC key.



# Delete Text on the Command Line

- `Ctrl+D` or `Delete` – remove or deletes the character under the cursor.
- `Ctrl+K` – removes all text from the cursor to the end of the line.
- `CTRL+U` – Delete all characters before the cursor.
- `Ctrl+X` and then `Backspace` – removes all the text from the cursor to the beginning of the line.

- **`ALT+D`** – **Closes the empty Terminal (I.e it closes the Terminal when there is nothing typed). Also deletes all characters after the cursor.**

- `CTRL+W` – Delete the words before the cursor.

  Don’t confuse it with `CTRL+U`. `CTRL+W` won’t delete everything behind a cursor, but a single word.

  [![img](https://www.ostechnix.com/wp-content/uploads/2018/02/CTRLW-1.gif)](https://www.ostechnix.com/wp-content/uploads/2018/02/CTRLW-1.gif)



# Copy Text 

- `CTRL+V` – Makes the next character typed verbatim.

- `CTRL+Y` –  Retrieves last item that you deleted or cut.

  Remember, we deleted a word “-al” using CTRL+W in the 21st command. You can retrieve that word instantly using CTRL+Y.

  [![img](https://www.ostechnix.com/wp-content/uploads/2018/02/CTRLY-1.gif)](https://www.ostechnix.com/wp-content/uploads/2018/02/CTRLY-1.gif)

  See? I didn’t type “-al”. Instead, I pressed CTRL+Y to retrieve it.

  `Ctrl+U` and `CTRL+Y` shortcuts are very useful in situations where you want to quickly delete the commands and retrieve them instantly.

  `Ctrl-U` will delete from the cursor to the beginning of the line, and `Ctrl-Y` will bring it back.



# Transpose Text or Change Case on the Command Line

- `Ctrl+T` – transposes the character before the cursor with the character under the cursor.

   Let us say you typed “sl” instead of “ls”. No problem! This shortcut will transposes the characters as in the below screenshot.

  [![img](https://www.ostechnix.com/wp-content/uploads/2018/02/CTRLT-1.gif)](https://www.ostechnix.com/wp-content/uploads/2018/02/CTRLT-1.gif)

- `Esc+T` – transposes the two words immediately before (or under) the cursor.

- `ALT+T` – Swaps the last two words.

- `Esc+U` – transforms the text from the cursor to the end of the word to uppercase.

- `ALT+U` – Capitalize all characters in a word after the cursor.

- `Esc+L` – transforms the text from the cursor to the end of the word to lowercase.

- `ALT+L` – Uncaptalize all characters in a word after the cursor.



# Working With Processes in Linux

- `Ctrl+Z` – suspend the current foreground process. This sends the **SIGTSTP** signal to the process.  You can resume it later with **fg** in the foreground or **bg** in the background.
- `Ctrl+C` – interrupt the current foreground process, by sending the **SIGINT** signal to it. The default behavior is to terminate a process gracefully, but the process can either honor or ignore it.
- `Ctrl+D` – exit the bash shell (same as running the **exit** command).



# Bash Bang (!) Commands

- `!!` – execute last command.
- `!top` – execute the most recent command that starts with **‘top’** (e.g. **!**).
- `!top:p` – displays the command that **!top** would run (also adds it as the latest command in the command history).
- `!$` – execute the last word of the previous command (same as **Alt +**., e.g. if last command is ‘**cat tecmint.txt**’, then **!$** would try to run ‘**tecmint.txt**’).
- `!$:p` – displays the word that **!$** would execute.
- `!*` – displays the last word of the previous command.
- `!*:p` – displays the last word that **!\*** would substitute.



# Search Through Bash History

```shell
# the history file at startup time of a session
> export HISTFILESIZE=/path/.bash_history
# the number of lines or commands that (a) are allowed in the history file at startup time of a session, and (b) are stored in the history file at the end of your bash session for use in future sessions.
> export HISTFILESIZE=100
# the number of lines or commands that are stored in memory in a history list
> export HISTSIZE=100
```

- `Up arrow key` – retrieves the previous command. If you press it constantly, it takes you through multiple commands in history, so you can find the one you want. Use the **Down arrow** to move in the reverse direction through the history.

- `Ctrl+P` and `Ctrl+N` – alternatives for the **Up** and **Down** arrow keys, respectively.
- `Ctrl+R` – starts a reverse search, through the bash history, simply type characters that should be unique to the command you want to find in the history.
- `CTRL+O` – Run the command that you found using reverse search i.e `CTRL+R`.
- `Ctrl+J` – quit the search
- `Ctrl+S` – launches a forward search, through the bash history. -- how
- `Ctrl+G` – quits reverse or forward search, through the bash history. Leave the history searching mode without running the command.-- how



# Controlling The Screen

- `Ctrl+L` – clears the screen (same effect as the “**clear**” command, but redisplay the currently typed line.).
- `Ctrl+S` – pause all command output to the screen. If you have executed a command that produces verbose, long output, use this to pause the output scrolling down the screen.
- `Ctrl+Q` – resume output to the screen after pausing it with **Ctrl+S**.

# Launch an Editor

​     Open a terminal and press `Ctrl+X` and `Ctrl+E` to open an editor (**nano editor**) with an empty buffer. Bash will try to launch the editor defined by the **$EDITOR** environment variable.